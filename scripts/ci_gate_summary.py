#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import json
import subprocess
import time
from datetime import UTC, datetime
from pathlib import Path

from spec_runner.doc_parser import iter_spec_doc_tests
from spec_runner.governance_engine import normalize_policy_evaluate
from spec_runner.spec_lang import SpecLangLimits, eval_predicate


def _now_iso_utc() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _runner_command(runner_bin: str, runner_impl: str, subcommand: str) -> list[str]:
    normalized = runner_bin.replace("\\", "/")
    if normalized.endswith("/scripts/runner_adapter.sh") or normalized in {
        "scripts/runner_adapter.sh",
        "./scripts/runner_adapter.sh",
    }:
        return [runner_bin, "--impl", runner_impl, subcommand]
    return [runner_bin, subcommand]


def _default_steps(runner_bin: str, runner_impl: str) -> list[tuple[str, list[str]]]:
    return [
        ("governance", _runner_command(runner_bin, runner_impl, "governance")),
        ("docs_generate_check", _runner_command(runner_bin, runner_impl, "docs-generate-check")),
        ("docs_lint", _runner_command(runner_bin, runner_impl, "docs-lint")),
        ("normalize_check", _runner_command(runner_bin, runner_impl, "normalize-check")),
        ("schema_registry_build", _runner_command(runner_bin, runner_impl, "schema-registry-build")),
        ("schema_registry_check", _runner_command(runner_bin, runner_impl, "schema-registry-check")),
        ("schema_docs_check", _runner_command(runner_bin, runner_impl, "schema-docs-check")),
        ("spec_portability_json", _runner_command(runner_bin, runner_impl, "spec-portability-json")),
        ("spec_portability_md", _runner_command(runner_bin, runner_impl, "spec-portability-md")),
        ("spec_lang_adoption_json", _runner_command(runner_bin, runner_impl, "spec-lang-adoption-json")),
        ("spec_lang_adoption_md", _runner_command(runner_bin, runner_impl, "spec-lang-adoption-md")),
        ("runner_independence_json", _runner_command(runner_bin, runner_impl, "runner-independence-json")),
        ("runner_independence_md", _runner_command(runner_bin, runner_impl, "runner-independence-md")),
        ("python_dependency_json", _runner_command(runner_bin, runner_impl, "python-dependency-json")),
        ("python_dependency_md", _runner_command(runner_bin, runner_impl, "python-dependency-md")),
        ("docs_operability_json", _runner_command(runner_bin, runner_impl, "docs-operability-json")),
        ("docs_operability_md", _runner_command(runner_bin, runner_impl, "docs-operability-md")),
        ("contract_assertions_json", _runner_command(runner_bin, runner_impl, "contract-assertions-json")),
        ("contract_assertions_md", _runner_command(runner_bin, runner_impl, "contract-assertions-md")),
        ("objective_scorecard_json", _runner_command(runner_bin, runner_impl, "objective-scorecard-json")),
        ("objective_scorecard_md", _runner_command(runner_bin, runner_impl, "objective-scorecard-md")),
        ("spec_lang_stdlib_json", _runner_command(runner_bin, runner_impl, "spec-lang-stdlib-json")),
        ("spec_lang_stdlib_md", _runner_command(runner_bin, runner_impl, "spec-lang-stdlib-md")),
        ("evaluate_style", _runner_command(runner_bin, runner_impl, "style-check")),
        ("ruff", _runner_command(runner_bin, runner_impl, "lint")),
        ("mypy", _runner_command(runner_bin, runner_impl, "typecheck")),
        ("compileall", _runner_command(runner_bin, runner_impl, "compilecheck")),
        ("conformance_purpose_json", _runner_command(runner_bin, runner_impl, "conformance-purpose-json")),
        ("conformance_purpose_md", _runner_command(runner_bin, runner_impl, "conformance-purpose-md")),
        ("conformance_parity", _runner_command(runner_bin, runner_impl, "conformance-parity")),
        ("pytest", _runner_command(runner_bin, runner_impl, "test-full")),
    ]


def _run_command(command: list[str]) -> int:
    proc = subprocess.run(command, check=False)
    return int(proc.returncode)


def _run_steps(steps: list[tuple[str, list[str]]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for name, command in steps:
        print(f"[gate] {name}: {' '.join(command)}")
        t0 = time.perf_counter()
        code = _run_command(command)
        duration_ms = int((time.perf_counter() - t0) * 1000)
        status = "pass" if code == 0 else "fail"
        rows.append(
            {
                "name": name,
                "command": command,
                "status": status,
                "exit_code": code,
                "duration_ms": duration_ms,
            }
        )
    return rows


def _load_gate_policy_expr(policy_case: Path) -> list[object]:
    parent = policy_case.parent
    pattern = policy_case.name
    for spec in iter_spec_doc_tests(parent, file_pattern=pattern):
        if spec.doc_path.resolve() != policy_case.resolve():
            continue
        if str(spec.test.get("check", "")).strip() != "runtime.orchestration_policy_via_spec_lang":
            continue
        harness = spec.test.get("harness")
        if not isinstance(harness, dict):
            continue
        orch = harness.get("orchestration_policy")
        if not isinstance(orch, dict):
            continue
        expr = orch.get("policy_evaluate")
        if isinstance(expr, list) and expr:
            return normalize_policy_evaluate(
                expr,
                field="harness.orchestration_policy.policy_evaluate",
            )
    raise ValueError(
        f"missing harness.orchestration_policy.policy_evaluate in {policy_case}"
    )


def _evaluate_gate_policy(*, rows: list[dict[str, object]], policy_evaluate: list[object]) -> bool:
    return eval_predicate(policy_evaluate, subject=rows, limits=SpecLangLimits())


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Run local CI gate checks and emit machine-readable summary JSON."
    )
    ap.add_argument(
        "--out",
        default=".artifacts/gate-summary.json",
        help="Output path for gate summary JSON (default: .artifacts/gate-summary.json)",
    )
    ap.add_argument("--runner-bin", required=True, help="Path to runner interface command")
    ap.add_argument(
        "--runner-impl",
        default=os.environ.get("SPEC_RUNNER_IMPL", "rust"),
        help="Runner implementation mode passed to runner adapter (default: rust).",
    )
    ap.add_argument(
        "--policy-case",
        default="docs/spec/governance/cases/core/runtime_orchestration_policy_via_spec_lang.spec.md",
        help="Governance spec case containing orchestration policy_evaluate policy.",
    )
    ap.add_argument(
        "--trace-out",
        default=os.environ.get("SPEC_RUNNER_TRACE_OUT", ""),
        help="Optional output path for command execution trace JSON.",
    )
    ns = ap.parse_args(argv)

    out_path = Path(str(ns.out))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    policy_case = Path(str(ns.policy_case))
    policy_evaluate = _load_gate_policy_expr(policy_case)

    started = _now_iso_utc()
    t0 = time.perf_counter()
    steps = _run_steps(_default_steps(str(ns.runner_bin), str(ns.runner_impl)))
    verdict = _evaluate_gate_policy(rows=steps, policy_evaluate=policy_evaluate)
    first_failure = next((int(step["exit_code"]) for step in steps if int(step["exit_code"]) != 0), 1)
    exit_code = 0 if verdict else first_failure
    total_duration_ms = int((time.perf_counter() - t0) * 1000)
    finished = _now_iso_utc()

    payload: dict[str, object] = {
        "version": 1,
        "status": "pass" if verdict else "fail",
        "policy_verdict": "pass" if verdict else "fail",
        "policy_case": str(policy_case),
        "policy_expr": policy_evaluate,
        "started_at": started,
        "finished_at": finished,
        "total_duration_ms": total_duration_ms,
        "steps": steps,
        "runner_bin": str(ns.runner_bin),
        "runner_impl": str(ns.runner_impl),
    }
    out_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    trace_out = str(ns.trace_out or "").strip()
    if trace_out:
        trace_path = Path(trace_out)
        trace_path.parent.mkdir(parents=True, exist_ok=True)
        trace_payload = {
            "version": 1,
            "runner_bin": str(ns.runner_bin),
            "runner_impl": str(ns.runner_impl),
            "steps": steps,
        }
        trace_path.write_text(json.dumps(trace_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"[gate] trace: {trace_path}")
    print(f"[gate] summary: {out_path}")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
