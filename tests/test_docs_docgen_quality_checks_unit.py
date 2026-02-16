# SPEC-OPT-OUT: Exercises docs docgen governance check registrations and quality threshold wiring.
from __future__ import annotations

import importlib.util
from pathlib import Path


def _load_script_module():
    repo_root = Path(__file__).resolve().parents[1]
    script_path = repo_root / "scripts/run_governance_specs.py"
    spec = importlib.util.spec_from_file_location("run_governance_specs_script", script_path)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_docgen_quality_checks_registered() -> None:
    mod = _load_script_module()
    required = {
        "docs.stdlib_symbol_docs_complete",
        "docs.stdlib_examples_complete",
        "docs.harness_reference_semantics_complete",
        "docs.runner_reference_semantics_complete",
        "docs.reference_namespace_chapters_sync",
        "docs.docgen_quality_score_threshold",
    }
    assert required.issubset(set(mod._CHECKS.keys()))
