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


def _env_bool(name: str, default: bool) -> bool:
    raw = str(os.environ.get(name, "")).strip().lower()
    if not raw:
        return default
    if raw in {"1", "true", "yes", "on"}:
        return True
    if raw in {"0", "false", "no", "off"}:
        return False
    return default


def _coerce_profile_level(raw: str) -> str:
    level = str(raw or "").strip().lower()
    if level in {"off", "basic", "detailed", "debug"}:
        return level
    return "off"


def _write_fail_profile_artifacts(
    *,
    trace_path: Path,
    summary_path: Path,
    payload: dict[str, object],
) -> None:
    trace_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    run_trace = {
        "version": 1,
        "run_id": f"gate-{int(time.time() * 1000)}",
        "runner_impl": payload.get("runner_impl"),
        "started_at": payload.get("started_at"),
        "ended_at": payload.get("finished_at"),
        "status": payload.get("status"),
        "command": "ci-gate-summary",
        "args": [],
        "env_profile": {},
        "spans": [
            {
                "span_id": "s1",
                "parent_span_id": None,
                "kind": "run",
                "name": "run.total",
                "phase": "run.total",
                "start_ns": 0,
                "end_ns": int(payload.get("total_duration_ms", 0)) * 1_000_000,
                "duration_ms": float(payload.get("total_duration_ms", 0)),
                "status": "ok" if payload.get("status") == "pass" else "error",
                "attrs": {"source": "ci-gate-summary"},
                "error": None,
            }
        ],
        "events": payload.get("events", []),
        "summary": {
            "step_count": len(payload.get("steps", [])) if isinstance(payload.get("steps"), list) else 0,
            "failed_step": payload.get("first_failure_step"),
        },
    }
    trace_path.write_text(json.dumps(run_trace, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    rows = []
    steps = payload.get("steps")
    if isinstance(steps, list):
        for row in steps:
            if isinstance(row, dict):
                rows.append(
                    (
                        str(row.get("name", "")),
                        str(row.get("status", "")),
                        str(row.get("duration_ms", "")),
                    )
                )
    md = [
        "# Run Trace Summary",
        "",
        f"- status: `{payload.get('status', 'unknown')}`",
        f"- first_failure_step: `{payload.get('first_failure_step', '')}`",
        f"- skipped_step_count: `{payload.get('skipped_step_count', 0)}`",
        "",
        "## Steps",
        "",
        "| step | status | duration_ms |",
        "|---|---|---|",
    ]
    for name, status, duration in rows:
        md.append(f"| `{name}` | `{status}` | `{duration}` |")
    md.append("")
    md.append("## Suggested Next Command")
    md.append("")
    md.append("- `./scripts/runner_adapter.sh --impl rust --profile-level detailed ci-gate-summary`")
    summary_path.write_text("\n".join(md) + "\n", encoding="utf-8")


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


def _runner_command_with_liveness(
    runner_bin: str,
    runner_impl: str,
    subcommand: str,
    *,
    level: str,
    stall_ms: str,
    kill_grace_ms: str,
    hard_cap_ms: str,
) -> list[str]:
    normalized = runner_bin.replace("\\", "/")
    if normalized.endswith("/scripts/runner_adapter.sh") or normalized in {
        "scripts/runner_adapter.sh",
        "./scripts/runner_adapter.sh",
    }:
        return [
            runner_bin,
            "--impl",
            runner_impl,
            "--liveness-level",
            level,
            "--liveness-stall-ms",
            stall_ms,
            "--liveness-kill-grace-ms",
            kill_grace_ms,
            "--liveness-hard-cap-ms",
            hard_cap_ms,
            subcommand,
        ]
    return [runner_bin, subcommand]


def _default_steps(runner_bin: str, runner_impl: str) -> list[tuple[str, list[str]]]:
    broad_liveness_level = str(os.environ.get("SPEC_CI_GOV_BROAD_LIVENESS_LEVEL", "strict"))
    broad_liveness_stall_ms = str(os.environ.get("SPEC_CI_GOV_BROAD_LIVENESS_STALL_MS", "5000"))
    broad_liveness_kill_grace_ms = str(os.environ.get("SPEC_CI_GOV_BROAD_LIVENESS_KILL_GRACE_MS", "1000"))
    broad_liveness_hard_cap_ms = str(os.environ.get("SPEC_CI_GOV_BROAD_LIVENESS_HARD_CAP_MS", "120000"))
    return [
        (
            "governance_critical",
            _runner_command(runner_bin, runner_impl, "critical-gate"),
        ),
        (
            "governance_broad",
            _runner_command_with_liveness(
                runner_bin,
                runner_impl,
                "governance",
                level=broad_liveness_level,
                stall_ms=broad_liveness_stall_ms,
                kill_grace_ms=broad_liveness_kill_grace_ms,
                hard_cap_ms=broad_liveness_hard_cap_ms,
            ),
        ),
        ("governance_heavy", _runner_command(runner_bin, runner_impl, "governance-heavy")),
        ("docs_generate_check", _runner_command(runner_bin, runner_impl, "docs-generate-check")),
        ("perf_smoke", _runner_command(runner_bin, runner_impl, "perf-smoke") + ["--mode", "strict"]),
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


def _run_steps(
    steps: list[tuple[str, list[str]]],
    *,
    fail_fast: bool,
) -> tuple[list[dict[str, object]], list[dict[str, object]], str | None]:
    rows: list[dict[str, object]] = []
    events: list[dict[str, object]] = []
    first_failure_step: str | None = None
    aborted = False
    for name, command in steps:
        if aborted:
            rows.append(
                {
                    "name": name,
                    "command": command,
                    "status": "skipped",
                    "exit_code": None,
                    "duration_ms": 0,
                    "skip_reason": "fail_fast.after_failure",
                    "blocked_by": first_failure_step,
                }
            )
            events.append(
                {
                    "ts_ns": time.monotonic_ns(),
                    "kind": "checkpoint",
                    "span_id": "run.total",
                    "attrs": {"event": "gate.step.skipped", "step": name, "blocked_by": first_failure_step},
                }
            )
            continue
        events.append(
            {
                "ts_ns": time.monotonic_ns(),
                "kind": "checkpoint",
                "span_id": "run.total",
                "attrs": {"event": "gate.step.start", "step": name},
            }
        )
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
        if name == "governance_critical":
            rows[-1]["triage_phase"] = "critical"
        elif name == "governance_broad":
            rows[-1]["triage_phase"] = "broad"
            rows[-1]["broad_required"] = True
        events.append(
            {
                "ts_ns": time.monotonic_ns(),
                "kind": "checkpoint",
                "span_id": "run.total",
                "attrs": {"event": f"gate.step.{status}", "step": name, "exit_code": code},
            }
        )
        if status == "fail" and first_failure_step is None:
            first_failure_step = name
            if fail_fast:
                aborted = True
                events.append(
                    {
                        "ts_ns": time.monotonic_ns(),
                        "kind": "checkpoint",
                        "span_id": "run.total",
                        "attrs": {"event": "gate.fail_fast.abort", "after_step": name},
                    }
                )
    return rows, events, first_failure_step


def _collect_unit_test_opt_out(root: Path) -> dict[str, int]:
    tests_root = root / "tests"
    baseline_path = root / "docs/spec/metrics/unit_test_opt_out_baseline.json"
    prefix = "# SPEC-OPT-OUT:"
    total = 0
    opted_out = 0
    if tests_root.exists():
        for path in sorted(tests_root.glob("test_*_unit.py")):
            if not path.is_file():
                continue
            total += 1
            first_non_empty = ""
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    first_non_empty = line.strip()
                    break
            if first_non_empty.startswith(prefix):
                opted_out += 1
    baseline_max = 0
    if baseline_path.exists():
        try:
            payload = json.loads(baseline_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            payload = {}
        if isinstance(payload, dict) and isinstance(payload.get("max_opt_out_file_count"), int):
            baseline_max = int(payload["max_opt_out_file_count"])
    return {
        "total_unit_test_files": total,
        "opt_out_file_count": opted_out,
        "baseline_max_opt_out_file_count": baseline_max,
    }


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
    ap.add_argument(
        "--fail-fast",
        action="store_true",
        default=False,
        help="Stop after first failing gate step (default: true unless --continue-on-fail).",
    )
    ap.add_argument(
        "--continue-on-fail",
        action="store_true",
        help="Disable fail-fast and execute all gate steps.",
    )
    ap.add_argument(
        "--profile-on-fail",
        default=os.environ.get("SPEC_RUNNER_PROFILE_ON_FAIL", "basic"),
        help="off|basic|detailed for fail-fast diagnostics (default: basic).",
    )
    ns = ap.parse_args(argv)

    out_path = Path(str(ns.out))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    policy_case = Path(str(ns.policy_case))
    policy_evaluate = _load_gate_policy_expr(policy_case)
    fail_fast_env_default = _env_bool("SPEC_RUNNER_FAIL_FAST", True)
    fail_fast_enabled = not bool(ns.continue_on_fail)
    if ns.fail_fast:
        fail_fast_enabled = True
    elif not ns.continue_on_fail:
        fail_fast_enabled = fail_fast_env_default
    profile_on_fail = _coerce_profile_level(str(ns.profile_on_fail))

    started = _now_iso_utc()
    t0 = time.perf_counter()
    steps, events, first_failure_step = _run_steps(
        _default_steps(str(ns.runner_bin), str(ns.runner_impl)),
        fail_fast=fail_fast_enabled,
    )
    verdict = _evaluate_gate_policy(rows=steps, policy_evaluate=policy_evaluate)
    first_failure = next(
        (
            int(step["exit_code"])
            for step in steps
            if step.get("exit_code") is not None and int(step["exit_code"]) != 0
        ),
        1,
    )
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
        "events": events,
        "fail_fast_enabled": bool(fail_fast_enabled),
        "first_failure_step": first_failure_step,
        "aborted_after_step": first_failure_step if (first_failure_step and fail_fast_enabled) else None,
        "skipped_step_count": sum(1 for step in steps if str(step.get("status", "")) == "skipped"),
        "runner_bin": str(ns.runner_bin),
        "runner_impl": str(ns.runner_impl),
        "unit_test_opt_out": _collect_unit_test_opt_out(Path.cwd()),
    }
    governance_step = next((s for s in steps if s.get("name") == "governance_broad"), None)
    if isinstance(governance_step, dict):
        payload["triage_attempted"] = bool(governance_step.get("triage_attempted", False))
        payload["triage_mode"] = governance_step.get("triage_mode", "not_run")
        payload["triage_result"] = governance_step.get("triage_result", "not_run")
        payload["failing_check_ids"] = governance_step.get("failing_check_ids", [])
        payload["failing_check_prefixes"] = governance_step.get("failing_check_prefixes", [])
        payload["stall_detected"] = bool(governance_step.get("stall_detected", False))
        payload["stall_phase"] = governance_step.get("stall_phase")
    else:
        payload["triage_attempted"] = False
        payload["triage_mode"] = "not_run"
        payload["triage_result"] = "not_run"
        payload["failing_check_ids"] = []
        payload["failing_check_prefixes"] = []
        payload["stall_detected"] = False
        payload["stall_phase"] = None
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
            "events": events,
            "fail_fast_enabled": bool(fail_fast_enabled),
            "first_failure_step": first_failure_step,
        }
        trace_path.write_text(json.dumps(trace_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"[gate] trace: {trace_path}")
    if exit_code != 0 and profile_on_fail != "off":
        _write_fail_profile_artifacts(
            trace_path=Path(".artifacts/run-trace.json"),
            summary_path=Path(".artifacts/run-trace-summary.md"),
            payload=payload,
        )
        print("[gate] profile: .artifacts/run-trace.json")
        print("[gate] profile-summary: .artifacts/run-trace-summary.md")
    print(f"[gate] summary: {out_path}")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
