# SPEC-OPT-OUT: Exercises chain execution graph behavior and dispatcher context wiring not yet representable as stable .spec.md coverage.
from pathlib import Path

import pytest

from spec_runner.compiler import compile_external_case
from spec_runner.components.chain_engine import compile_chain_plan, execute_chain_plan
from spec_runner.dispatcher import SpecRunContext


def _write_spec(path: Path, case_id: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        """# Fixtures\n\n## {case_id}\n\n```yaml contract-spec\nid: {case_id}\ntype: text.file\npath: /README.md\nharness:\n  exports:\n  - as: dep_id\n    from: assert.function\n    path: exported_step\n    params: [subject]\ncontract:\n- id: exported_step\n  class: must\n  target: body_json\n  asserts:\n  - std.object.get:\n    - {{var: subject}}\n    - id\n```\n""".format(case_id=case_id),
        encoding="utf-8",
    )


def test_compile_chain_plan_rejects_empty_ref(tmp_path):
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
                        "class": "must",
                        "ref": "",
                    }
                ]
            }
        },
        "contract": [],
    }
    case = compile_external_case(raw, doc_path=doc)
    with pytest.raises(ValueError, match="must be a non-empty string"):
        compile_chain_plan(case)


def test_compile_chain_plan_rejects_legacy_ref_mapping(tmp_path):
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
                        "class": "must",
                        "ref": {"case_id": "CASE-B"},
                    }
                ]
            }
        },
        "contract": [],
    }
    case = compile_external_case(raw, doc_path=doc)
    with pytest.raises(TypeError, match="legacy mapping format"):
        compile_chain_plan(case)


def test_compile_chain_plan_rejects_empty_fragment_and_invalid_case_id(tmp_path):
    (tmp_path / ".git").mkdir(parents=True)
    doc = tmp_path / "docs/spec/case.spec.md"
    doc.parent.mkdir(parents=True, exist_ok=True)

    base = {
        "id": "CASE-A",
        "type": "text.file",
        "path": "/README.md",
        "contract": [],
    }

    case_empty = compile_external_case(
        {
            **base,
            "harness": {"chain": {"steps": [{"id": "s1", "class": "must", "ref": "/docs/spec/a.spec.md#"}]}},
        },
        doc_path=doc,
    )
    with pytest.raises(ValueError, match="must be non-empty"):
        compile_chain_plan(case_empty)

    case_invalid = compile_external_case(
        {
            **base,
            "harness": {"chain": {"steps": [{"id": "s1", "class": "must", "ref": "/docs/spec/a.spec.md#BAD CASE"}]}},
        },
        doc_path=doc,
    )
    with pytest.raises(ValueError, match="must match"):
        compile_chain_plan(case_invalid)


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
                        "class": "must",
                        "ref": "#CASE-B",
                        "allow_continue": False,
                    }
                ],
            }
        },
        "contract": [],
    }
    case = compile_external_case(raw, doc_path=doc)
    with pytest.raises(TypeError, match="fail_fast must be a bool"):
        compile_chain_plan(case)

    raw["harness"]["chain"]["fail_fast"] = True
    raw["harness"]["chain"]["steps"][0]["allow_continue"] = "no"
    case = compile_external_case(raw, doc_path=doc)
    with pytest.raises(TypeError, match="allow_continue must be a bool"):
        compile_chain_plan(case)


def test_compile_chain_plan_requires_step_class(tmp_path):
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
                        "ref": "#CASE-B",
                    }
                ],
            }
        },
        "contract": [],
    }
    case = compile_external_case(raw, doc_path=doc)
    with pytest.raises(ValueError, match="class must be one of"):
        compile_chain_plan(case)


def test_execute_chain_plan_resolves_path_case_and_imports(tmp_path, monkeypatch, capsys):
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
                            "class": "must",
                            "ref": "/docs/spec/dep.spec.md#CASE-DEP-1",
                        }
                    ],
                    "imports": [{"from": "preload", "names": ["dep_id"]}],
                }
            },
            "contract": [],
        },
        doc_path=host_doc,
    )

    ctx = SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys)

    def _run_case(ref_case):
        case_key = f"{ref_case.doc_path.resolve().as_posix()}::{ref_case.id}"
        ctx.set_case_targets(case_key=case_key, targets={"body_json": {"id": "abc-123"}})

    execute_chain_plan(host, ctx=ctx, run_case_fn=_run_case)
    assert "dep_id" in ctx.chain_state["preload"]
    assert len(ctx.chain_trace) == 1
    assert ctx.chain_trace[0]["status"] == "pass"


def test_execute_chain_plan_hash_only_local_case_id_resolution(tmp_path, monkeypatch, capsys):
    (tmp_path / ".git").mkdir(parents=True)
    (tmp_path / "README.md").write_text("ok\n", encoding="utf-8")

    doc = tmp_path / "docs/spec/mixed.spec.md"
    doc.parent.mkdir(parents=True, exist_ok=True)
    doc.write_text(
        """# Mixed\n\n## CASE-ONE\n\n```yaml contract-spec\nid: CASE-ONE\ntype: text.file\npath: /README.md\ncontract: []\n```\n\n## CASE-TWO\n\n```yaml contract-spec\nid: CASE-TWO\ntype: text.file\npath: /README.md\nharness:\n  chain:\n    steps:\n    - id: local\n      class: must\n      ref: "#CASE-ONE"\ncontract: []\n```\n""",
        encoding="utf-8",
    )

    case_two = compile_external_case(
        {
            "id": "CASE-TWO",
            "type": "text.file",
            "path": "/README.md",
            "harness": {"chain": {"steps": [{"id": "local", "class": "must", "ref": "#CASE-ONE"}]}},
            "contract": [],
        },
        doc_path=doc,
    )

    ctx = SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys)
    seen: list[str] = []

    def _run_case(ref_case):
        seen.append(ref_case.id)

    execute_chain_plan(case_two, ctx=ctx, run_case_fn=_run_case)
    assert seen == ["CASE-ONE"]


def test_parse_scalar_ref_supports_relative_and_path_only(tmp_path, monkeypatch, capsys):
    (tmp_path / ".git").mkdir(parents=True)
    (tmp_path / "README.md").write_text("ok\n", encoding="utf-8")
    dep_doc = tmp_path / "docs/spec/fixtures/dep.spec.md"
    _write_spec(dep_doc, "CASE-DEP-2")

    host_doc = tmp_path / "docs/spec/host/case.spec.md"
    host_doc.parent.mkdir(parents=True, exist_ok=True)
    case = compile_external_case(
        {
            "id": "CASE-HOST-REL",
            "type": "text.file",
            "path": "/README.md",
            "harness": {
                "chain": {
                    "steps": [
                        {"id": "run_all", "class": "must", "ref": "../fixtures/dep.spec.md"},
                        {"id": "single", "class": "must", "ref": "../fixtures/dep.spec.md#CASE-DEP-2"},
                    ]
                }
            },
            "contract": [],
        },
        doc_path=host_doc,
    )
    seen: list[str] = []
    ctx = SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys)

    def _run_case(ref_case):
        seen.append(ref_case.id)

    execute_chain_plan(case, ctx=ctx, run_case_fn=_run_case)
    assert seen == ["CASE-DEP-2", "CASE-DEP-2"]


def test_execute_chain_plan_resolves_import_aliases(tmp_path, monkeypatch, capsys):
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
                            "class": "must",
                            "ref": "/docs/spec/dep.spec.md#CASE-DEP-1",
                        }
                    ],
                    "imports": [
                        {
                            "from": "preload",
                            "names": ["dep_id"],
                            "as": {"dep_id": "seed_id"},
                        }
                    ],
                }
            },
            "contract": [],
        },
        doc_path=host_doc,
    )

    ctx = SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys)

    def _run_case(ref_case):
        case_key = f"{ref_case.doc_path.resolve().as_posix()}::{ref_case.id}"
        ctx.set_case_targets(case_key=case_key, targets={"body_json": {"id": "abc-123"}})

    execute_chain_plan(host, ctx=ctx, run_case_fn=_run_case)
    host_key = f"{host.doc_path.resolve().as_posix()}::{host.id}"
    imports = dict(ctx.get_case_chain_imports(case_key=host_key))
    assert "seed_id" in imports


def test_compile_chain_plan_accepts_assert_function_imports(tmp_path):
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
                        "id": "lib",
                        "class": "must",
                        "ref": "/docs/spec/libraries/domain/http_core.spec.md#SRLIB-DOMAIN-HTTP-STATUS-IS",
                    }
                ],
                "imports": [{"from": "lib", "names": ["domain.http.status_is"]}],
            }
        },
        "contract": [],
    }
    case = compile_external_case(raw, doc_path=doc)
    steps, imports, _fail_fast = compile_chain_plan(case)
    assert steps[0].id == "lib"
    assert imports[0].from_id == "lib"


def test_compile_chain_plan_rejects_step_symbol_declarations(tmp_path):
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
                        "id": "lib",
                        "class": "must",
                        "ref": "/docs/spec/dep.spec.md#CASE-DEP-1",
                        "imports": [{"as": "dep_id", "from": "assert.function", "path": "x"}],
                    }
                ]
            }
        },
        "contract": [],
    }
    case = compile_external_case(raw, doc_path=doc)
    with pytest.raises(ValueError, match="steps\\[0\\]\\.imports is forbidden"):
        compile_chain_plan(case)
