from __future__ import annotations

import base64
import json
import os
import time
import urllib.parse
import urllib.request
from urllib.error import HTTPError, URLError
from pathlib import Path
from typing import Any

from spec_runner.assertions import (
    evaluate_internal_assert_tree,
)
from spec_runner.compiler import compile_external_case
from spec_runner.spec_lang_libraries import load_spec_lang_symbols_for_case
from spec_runner.spec_lang import compile_import_bindings, limits_from_harness
from spec_runner.virtual_paths import contract_root_for, resolve_contract_path

_OAUTH_TOKEN_CACHE: dict[tuple[str, str, str, str], tuple[str, float]] = {}


def _resolve_relative_subject_path(doc_path: Path, rel: str) -> Path:
    try:
        return resolve_contract_path(
            contract_root_for(doc_path), str(rel), field="api.http request.url path"
        )
    except ValueError as e:
        raise ValueError(str(e)) from e


def _is_live_network_url(url: str) -> bool:
    parsed = urllib.parse.urlparse(url)
    return parsed.scheme.lower() in {"http", "https"}


def _has_header(headers: dict[str, str], key: str) -> bool:
    want = key.strip().lower()
    return any(str(k).strip().lower() == want for k in headers)


def _env_required(ctx, name: str) -> str:
    env_name = str(name).strip()
    if not env_name:
        raise ValueError("api.http oauth env var name must be a non-empty string")
    raw = None
    if getattr(ctx, "env", None) is not None:
        raw = ctx.env.get(env_name)
    if raw is None:
        raw = os.environ.get(env_name)
    if raw is None or str(raw).strip() == "":
        raise ValueError(f"api.http oauth env var is required: {env_name}")
    return str(raw)


def _parse_api_http_harness(case_harness: dict[str, Any]) -> tuple[str, dict[str, Any] | None]:
    api_http = case_harness.get("api_http") if isinstance(case_harness, dict) else None
    if api_http is None:
        return "deterministic", None
    if not isinstance(api_http, dict):
        raise TypeError("harness.api_http must be a mapping")
    mode = str(api_http.get("mode", "deterministic")).strip().lower() or "deterministic"
    if mode not in {"deterministic", "live"}:
        raise ValueError("harness.api_http.mode must be one of: deterministic, live")

    auth = api_http.get("auth")
    if auth is None:
        return mode, None
    if not isinstance(auth, dict):
        raise TypeError("harness.api_http.auth must be a mapping")
    oauth = auth.get("oauth")
    if oauth is None:
        return mode, None
    if not isinstance(oauth, dict):
        raise TypeError("harness.api_http.auth.oauth must be a mapping")

    grant_type = str(oauth.get("grant_type", "client_credentials")).strip().lower() or "client_credentials"
    if grant_type != "client_credentials":
        raise ValueError("api.http oauth grant_type must be client_credentials")

    token_url = str(oauth.get("token_url", "")).strip()
    if not token_url:
        raise ValueError("api.http oauth token_url is required")

    client_id_env = str(oauth.get("client_id_env", "")).strip()
    if not client_id_env:
        raise ValueError("api.http oauth client_id_env is required")
    client_secret_env = str(oauth.get("client_secret_env", "")).strip()
    if not client_secret_env:
        raise ValueError("api.http oauth client_secret_env is required")

    auth_style = str(oauth.get("auth_style", "basic")).strip().lower() or "basic"
    if auth_style not in {"basic", "body"}:
        raise ValueError("api.http oauth auth_style must be one of: basic, body")

    token_field = str(oauth.get("token_field", "access_token")).strip() or "access_token"
    expires_field = str(oauth.get("expires_field", "expires_in")).strip() or "expires_in"

    skew_raw = oauth.get("refresh_skew_seconds", 30)
    try:
        refresh_skew_seconds = int(skew_raw)
    except Exception as e:  # noqa: BLE001
        raise TypeError("api.http oauth refresh_skew_seconds must be an integer") from e
    if refresh_skew_seconds < 0:
        raise ValueError("api.http oauth refresh_skew_seconds must be >= 0")

    scope = oauth.get("scope")
    audience = oauth.get("audience")

    return mode, {
        "grant_type": grant_type,
        "token_url": token_url,
        "client_id_env": client_id_env,
        "client_secret_env": client_secret_env,
        "scope": None if scope is None else str(scope),
        "audience": None if audience is None else str(audience),
        "auth_style": auth_style,
        "token_field": token_field,
        "expires_field": expires_field,
        "refresh_skew_seconds": refresh_skew_seconds,
    }


def _load_token_payload_from_url(
    case,
    *,
    token_url: str,
    timeout_seconds: float,
    mode: str,
    client_id: str,
    client_secret: str,
    grant_type: str,
    scope: str | None,
    audience: str | None,
    auth_style: str,
) -> dict[str, Any]:
    parsed = urllib.parse.urlparse(token_url)
    if not parsed.scheme:
        path = _resolve_relative_subject_path(case.doc_path, token_url)
        return json.loads(path.read_text(encoding="utf-8"))
    if parsed.scheme == "file":
        path = Path(urllib.parse.unquote(parsed.path))
        return json.loads(path.read_text(encoding="utf-8"))
    if _is_live_network_url(token_url):
        if mode != "live":
            raise ValueError("api.http oauth token_url network fetch requires harness.api_http.mode=live")
        form: dict[str, str] = {"grant_type": grant_type}
        if scope:
            form["scope"] = str(scope)
        if audience:
            form["audience"] = str(audience)
        headers: dict[str, str] = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
        }
        if auth_style == "basic":
            pair = f"{client_id}:{client_secret}".encode("utf-8")
            headers["Authorization"] = "Basic " + base64.b64encode(pair).decode("ascii")
        else:
            form["client_id"] = client_id
            form["client_secret"] = client_secret
        data = urllib.parse.urlencode(form).encode("utf-8")
        req = urllib.request.Request(url=token_url, method="POST", headers=headers, data=data)
        try:
            with urllib.request.urlopen(req, timeout=timeout_seconds) as resp:  # nosec B310
                body = resp.read().decode("utf-8")
        except HTTPError as e:
            raise RuntimeError(f"api.http oauth token request failed with HTTP {int(e.code)}") from e
        except URLError as e:
            raise RuntimeError("api.http oauth token request failed") from e
        try:
            parsed_body = json.loads(body)
        except json.JSONDecodeError as e:
            raise RuntimeError("api.http oauth token response is not valid JSON") from e
        if not isinstance(parsed_body, dict):
            raise RuntimeError("api.http oauth token response must be a JSON object")
        return parsed_body
    raise ValueError(f"api.http oauth token_url scheme is not supported: {parsed.scheme}")


def _oauth_access_token(case, *, ctx, oauth: dict[str, Any], timeout_seconds: float, mode: str) -> tuple[str, bool, float]:
    token_url = str(oauth["token_url"])
    scope = oauth.get("scope")
    audience = oauth.get("audience")
    cache_key = (
        token_url,
        str(oauth["client_id_env"]),
        "" if scope is None else str(scope),
        "" if audience is None else str(audience),
    )
    now = time.time()
    cached = _OAUTH_TOKEN_CACHE.get(cache_key)
    if cached is not None:
        token, expires_at = cached
        if now < expires_at - int(oauth["refresh_skew_seconds"]):
            return token, True, 0.0

    client_id = _env_required(ctx, str(oauth["client_id_env"]))
    client_secret = _env_required(ctx, str(oauth["client_secret_env"]))
    started = time.perf_counter()
    payload = _load_token_payload_from_url(
        case,
        token_url=token_url,
        timeout_seconds=timeout_seconds,
        mode=mode,
        client_id=client_id,
        client_secret=client_secret,
        grant_type=str(oauth["grant_type"]),
        scope=None if scope is None else str(scope),
        audience=None if audience is None else str(audience),
        auth_style=str(oauth["auth_style"]),
    )
    fetch_ms = (time.perf_counter() - started) * 1000.0
    token_field = str(oauth["token_field"])
    raw_token = payload.get(token_field)
    if raw_token is None or str(raw_token).strip() == "":
        raise RuntimeError(f"api.http oauth token response missing field: {token_field}")
    access_token = str(raw_token)

    expires_in = payload.get(str(oauth["expires_field"]), 3600)
    try:
        expires_seconds = float(expires_in)
    except Exception:
        expires_seconds = 3600.0
    _OAUTH_TOKEN_CACHE[cache_key] = (access_token, now + max(expires_seconds, 0.0))
    return access_token, False, fetch_ms


def _fetch_response(
    case,
    *,
    method: str,
    url: str,
    headers: dict[str, str],
    body_bytes: bytes | None,
    timeout_seconds: float,
    mode: str,
) -> dict[str, Any]:
    parsed = urllib.parse.urlparse(url)
    if not parsed.scheme:
        subject = _resolve_relative_subject_path(case.doc_path, url)
        text = subject.read_text(encoding="utf-8")
        return {"status": 200, "headers": {}, "body_text": text}

    if parsed.scheme == "file":
        subject = Path(urllib.parse.unquote(parsed.path))
        text = subject.read_text(encoding="utf-8")
        return {"status": 200, "headers": {}, "body_text": text}

    if _is_live_network_url(url) and mode != "live":
        raise ValueError("api.http request.url network fetch requires harness.api_http.mode=live")

    req = urllib.request.Request(url=url, method=method, headers=headers, data=body_bytes)
    with urllib.request.urlopen(req, timeout=timeout_seconds) as resp:  # nosec B310 (explicit, spec-driven runtime behavior)
        raw = resp.read()
        text = raw.decode("utf-8")
        hdrs = {str(k).strip(): str(v).strip() for k, v in resp.headers.items()}
        status = int(getattr(resp, "status", None) or resp.getcode() or 0)
        return {"status": status, "headers": hdrs, "body_text": text}


def run(case, *, ctx) -> None:
    if hasattr(case, "test") and hasattr(case, "doc_path"):
        case = compile_external_case(case.test, doc_path=case.doc_path)
    t = case.raw_case
    case_id = case.id
    request = t.get("request")
    if not isinstance(request, dict):
        raise TypeError("api.http requires request mapping")

    method = str(request.get("method", "")).strip().upper()
    if not method:
        raise ValueError("api.http request.method is required")
    url = str(request.get("url", "")).strip()
    if not url:
        raise ValueError("api.http request.url is required")

    raw_headers = request.get("headers") or {}
    if not isinstance(raw_headers, dict):
        raise TypeError("api.http request.headers must be a mapping")
    headers = {str(k).strip(): str(v).strip() for k, v in raw_headers.items()}

    body_text = request.get("body_text")
    body_json = request.get("body_json")
    if body_text is not None and body_json is not None:
        raise ValueError("api.http request.body_text and request.body_json are mutually exclusive")
    body_bytes: bytes | None = None
    if body_text is not None:
        body_bytes = str(body_text).encode("utf-8")
    elif body_json is not None:
        body_bytes = json.dumps(body_json, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        if "Content-Type" not in headers:
            headers["Content-Type"] = "application/json"

    h = case.harness
    mode, oauth = _parse_api_http_harness(h)
    spec_lang_limits = limits_from_harness(h)
    spec_lang_imports = compile_import_bindings((h or {}).get("spec_lang"))
    spec_lang_symbols = load_spec_lang_symbols_for_case(
        doc_path=case.doc_path,
        harness=h,
        limits=spec_lang_limits,
    )
    timeout_seconds = float(h.get("timeout_seconds", 5))
    auth_mode = "none"
    oauth_token_source = "none"
    oauth_context: dict[str, Any] = {}
    if oauth is not None:
        auth_mode = "oauth"
        oauth_token_source = "env_ref"
        token, used_cached_token, token_fetch_ms = _oauth_access_token(
            case,
            ctx=ctx,
            oauth=oauth,
            timeout_seconds=timeout_seconds,
            mode=mode,
        )
        if not _has_header(headers, "Authorization"):
            headers["Authorization"] = f"Bearer {token}"
        token_host = urllib.parse.urlparse(str(oauth["token_url"])).hostname
        oauth_context = {
            "token_url_host": token_host,
            "scope_requested": oauth.get("scope"),
            "token_fetch_ms": token_fetch_ms,
            "used_cached_token": used_cached_token,
        }

    response = _fetch_response(
        case,
        method=method,
        url=url,
        headers=headers,
        body_bytes=body_bytes,
        timeout_seconds=timeout_seconds,
        mode=mode,
    )
    status_text = str(int(response["status"]))
    headers_text = "\n".join(f"{k}: {v}" for k, v in sorted(response["headers"].items()))
    body_text_value = str(response["body_text"])
    body_json_value = json.loads(body_text_value)
    context_profile = {
        "profile_id": "api.http/v1",
        "profile_version": 1,
        "value": {
            "status": int(response["status"]),
            "headers": response["headers"],
            "body_text": body_text_value,
            "body_json": body_json_value,
        },
        "meta": {
            "target": "api.http",
            "method": method,
            "url": url,
            "auth_mode": auth_mode,
            "oauth_token_source": oauth_token_source,
        },
        "context": {
            "timeout_seconds": timeout_seconds,
            "oauth": oauth_context,
        },
    }

    def _subject_for_key(subject_key: str):
        if subject_key == "status":
            return status_text
        if subject_key == "headers":
            return headers_text
        if subject_key == "body_text":
            return body_text_value
        if subject_key == "body_json":
            return body_json_value
        if subject_key == "context_json":
            return context_profile
        raise ValueError(f"unknown assert target for api.http: {subject_key}")

    evaluate_internal_assert_tree(
        case.assert_tree,
        case_id=case_id,
        subject_for_key=_subject_for_key,
        limits=spec_lang_limits,
        symbols=spec_lang_symbols,
        imports=spec_lang_imports,
    )
