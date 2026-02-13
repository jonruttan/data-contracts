from __future__ import annotations

import json
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

from spec_runner.assertions import (
    _raise_with_assert_context,
    assert_text_op,
    eval_assert_tree,
    is_text_op,
    iter_leaf_assertions,
)


def _contract_root_for(doc_path: Path) -> Path:
    p = doc_path.resolve()
    for cur in (p.parent, *p.parent.parents):
        if (cur / ".git").exists():
            return cur
    return p.parent


def _resolve_relative_subject_path(doc_path: Path, rel: str) -> Path:
    rel_p = Path(str(rel))
    if rel_p.is_absolute():
        raise ValueError("api.http request.url relative path must not be absolute")
    p = (doc_path.parent / rel_p).resolve()
    root = _contract_root_for(doc_path)
    try:
        p.relative_to(root)
    except ValueError as e:
        raise ValueError("api.http request.url relative path escapes contract root") from e
    return p


def _fetch_response(case, *, method: str, url: str, headers: dict[str, str], body_bytes: bytes | None, timeout_seconds: float) -> dict[str, Any]:
    parsed = urllib.parse.urlparse(url)
    if not parsed.scheme:
        subject = _resolve_relative_subject_path(case.doc_path, url)
        text = subject.read_text(encoding="utf-8")
        return {"status": 200, "headers": {}, "body_text": text}

    if parsed.scheme == "file":
        subject = Path(urllib.parse.unquote(parsed.path))
        text = subject.read_text(encoding="utf-8")
        return {"status": 200, "headers": {}, "body_text": text}

    req = urllib.request.Request(url=url, method=method, headers=headers, data=body_bytes)
    with urllib.request.urlopen(req, timeout=timeout_seconds) as resp:  # nosec B310 (explicit, spec-driven runtime behavior)
        raw = resp.read()
        text = raw.decode("utf-8")
        hdrs = {str(k).strip(): str(v).strip() for k, v in resp.headers.items()}
        status = int(getattr(resp, "status", None) or resp.getcode() or 0)
        return {"status": status, "headers": hdrs, "body_text": text}


def run(case, *, ctx) -> None:
    t = case.test
    case_id = str(t.get("id", ""))
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

    h = t.get("harness") or {}
    if not isinstance(h, dict):
        raise TypeError("harness must be a mapping")
    timeout_seconds = float(h.get("timeout_seconds", 5))

    response = _fetch_response(
        case,
        method=method,
        url=url,
        headers=headers,
        body_bytes=body_bytes,
        timeout_seconds=timeout_seconds,
    )
    status_text = str(int(response["status"]))
    headers_text = "\n".join(f"{k}: {v}" for k, v in sorted(response["headers"].items()))
    body_text_value = str(response["body_text"])
    body_json_value = json.loads(body_text_value)

    def _eval_leaf(leaf: dict, *, inherited_target: str | None = None, assert_path: str = "assert") -> None:
        for target, op, value, is_true in iter_leaf_assertions(leaf, target_override=inherited_target):
            try:
                if target == "status":
                    if not is_text_op(op):
                        raise ValueError(f"unsupported op for status: {op}")
                    assert_text_op(status_text, op, value, is_true=is_true)
                elif target == "headers":
                    if not is_text_op(op):
                        raise ValueError(f"unsupported op for headers: {op}")
                    assert_text_op(headers_text, op, value, is_true=is_true)
                elif target == "body_text":
                    if op == "json_type":
                        want = str(value).strip().lower()
                        if want == "dict":
                            assert isinstance(body_json_value, dict)
                        elif want == "list":
                            assert isinstance(body_json_value, list)
                        else:
                            raise ValueError(f"unsupported json_type: {value}")
                    elif is_text_op(op):
                        assert_text_op(body_text_value, op, value, is_true=is_true)
                    else:
                        raise ValueError(f"unsupported op for body_text: {op}")
                elif target == "body_json":
                    if op == "json_type":
                        want = str(value).strip().lower()
                        if want == "dict":
                            assert isinstance(body_json_value, dict)
                        elif want == "list":
                            assert isinstance(body_json_value, list)
                        else:
                            raise ValueError(f"unsupported json_type: {value}")
                    elif is_text_op(op):
                        assert_text_op(json.dumps(body_json_value, sort_keys=True), op, value, is_true=is_true)
                    else:
                        raise ValueError(f"unsupported op for body_json: {op}")
                else:
                    raise ValueError(f"unknown assert target for api.http: {target}")
            except BaseException as e:  # noqa: BLE001
                _raise_with_assert_context(
                    e,
                    case_id=case_id,
                    assert_path=assert_path,
                    target=target,
                    op=op,
                )

    eval_assert_tree(t.get("assert", []) or [], eval_leaf=_eval_leaf)
