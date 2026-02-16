# SPEC-OPT-OUT: Exercises behavior not yet representable as stable .spec.md coverage (unit-level API/diagnostic/infrastructure checks).
import pytest

from spec_runner.dispatcher import SpecRunContext
from spec_runner.doc_parser import SpecDocTest


def test_api_http_relative_fixture_passes(tmp_path, monkeypatch, capsys):
    fixture = tmp_path / "fixtures" / "ok.json"
    fixture.parent.mkdir(parents=True)
    fixture.write_text('{"ok": true}', encoding="utf-8")
    doc = tmp_path / "case.spec.md"
    doc.write_text("# case\n", encoding="utf-8")
    case = SpecDocTest(
        doc_path=doc,
        test={
            "id": "SR-API-UNIT-001",
            "type": "api.http",
            "request": {
                "method": "GET",
                "url": "/fixtures/ok.json",
            },
            "assert": [
                {"target": "status", "must": [{"evaluate": [{"contains": [{"var": "subject"}, "200"]}]}]},
                {"target": "body_json", "must": [{"evaluate": [{"json_type": [{"var": "subject"}, "dict"]}]}]},
            ],
        },
    )
    from spec_runner.harnesses.api_http import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys))


def test_api_http_requires_request_mapping(tmp_path, monkeypatch, capsys):
    doc = tmp_path / "case.spec.md"
    doc.write_text("# case\n", encoding="utf-8")
    case = SpecDocTest(
        doc_path=doc,
        test={"id": "SR-API-UNIT-002", "type": "api.http", "request": "x", "assert": []},
    )
    from spec_runner.harnesses.api_http import run

    with pytest.raises(TypeError, match="requires request mapping"):
        run(case, ctx=SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys))


def test_api_http_requires_url(tmp_path, monkeypatch, capsys):
    doc = tmp_path / "case.spec.md"
    doc.write_text("# case\n", encoding="utf-8")
    case = SpecDocTest(
        doc_path=doc,
        test={
            "id": "SR-API-UNIT-003",
            "type": "api.http",
            "request": {"method": "GET"},
            "assert": [],
        },
    )
    from spec_runner.harnesses.api_http import run

    with pytest.raises(ValueError, match="request.url is required"):
        run(case, ctx=SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys))


def test_api_http_rejects_relative_escape(tmp_path, monkeypatch, capsys):
    repo = tmp_path / "repo"
    (repo / ".git").mkdir(parents=True)
    doc = repo / "docs" / "spec" / "case.spec.md"
    doc.parent.mkdir(parents=True)
    doc.write_text("# case\n", encoding="utf-8")
    outside = tmp_path / "outside.txt"
    outside.write_text("x", encoding="utf-8")
    case = SpecDocTest(
        doc_path=doc,
        test={
            "id": "SR-API-UNIT-004",
            "type": "api.http",
            "request": {"method": "GET", "url": "../../../outside.txt"},
            "assert": [],
        },
    )
    from spec_runner.harnesses.api_http import run

    with pytest.raises(ValueError, match="escapes contract root"):
        run(case, ctx=SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys))


def test_api_http_body_json_expr_operator(tmp_path, monkeypatch, capsys):
    fixture = tmp_path / "fixtures" / "ok.json"
    fixture.parent.mkdir(parents=True)
    fixture.write_text('{"ok": true, "items": [1, 2]}', encoding="utf-8")
    doc = tmp_path / "case.spec.md"
    doc.write_text("# case\n", encoding="utf-8")
    case = SpecDocTest(
        doc_path=doc,
        test={
            "id": "SR-API-UNIT-EXPR-001",
            "type": "api.http",
            "request": {
                "method": "GET",
                "url": "/fixtures/ok.json",
            },
            "assert": [
                {
                    "target": "body_json",
                    "must": [
                        {
                            "evaluate": [
                                {
                                    "and": [
                                        {"has_key": ["ok"]},
                                        {"eq": [{"get": [{"var": "subject"}, "ok"]}, True]},
                                    ]
                                }
                            ]
                        }
                    ],
                }
            ],
        },
    )
    from spec_runner.harnesses.api_http import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys))


def test_api_http_oauth_missing_env_is_schema_error(tmp_path, monkeypatch, capsys):
    fixture = tmp_path / "fixtures" / "ok.json"
    fixture.parent.mkdir(parents=True)
    fixture.write_text('{"ok": true}', encoding="utf-8")
    token = tmp_path / "fixtures" / "token.json"
    token.write_text('{"access_token":"stub","expires_in":3600}', encoding="utf-8")
    doc = tmp_path / "case.spec.md"
    doc.write_text("# case\n", encoding="utf-8")
    case = SpecDocTest(
        doc_path=doc,
        test={
            "id": "SR-API-UNIT-OAUTH-001",
            "type": "api.http",
            "harness": {
                "api_http": {
                    "auth": {
                        "oauth": {
                            "grant_type": "client_credentials",
                            "token_url": "/fixtures/token.json",
                            "client_id_env": "SPEC_RUNNER_MISSING_CLIENT_ID",
                            "client_secret_env": "SPEC_RUNNER_MISSING_CLIENT_SECRET",
                        }
                    }
                }
            },
            "request": {"method": "GET", "url": "/fixtures/ok.json"},
            "assert": [],
        },
    )
    from spec_runner.harnesses.api_http import run

    with pytest.raises(ValueError, match="oauth env var is required"):
        run(case, ctx=SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys))


def test_api_http_oauth_invalid_auth_style_is_schema_error(tmp_path, monkeypatch, capsys):
    fixture = tmp_path / "fixtures" / "ok.json"
    fixture.parent.mkdir(parents=True)
    fixture.write_text('{"ok": true}', encoding="utf-8")
    token = tmp_path / "fixtures" / "token.json"
    token.write_text('{"access_token":"stub","expires_in":3600}', encoding="utf-8")
    doc = tmp_path / "case.spec.md"
    doc.write_text("# case\n", encoding="utf-8")
    case = SpecDocTest(
        doc_path=doc,
        test={
            "id": "SR-API-UNIT-OAUTH-002",
            "type": "api.http",
            "harness": {
                "api_http": {
                    "auth": {
                        "oauth": {
                            "grant_type": "client_credentials",
                            "token_url": "/fixtures/token.json",
                            "client_id_env": "PATH",
                            "client_secret_env": "HOME",
                            "auth_style": "token",
                        }
                    }
                }
            },
            "request": {"method": "GET", "url": "/fixtures/ok.json"},
            "assert": [],
        },
    )
    from spec_runner.harnesses.api_http import run

    with pytest.raises(ValueError, match="auth_style"):
        run(case, ctx=SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys))


def test_api_http_oauth_live_fetch_and_context_metadata(tmp_path, monkeypatch, capsys):
    doc = tmp_path / "case.spec.md"
    doc.write_text("# case\n", encoding="utf-8")
    monkeypatch.setenv("TEST_OAUTH_CLIENT_ID", "cid")
    monkeypatch.setenv("TEST_OAUTH_CLIENT_SECRET", "secret")

    class _Resp:
        def __init__(self, body: str, *, status: int = 200, headers: dict[str, str] | None = None):
            self._body = body.encode("utf-8")
            self.status = status
            self.headers = headers or {}

        def read(self):
            return self._body

        def getcode(self):
            return self.status

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

    def _fake_urlopen(req, timeout=0):  # noqa: ARG001
        url = req.full_url
        if "issuer.example.invalid" in url:
            return _Resp('{"access_token":"token-123","expires_in":3600}')
        assert req.headers.get("Authorization") == "Bearer token-123"
        return _Resp('{"ok": true}')

    monkeypatch.setattr("urllib.request.urlopen", _fake_urlopen)

    case = SpecDocTest(
        doc_path=doc,
        test={
            "id": "SR-API-UNIT-OAUTH-003",
            "type": "api.http",
            "harness": {
                "api_http": {
                    "mode": "live",
                    "auth": {
                        "oauth": {
                            "grant_type": "client_credentials",
                            "token_url": "https://issuer.example.invalid/oauth/token",
                            "client_id_env": "TEST_OAUTH_CLIENT_ID",
                            "client_secret_env": "TEST_OAUTH_CLIENT_SECRET",
                            "scope": "read:items",
                        }
                    },
                }
            },
            "request": {"method": "GET", "url": "https://api.example.invalid/items"},
            "assert": [
                {
                    "target": "context_json",
                    "must": [
                        {
                            "evaluate": [
                                {
                                    "eq": [
                                        {"get": [{"get": [{"var": "subject"}, "meta"]}, "auth_mode"]},
                                        "oauth",
                                    ]
                                }
                            ]
                        }
                    ],
                }
            ],
        },
    )
    from spec_runner.harnesses.api_http import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys))


def test_api_http_oauth_token_cache_reuse_and_header_override(tmp_path, monkeypatch, capsys):
    doc = tmp_path / "case.spec.md"
    doc.write_text("# case\n", encoding="utf-8")
    monkeypatch.setenv("TEST_OAUTH_CLIENT_ID", "cid")
    monkeypatch.setenv("TEST_OAUTH_CLIENT_SECRET", "secret")
    token_calls = {"count": 0}
    api_calls = {"count": 0}

    class _Resp:
        def __init__(self, body: str, *, status: int = 200, headers: dict[str, str] | None = None):
            self._body = body.encode("utf-8")
            self.status = status
            self.headers = headers or {}

        def read(self):
            return self._body

        def getcode(self):
            return self.status

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

    def _fake_urlopen(req, timeout=0):  # noqa: ARG001
        url = req.full_url
        if "issuer.example.invalid" in url:
            token_calls["count"] += 1
            return _Resp('{"access_token":"token-123","expires_in":3600}')
        api_calls["count"] += 1
        assert req.headers.get("Authorization") == "Bearer explicit-token"
        return _Resp('{"ok": true}')

    monkeypatch.setattr("urllib.request.urlopen", _fake_urlopen)

    from spec_runner.harnesses import api_http as api_http_mod
    from spec_runner.harnesses.api_http import run

    api_http_mod._OAUTH_TOKEN_CACHE.clear()
    case = SpecDocTest(
        doc_path=doc,
        test={
            "id": "SR-API-UNIT-OAUTH-004",
            "type": "api.http",
            "harness": {
                "api_http": {
                    "mode": "live",
                    "auth": {
                        "oauth": {
                            "grant_type": "client_credentials",
                            "token_url": "https://issuer.example.invalid/oauth/token",
                            "client_id_env": "TEST_OAUTH_CLIENT_ID",
                            "client_secret_env": "TEST_OAUTH_CLIENT_SECRET",
                        }
                    },
                }
            },
            "request": {
                "method": "GET",
                "url": "https://api.example.invalid/items",
                "headers": {"Authorization": "Bearer explicit-token"},
            },
            "assert": [],
        },
    )

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys))
    run(case, ctx=SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys))
    assert token_calls["count"] == 1
    assert api_calls["count"] == 2


def test_api_http_rejects_unsupported_method(tmp_path, monkeypatch, capsys):
    doc = tmp_path / "case.spec.md"
    doc.write_text("# case\n", encoding="utf-8")
    case = SpecDocTest(
        doc_path=doc,
        test={
            "id": "SR-API-UNIT-METHOD-001",
            "type": "api.http",
            "request": {"method": "TRACE", "url": "/missing.json"},
            "assert": [],
        },
    )
    from spec_runner.harnesses.api_http import run

    with pytest.raises(ValueError, match="request.method must be one of"):
        run(case, ctx=SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys))


def test_api_http_query_merge_and_cors_projection(tmp_path, monkeypatch, capsys):
    doc = tmp_path / "case.spec.md"
    doc.write_text("# case\n", encoding="utf-8")
    seen_urls: list[str] = []
    seen_headers: dict[str, str] = {}

    class _Resp:
        def __init__(self, body: str, *, status: int = 200, headers: dict[str, str] | None = None):
            self._body = body.encode("utf-8")
            self.status = status
            self.headers = headers or {}

        def read(self):
            return self._body

        def getcode(self):
            return self.status

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

    def _fake_urlopen(req, timeout=0):  # noqa: ARG001
        seen_urls.append(req.full_url)
        seen_headers.update(req.headers)
        return _Resp(
            '{"ok": true}',
            headers={
                "Access-Control-Allow-Origin": "https://client.example",
                "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
                "Access-Control-Allow-Headers": "authorization, content-type",
                "Access-Control-Allow-Credentials": "true",
                "Access-Control-Max-Age": "600",
                "Vary": "Origin, Accept-Encoding",
            },
        )

    monkeypatch.setattr("urllib.request.urlopen", _fake_urlopen)

    case = SpecDocTest(
        doc_path=doc,
        test={
            "id": "SR-API-UNIT-CORS-001",
            "type": "api.http",
            "harness": {"api_http": {"mode": "live"}},
            "request": {
                "method": "OPTIONS",
                "url": "https://api.example.invalid/items?existing=1",
                "query": {"page": 2, "limit": 10},
                "cors": {
                    "origin": "https://client.example",
                    "preflight": True,
                    "request_method": "POST",
                    "request_headers": ["authorization", "content-type"],
                },
            },
            "assert": [],
        },
    )
    from spec_runner.harnesses.api_http import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys))
    assert seen_urls
    assert "existing=1" in seen_urls[0]
    assert "page=2" in seen_urls[0]
    assert "limit=10" in seen_urls[0]
    assert seen_headers.get("Origin") == "https://client.example"
    assert seen_headers.get("Access-control-request-method") == "POST"


def test_api_http_scenario_round_trip_templating(tmp_path, monkeypatch, capsys):
    doc = tmp_path / "case.spec.md"
    doc.write_text("# case\n", encoding="utf-8")
    seen_urls: list[str] = []
    seen_methods: list[str] = []

    class _Resp:
        def __init__(self, body: str, *, status: int = 200, headers: dict[str, str] | None = None):
            self._body = body.encode("utf-8")
            self.status = status
            self.headers = headers or {}

        def read(self):
            return self._body

        def getcode(self):
            return self.status

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

    def _fake_urlopen(req, timeout=0):  # noqa: ARG001
        url = req.full_url
        method = str(req.get_method()).upper()
        seen_urls.append(url)
        seen_methods.append(method)
        if method == "POST":
            return _Resp('{"id":"abc-123"}', status=201)
        if method == "GET":
            return _Resp('{"id":"abc-123","ok":true}', status=200)
        if method == "DELETE":
            return _Resp('{"deleted":true}', status=204)
        raise AssertionError(f"unexpected request {method} {url}")

    monkeypatch.setattr("urllib.request.urlopen", _fake_urlopen)

    case = SpecDocTest(
        doc_path=doc,
        test={
            "id": "SR-API-UNIT-SCENARIO-001",
            "type": "api.http",
            "harness": {
                "api_http": {
                    "mode": "live",
                    "scenario": {"fail_fast": True},
                }
            },
            "requests": [
                {"id": "create", "method": "POST", "url": "https://api.example.invalid/items"},
                {"id": "get", "method": "GET", "url": "https://api.example.invalid/items/{{steps.create.body_json.id}}"},
                {"id": "cleanup", "method": "DELETE", "url": "https://api.example.invalid/items/{{steps.get.body_json.id}}"},
            ],
            "assert": [
                {
                    "target": "status",
                    "must": [{"evaluate": [{"contains": [{"var": "subject"}, "204"]}]}],
                }
            ],
        },
    )
    from spec_runner.harnesses.api_http import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys))
    assert seen_methods == ["POST", "GET", "DELETE"]
    assert seen_urls[1].endswith("/abc-123")
    assert seen_urls[2].endswith("/abc-123")
