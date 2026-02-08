from pathlib import Path

import pytest

from spec_runner.dispatcher import SpecRunContext
from spec_runner.doc_parser import SpecDocTest


def test_text_file_contains(tmp_path, monkeypatch, capsys):
    p = tmp_path / "doc.md"
    p.write_text("hello world\n", encoding="utf-8")

    case = SpecDocTest(
        doc_path=p,
        test={
            "id": "X",
            "kind": "text.file",
            "assert": [{"target": "text", "contains": ["hello"]}],
        },
    )

    from spec_runner.harnesses.text_file import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_text_file_unknown_target(tmp_path, monkeypatch, capsys):
    p = tmp_path / "doc.md"
    p.write_text("hello\n", encoding="utf-8")

    case = SpecDocTest(
        doc_path=p,
        test={
            "id": "X",
            "kind": "text.file",
            "assert": [{"target": "stdout", "contains": ["hello"]}],
        },
    )

    from spec_runner.harnesses.text_file import run

    with pytest.raises(ValueError, match="unknown assert target"):
        run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_dispatcher_includes_text_file_kind():
    from spec_runner.dispatcher import default_kind_runners

    runners = default_kind_runners()
    assert "text.file" in runners

