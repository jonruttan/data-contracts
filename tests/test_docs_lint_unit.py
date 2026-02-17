# SPEC-OPT-OUT: Exercises docs-lint command wiring and metadata edge-cases not yet represented as stable .spec.md fixtures.
from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

from spec_runner import spec_lang_commands


def _load_docs_lint_module() -> SimpleNamespace:
    return SimpleNamespace(main=spec_lang_commands.docs_lint_main)


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _chapter(doc_id: str, own: str, req: str, ex_id: str) -> str:
    return f"""# Chapter

```yaml doc-meta
doc_id: {doc_id}
title: {doc_id}
status: active
audience: author
owns_tokens: ["{own}"]
requires_tokens: ["{req}"]
commands:
  - run: "./scripts/ci_gate.sh"
    purpose: run gate
examples:
  - id: {ex_id}
    runnable: true
sections_required:
  - "## Purpose"
  - "## Inputs"
  - "## Outputs"
  - "## Failure Modes"
```

## Purpose
x
## Inputs
x
## Outputs
x
## Failure Modes
x
"""


def test_docs_lint_passes_with_valid_manifest_and_meta(tmp_path: Path) -> None:
    mod = _load_docs_lint_module()
    _write_text(
        tmp_path / "docs/book/reference_manifest.yaml",
        """version: 1
chapters:
  - path: docs/book/a.md
    summary: A.
  - path: docs/book/b.md
    summary: B.
""",
    )
    _write_text(tmp_path / "docs/book/a.md", _chapter("DOC-REF-001", "tok.a", "tok.b", "EX-A-001"))
    _write_text(tmp_path / "docs/book/b.md", _chapter("DOC-REF-002", "tok.b", "tok.a", "EX-B-001"))
    old = Path.cwd()
    try:
        import os

        os.chdir(tmp_path)
        assert mod.main([]) == 0
    finally:
        os.chdir(old)


def test_docs_lint_fails_on_duplicate_token_owner(tmp_path: Path) -> None:
    mod = _load_docs_lint_module()
    _write_text(
        tmp_path / "docs/book/reference_manifest.yaml",
        """version: 1
chapters:
  - path: docs/book/a.md
    summary: A.
  - path: docs/book/b.md
    summary: B.
""",
    )
    _write_text(tmp_path / "docs/book/a.md", _chapter("DOC-REF-001", "tok.a", "tok.b", "EX-A-001"))
    _write_text(tmp_path / "docs/book/b.md", _chapter("DOC-REF-002", "tok.a", "tok.a", "EX-B-001"))
    old = Path.cwd()
    try:
        import os

        os.chdir(tmp_path)
        assert mod.main([]) == 1
    finally:
        os.chdir(old)


def test_docs_lint_fails_on_unresolved_required_token(tmp_path: Path) -> None:
    mod = _load_docs_lint_module()
    _write_text(
        tmp_path / "docs/book/reference_manifest.yaml",
        """version: 1
chapters:
  - path: docs/book/a.md
    summary: A.
""",
    )
    _write_text(tmp_path / "docs/book/a.md", _chapter("DOC-REF-001", "tok.a", "tok.missing", "EX-A-001"))
    old = Path.cwd()
    try:
        import os

        os.chdir(tmp_path)
        assert mod.main([]) == 1
    finally:
        os.chdir(old)


def test_docs_lint_fails_on_duplicate_example_id(tmp_path: Path) -> None:
    mod = _load_docs_lint_module()
    _write_text(
        tmp_path / "docs/book/reference_manifest.yaml",
        """version: 1
chapters:
  - path: docs/book/a.md
    summary: A.
  - path: docs/book/b.md
    summary: B.
""",
    )
    _write_text(tmp_path / "docs/book/a.md", _chapter("DOC-REF-001", "tok.a", "tok.b", "EX-SHARED-001"))
    _write_text(tmp_path / "docs/book/b.md", _chapter("DOC-REF-002", "tok.b", "tok.a", "EX-SHARED-001"))
    old = Path.cwd()
    try:
        import os

        os.chdir(tmp_path)
        assert mod.main([]) == 1
    finally:
        os.chdir(old)
