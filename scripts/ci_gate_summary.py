#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import time
from datetime import UTC, datetime
from pathlib import Path

from spec_runner.doc_parser import iter_spec_doc_tests
from spec_runner.spec_lang import SpecLangLimits, eval_predicate


def _now_iso_utc() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _default_steps(runner_bin: str) -> list[tuple[str, list[str]]]:
    return [
        ("governance", [runner_bin, "governance"]),
        ("docs_build_check", [runner_bin, "docs-build-check"]),
        ("docs_lint", [runner_bin, "docs-lint"]),
        ("spec_portability_json", [runner_bin, "spec-portability-json"]),
        ("spec_portability_md", [runner_bin, "spec-portability-md"]),
        ("evaluate_style", [runner_bin, "style-check"]),
        ("ruff", [runner_bin, "lint"]),
        ("mypy", [runner_bin, "typecheck"]),
        ("compileall", [runner_bin, "compilecheck"]),
        ("conformance_purpose_json", [runner_bin, "conformance-purpose-json"]),
        ("conformance_purpose_md", [runner_bin, "conformance-purpose-md"]),
        ("conformance_parity", [runner_bin, "conformance-parity"]),
        ("pytest", [runner_bin, "test-full"]),
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
        expr = orch.get("decision_expr")
        if isinstance(expr, list) and expr:
            if isinstance(expr[0], str):
                return expr
            if len(expr) == 1 and isinstance(expr[0], list) and expr[0] and isinstance(expr[0][0], str):
                return expr[0]
    raise ValueError(
        f"missing harness.orchestration_policy.decision_expr in {policy_case}"
    )


def _evaluate_gate_policy(*, rows: list[dict[str, object]], decision_expr: list[object]) -> bool:
    return eval_predicate(decision_expr, subject=rows, limits=SpecLangLimits())


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
        "--policy-case",
        default="docs/spec/governance/cases/runtime_orchestration_policy_via_spec_lang.spec.md",
        help="Governance spec case containing orchestration decision_expr policy.",
    )
    ns = ap.parse_args(argv)

    out_path = Path(str(ns.out))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    policy_case = Path(str(ns.policy_case))
    decision_expr = _load_gate_policy_expr(policy_case)

    started = _now_iso_utc()
    t0 = time.perf_counter()
    steps = _run_steps(_default_steps(str(ns.runner_bin)))
    verdict = _evaluate_gate_policy(rows=steps, decision_expr=decision_expr)
    first_failure = next((int(step["exit_code"]) for step in steps if int(step["exit_code"]) != 0), 1)
    exit_code = 0 if verdict else first_failure
    total_duration_ms = int((time.perf_counter() - t0) * 1000)
    finished = _now_iso_utc()

    payload: dict[str, object] = {
        "version": 1,
        "status": "pass" if verdict else "fail",
        "policy_verdict": "pass" if verdict else "fail",
        "policy_case": str(policy_case),
        "policy_expr": decision_expr,
        "started_at": started,
        "finished_at": finished,
        "total_duration_ms": total_duration_ms,
        "steps": steps,
    }
    out_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"[gate] summary: {out_path}")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
