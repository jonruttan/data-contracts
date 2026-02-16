# SPEC-OPT-OUT: Exercises behavior not yet representable as stable .spec.md coverage (unit-level API/diagnostic/infrastructure checks).
from pathlib import Path

import pytest

from spec_runner.dispatcher import SpecRunContext, default_type_runners, run_case
from spec_runner.doc_parser import SpecDocTest


def test_unknown_type_raises_clear_error(tmp_path, monkeypatch, capsys):
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={"id": "CK-CLI-999", "type": "unknown.type", "title": "Unknown type"},
    )

    with pytest.raises(RuntimeError, match=r"unknown spec-test type: unknown\.type"):
        run_case(
            case,
            ctx=SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys),
            type_runners={"cli.run": lambda *_a, **_k: None},
        )


def test_run_context_adapter_methods_require_explicit_fields(tmp_path, monkeypatch, capsys):
    ctx = SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys)
    with ctx.patch_context():
        pass
    got = ctx.read_capture()
    assert hasattr(got, "out")
    assert hasattr(got, "err")


def test_run_context_requires_patcher_and_capture(tmp_path):
    with pytest.raises(TypeError):
        SpecRunContext(tmp_path=tmp_path)  # type: ignore[call-arg]


def test_default_type_runners_include_api_http():
    runners = default_type_runners()
    assert "api.http" in runners


def test_run_case_rejects_recursive_chain_reentry(tmp_path, monkeypatch, capsys):
    (tmp_path / ".git").mkdir(parents=True)
    case_doc = tmp_path / "docs/spec/recur.spec.md"
    case_doc.parent.mkdir(parents=True, exist_ok=True)
    case_doc.write_text(
        """# Recursion

## CASE-RECUR

```yaml spec-test
id: CASE-RECUR
type: text.file
path: /README.md
harness:
  chain:
    steps:
    - id: self
      ref: "#CASE-RECUR"
assert: []
```
""",
        encoding="utf-8",
    )
    (tmp_path / "README.md").write_text("ok\n", encoding="utf-8")
    case = SpecDocTest(
        doc_path=case_doc,
        test={
            "id": "CASE-RECUR",
            "type": "text.file",
            "path": "/README.md",
            "harness": {"chain": {"steps": [{"id": "self", "ref": "#CASE-RECUR"}]}},
            "assert": [],
        },
    )
    with pytest.raises(RuntimeError, match="references current case recursively"):
        run_case(case, ctx=SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys))
