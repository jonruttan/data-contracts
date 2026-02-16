# SPEC-OPT-OUT: Exercises chain execution graph behavior and dispatcher context wiring not yet representable as stable .spec.md coverage.
from pathlib import Path

import pytest

from spec_runner.compiler import compile_external_case
from spec_runner.components.chain_engine import compile_chain_plan, execute_chain_plan
from spec_runner.dispatcher import SpecRunContext


def _write_spec(path: Path, case_id: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        """# Fixtures\n\n## {case_id}\n\n```yaml spec-test\nid: {case_id}\ntype: text.file\npath: /README.md\nassert: []\n```\n""".format(case_id=case_id),
        encoding="utf-8",
    )


def test_compile_chain_plan_rejects_missing_ref_fields(tmp_path):
    (tmp_path / ".git").mkdir(parents=True)
    doc = tmp_path / "docs/spec/case.spec.md"
    doc.parent.mkdir(parents=True, exist_ok=True)
    raw = {
        "id": "CASE-A",
        "type": "text.file",
        "path": "/README.md",
        "harness": {
            "chain": {
                "steps": [
                    {
                        "id": "s1",
                        "ref": {},
                    }
                ]
            }
        },
        "assert": [],
    }
    case = compile_external_case(raw, doc_path=doc)
    with pytest.raises(ValueError, match="requires path and/or case_id"):
        compile_chain_plan(case)


def test_compile_chain_plan_rejects_non_bool_flags(tmp_path):
    (tmp_path / ".git").mkdir(parents=True)
    doc = tmp_path / "docs/spec/case.spec.md"
    doc.parent.mkdir(parents=True, exist_ok=True)
    raw = {
        "id": "CASE-A",
        "type": "text.file",
        "path": "/README.md",
        "harness": {
            "chain": {
                "fail_fast": "yes",
                "steps": [
                    {
                        "id": "s1",
                        "ref": {"case_id": "CASE-B"},
                        "allow_continue": "no",
                    }
                ],
            }
        },
        "assert": [],
    }
    case = compile_external_case(raw, doc_path=doc)
    with pytest.raises(TypeError, match="allow_continue must be a bool"):
        compile_chain_plan(case)


def test_execute_chain_plan_resolves_path_case_and_exports(tmp_path, monkeypatch, capsys):
    (tmp_path / ".git").mkdir(parents=True)
    (tmp_path / "README.md").write_text("ok\n", encoding="utf-8")

    dep_doc = tmp_path / "docs/spec/dep.spec.md"
    _write_spec(dep_doc, "CASE-DEP-1")

    host_doc = tmp_path / "docs/spec/host.spec.md"
    host_doc.parent.mkdir(parents=True, exist_ok=True)
    host = compile_external_case(
        {
            "id": "CASE-HOST",
            "type": "text.file",
            "path": "/README.md",
            "harness": {
                "chain": {
                    "steps": [
                        {
                            "id": "preload",
                            "ref": {
                                "path": "/docs/spec/dep.spec.md",
                                "case_id": "CASE-DEP-1",
                            },
                            "exports": {
                                "dep_id": {
                                    "from_target": "body_json",
                                    "path": "id",
                                }
                            },
                        }
                    ]
                }
            },
            "assert": [],
        },
        doc_path=host_doc,
    )

    ctx = SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys)

    def _run_case(ref_case):
        case_key = f"{ref_case.doc_path.resolve().as_posix()}::{ref_case.id}"
        ctx.set_case_targets(case_key=case_key, targets={"body_json": {"id": "abc-123"}})

    execute_chain_plan(host, ctx=ctx, run_case_fn=_run_case)
    assert ctx.chain_state["preload"]["dep_id"] == "abc-123"
    assert len(ctx.chain_trace) == 1
    assert ctx.chain_trace[0]["status"] == "pass"


def test_execute_chain_plan_local_case_id_resolution(tmp_path, monkeypatch, capsys):
    (tmp_path / ".git").mkdir(parents=True)
    (tmp_path / "README.md").write_text("ok\n", encoding="utf-8")

    doc = tmp_path / "docs/spec/mixed.spec.md"
    doc.parent.mkdir(parents=True, exist_ok=True)
    doc.write_text(
        """# Mixed\n\n## CASE-ONE\n\n```yaml spec-test\nid: CASE-ONE\ntype: text.file\npath: /README.md\nassert: []\n```\n\n## CASE-TWO\n\n```yaml spec-test\nid: CASE-TWO\ntype: text.file\npath: /README.md\nharness:\n  chain:\n    steps:\n    - id: local\n      ref:\n        case_id: CASE-ONE\nassert: []\n```\n""",
        encoding="utf-8",
    )

    case_two = compile_external_case(
        {
            "id": "CASE-TWO",
            "type": "text.file",
            "path": "/README.md",
            "harness": {"chain": {"steps": [{"id": "local", "ref": {"case_id": "CASE-ONE"}}]}},
            "assert": [],
        },
        doc_path=doc,
    )

    ctx = SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys)
    seen: list[str] = []

    def _run_case(ref_case):
        seen.append(ref_case.id)

    execute_chain_plan(case_two, ctx=ctx, run_case_fn=_run_case)
    assert seen == ["CASE-ONE"]
