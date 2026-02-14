# SPEC-OPT-OUT: Exercises docs-build script wiring and generated-artifact freshness checks.
from __future__ import annotations

import importlib.util
import json
from pathlib import Path


def _load_docs_build_module():
    repo_root = Path(__file__).resolve().parents[1]
    script_path = repo_root / "scripts/docs_build_reference.py"
    spec = importlib.util.spec_from_file_location("docs_build_reference_script", script_path)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _chapter(doc_id: str, own: str, req: str, ex_id: str) -> str:
    return f"""# Chapter

```yaml doc-meta
doc_id: {doc_id}
title: {doc_id}
status: active
audience: maintainer
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


def test_docs_build_writes_and_check_passes(tmp_path: Path) -> None:
    mod = _load_docs_build_module()
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
        assert mod.main(["--check"]) == 0
    finally:
        os.chdir(old)


def test_docs_build_check_detects_stale_generated_file(tmp_path: Path) -> None:
    mod = _load_docs_build_module()
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
        _write_text(tmp_path / "docs/book/reference_index.md", "# stale\n")
        assert mod.main(["--check"]) == 1
    finally:
        os.chdir(old)


def test_docs_build_graph_is_path_stable(tmp_path: Path) -> None:
    mod = _load_docs_build_module()
    _write_text(
        tmp_path / "docs/book/reference_manifest.yaml",
        """version: 1
chapters:
  - path: docs/book/a.md
    summary: A.
""",
    )
    _write_text(tmp_path / "docs/book/a.md", _chapter("DOC-REF-001", "tok.a", "tok.a", "EX-A-001"))
    old = Path.cwd()
    try:
        import os

        os.chdir(tmp_path)
        assert mod.main([]) == 0
        graph = json.loads((tmp_path / "docs/book/docs_graph.json").read_text(encoding="utf-8"))
        assert graph["root"] == "."
        assert str(tmp_path) not in json.dumps(graph, sort_keys=True)
    finally:
        os.chdir(old)
