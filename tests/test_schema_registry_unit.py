# SPEC-OPT-OUT: Validates schema registry compiler internals and artifact-level determinism not yet represented as stable .spec.md fixtures.
from __future__ import annotations

from pathlib import Path

from spec_runner.schema_registry import compile_registry


def test_compile_registry_has_core_fields_and_type_profiles() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    compiled, errs = compile_registry(repo_root)
    assert errs == []
    assert compiled is not None
    top = compiled.get("top_level_fields") or {}
    types = compiled.get("type_profiles") or {}
    assert "id" in top
    assert "type" in top
    assert "harness" in top
    assert "cli.run" in types
    assert "text.file" in types
    assert "governance.check" in types
    assert "spec_lang.export" in types
