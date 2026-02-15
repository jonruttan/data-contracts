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
                "url": "fixtures/ok.json",
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
                "url": "fixtures/ok.json",
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
