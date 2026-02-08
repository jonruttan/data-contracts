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
            "type": "text.file",
            "assert": [{"target": "text", "contains": ["hello"]}],
        },
    )

    from spec_runner.harnesses.text_file import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_text_file_can_read_relative_path(tmp_path, monkeypatch, capsys):
    doc = tmp_path / "spec.md"
    doc.write_text("spec doc\n", encoding="utf-8")
    target = tmp_path / "other.txt"
    target.write_text("hello other\n", encoding="utf-8")

    case = SpecDocTest(
        doc_path=doc,
        test={
            "id": "X",
            "type": "text.file",
            "path": "other.txt",
            "assert": [{"target": "text", "contains": ["hello other"]}],
        },
    )

    from spec_runner.harnesses.text_file import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_text_file_rejects_absolute_path(tmp_path, monkeypatch, capsys):
    doc = tmp_path / "spec.md"
    doc.write_text("spec doc\n", encoding="utf-8")

    case = SpecDocTest(
        doc_path=doc,
        test={
            "id": "X",
            "type": "text.file",
            "path": str(doc.resolve()),
            "assert": [{"target": "text", "contains": ["spec doc"]}],
        },
    )

    from spec_runner.harnesses.text_file import run

    with pytest.raises(ValueError, match="must be relative"):
        run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_text_file_unknown_target(tmp_path, monkeypatch, capsys):
    p = tmp_path / "doc.md"
    p.write_text("hello\n", encoding="utf-8")

    case = SpecDocTest(
        doc_path=p,
        test={
            "id": "X",
            "type": "text.file",
            "assert": [{"target": "stdout", "contains": ["hello"]}],
        },
    )

    from spec_runner.harnesses.text_file import run

    with pytest.raises(ValueError, match="unknown assert target"):
        run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_dispatcher_includes_text_file_kind():
    from spec_runner.dispatcher import default_type_runners

    runners = default_type_runners()
    assert "text.file" in runners
