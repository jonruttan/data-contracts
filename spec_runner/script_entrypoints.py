from __future__ import annotations

import importlib.util
import sys
from functools import lru_cache
from pathlib import Path
from types import ModuleType

from spec_runner.normalize_repo_runtime import main as _normalize_repo_main
from spec_runner.script_runtime_commands import (
    check_docs_freshness_main as _check_docs_freshness_main,
    ci_gate_summary_main as _ci_gate_summary_main,
    compare_conformance_parity_main as _compare_conformance_parity_main,
)
from spec_runner.script_runtime_commands import docs_generate_all_main as _docs_generate_all_main
from spec_runner.script_runtime_commands import perf_smoke_main as _perf_smoke_main


@lru_cache(maxsize=None)
def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


@lru_cache(maxsize=None)
def _load_script_module(script_relpath: str) -> ModuleType:
    script_path = _repo_root() / script_relpath
    if not script_path.exists():
        raise FileNotFoundError(f"script not found: {script_relpath}")
    module_name = f"spec_runner_script_{script_relpath.replace('/', '_').replace('.', '_')}"
    spec = importlib.util.spec_from_file_location(module_name, script_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"failed to load script module: {script_relpath}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _run_script_main(script_relpath: str, argv: list[str] | None = None) -> int:
    module = _load_script_module(script_relpath)
    entry = getattr(module, "main", None)
    if not callable(entry):
        raise RuntimeError(f"script missing callable main(argv): {script_relpath}")
    return int(entry(argv))


def ci_gate_summary_main(argv: list[str] | None = None) -> int:
    return int(_ci_gate_summary_main(argv))


def check_docs_freshness_main(argv: list[str] | None = None) -> int:
    return int(_check_docs_freshness_main(argv))


def compare_conformance_parity_main(argv: list[str] | None = None) -> int:
    return int(_compare_conformance_parity_main(argv))


def conformance_purpose_report_main(argv: list[str] | None = None) -> int:
    return _run_script_main("scripts/conformance_purpose_report.py", argv)


def docs_generate_all_main(argv: list[str] | None = None) -> int:
    return int(_docs_generate_all_main(argv))


def docs_generate_specs_main(argv: list[str] | None = None) -> int:
    return _run_script_main("scripts/docs_generate_specs.py", argv)


def docs_build_reference_main(argv: list[str] | None = None) -> int:
    return _run_script_main("scripts/docs_build_reference.py", argv)


def evaluate_style_main(argv: list[str] | None = None) -> int:
    return _run_script_main("scripts/evaluate_style.py", argv)


def impl_evaluate_migration_report_main(argv: list[str] | None = None) -> int:
    return _run_script_main("scripts/report_impl_evaluate_migration.py", argv)


def normalize_docs_layout_main(argv: list[str] | None = None) -> int:
    return _run_script_main("scripts/normalize_docs_layout.py", argv)


def normalize_repo_main(argv: list[str] | None = None) -> int:
    return int(_normalize_repo_main(argv))


def objective_scorecard_report_main(argv: list[str] | None = None) -> int:
    return _run_script_main("scripts/objective_scorecard_report.py", argv)


def python_conformance_runner_main(argv: list[str] | None = None) -> int:
    return _run_script_main("scripts/python/conformance_runner.py", argv)


def quality_metric_reports_main(argv: list[str] | None = None) -> int:
    forwarded = list(argv or [])
    if not forwarded:
        raise SystemExit(
            "quality_metric_reports_main requires first argument: "
            "spec-lang-adoption|runner-independence|python-dependency|docs-operability|contract-assertions"
        )
    report = str(forwarded.pop(0)).strip()
    report_to_script = {
        "spec-lang-adoption": "scripts/spec_lang_adoption_report.py",
        "runner-independence": "scripts/runner_independence_report.py",
        "python-dependency": "scripts/python_dependency_report.py",
        "docs-operability": "scripts/docs_operability_report.py",
        "contract-assertions": "scripts/contract_assertions_report.py",
    }
    script = report_to_script.get(report)
    if not script:
        print(f"unsupported quality report: {report}", file=sys.stderr)
        return 1
    return _run_script_main(script, forwarded)


def schema_registry_scripts_main(argv: list[str] | None = None) -> int:
    return _run_script_main("scripts/generate_schema_docs.py", argv)


def spec_portability_report_main(argv: list[str] | None = None) -> int:
    return _run_script_main("scripts/spec_portability_report.py", argv)


def split_library_cases_per_symbol_main(argv: list[str] | None = None) -> int:
    return _run_script_main("scripts/split_library_cases_per_symbol.py", argv)


def generate_governance_check_catalog_main(argv: list[str] | None = None) -> int:
    return _run_script_main("scripts/generate_governance_check_catalog.py", argv)


def generate_harness_type_catalog_main(argv: list[str] | None = None) -> int:
    return _run_script_main("scripts/generate_harness_type_catalog.py", argv)


def generate_metrics_field_catalog_main(argv: list[str] | None = None) -> int:
    return _run_script_main("scripts/generate_metrics_field_catalog.py", argv)


def generate_policy_rule_catalog_main(argv: list[str] | None = None) -> int:
    return _run_script_main("scripts/generate_policy_rule_catalog.py", argv)


def generate_runner_api_catalog_main(argv: list[str] | None = None) -> int:
    return _run_script_main("scripts/generate_runner_api_catalog.py", argv)


def generate_spec_lang_builtin_catalog_main(argv: list[str] | None = None) -> int:
    return _run_script_main("scripts/generate_spec_lang_builtin_catalog.py", argv)


def generate_spec_schema_field_catalog_main(argv: list[str] | None = None) -> int:
    return _run_script_main("scripts/generate_spec_schema_field_catalog.py", argv)


def generate_traceability_catalog_main(argv: list[str] | None = None) -> int:
    return _run_script_main("scripts/generate_traceability_catalog.py", argv)


def perf_smoke_main(argv: list[str] | None = None) -> int:
    return int(_perf_smoke_main(argv))


def run_governance_specs_main(argv: list[str] | None = None) -> int:
    from spec_runner.governance_runtime import main as _main

    return int(_main(argv))
