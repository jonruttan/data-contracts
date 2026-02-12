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
            "assert": [{"target": "text", "must": [{"contain": ["hello"]}]}],
        },
    )

    from spec_runner.harnesses.text_file import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_text_file_cannot_group(tmp_path, monkeypatch, capsys):
    p = tmp_path / "doc.md"
    p.write_text("hello world\n", encoding="utf-8")

    case = SpecDocTest(
        doc_path=p,
        test={
            "id": "X",
            "type": "text.file",
            "assert": [{"target": "text", "cannot": [{"contain": ["ERROR:"]}]}],
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
            "assert": [{"target": "text", "must": [{"contain": ["hello other"]}]}],
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
            "assert": [{"target": "text", "must": [{"contain": ["spec doc"]}]}],
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
            "assert": [{"target": "stdout", "must": [{"contain": ["hello"]}]}],
        },
    )

    from spec_runner.harnesses.text_file import run

    with pytest.raises(ValueError, match="unknown assert target"):
        run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_dispatcher_includes_text_file_kind():
    from spec_runner.dispatcher import default_type_runners

    runners = default_type_runners()
    assert "text.file" in runners


def test_text_file_rejects_path_escape_without_repo_root(tmp_path, monkeypatch, capsys):
    doc = tmp_path / "spec.md"
    doc.write_text("spec doc\n", encoding="utf-8")
    outside = tmp_path.parent / "outside.txt"
    outside.write_text("outside\n", encoding="utf-8")

    case = SpecDocTest(
        doc_path=doc,
        test={
            "id": "X",
            "type": "text.file",
            "path": "../outside.txt",
            "assert": [{"target": "text", "must": [{"contain": ["outside"]}]}],
        },
    )

    from spec_runner.harnesses.text_file import run

    with pytest.raises(ValueError, match="escapes contract root"):
        run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_text_file_allows_parent_reference_with_repo_root(tmp_path, monkeypatch, capsys):
    root = tmp_path / "repo"
    (root / ".git").mkdir(parents=True)
    doc_dir = root / "docs" / "spec"
    doc_dir.mkdir(parents=True)
    doc = doc_dir / "spec.md"
    doc.write_text("spec doc\n", encoding="utf-8")
    target = root / "docs" / "other.txt"
    target.write_text("hello other\n", encoding="utf-8")

    case = SpecDocTest(
        doc_path=doc,
        test={
            "id": "X",
            "type": "text.file",
            "path": "../other.txt",
            "assert": [{"target": "text", "must": [{"contain": ["hello other"]}]}],
        },
    )

    from spec_runner.harnesses.text_file import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))
