# SPEC-OPT-OUT: Exercises behavior not yet representable as stable .spec.md coverage (unit-level API/diagnostic/infrastructure checks).
from pathlib import Path

import pytest

from spec_runner.dispatcher import SpecRunContext, run_case
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
