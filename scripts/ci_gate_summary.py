#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from datetime import UTC, datetime
from pathlib import Path


def _now_iso_utc() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _default_steps(python_bin: str) -> list[tuple[str, list[str]]]:
    return [
        ("governance", [python_bin, "scripts/run_governance_specs.py"]),
        ("evaluate_style", [python_bin, "scripts/evaluate_style.py", "--check", "docs/spec"]),
        ("ruff", [python_bin, "-m", "ruff", "check", "."]),
        ("mypy", [python_bin, "-m", "mypy", "spec_runner"]),
        ("compileall", [python_bin, "-m", "compileall", "-q", "spec_runner", "scripts", "tests"]),
        (
            "conformance_purpose_json",
            [python_bin, "scripts/conformance_purpose_report.py", "--out", ".artifacts/conformance-purpose.json"],
        ),
        (
            "conformance_purpose_md",
            [
                python_bin,
                "scripts/conformance_purpose_report.py",
                "--format",
                "md",
                "--out",
                ".artifacts/conformance-purpose-summary.md",
            ],
        ),
        (
            "conformance_parity",
            [
                python_bin,
                "scripts/compare_conformance_parity.py",
                "--cases",
                "docs/spec/conformance/cases",
                "--php-runner",
                "scripts/php/conformance_runner.php",
                "--out",
                ".artifacts/conformance-parity.json",
            ],
        ),
        ("pytest", [python_bin, "-m", "pytest"]),
    ]


def _run_command(command: list[str]) -> int:
    proc = subprocess.run(command, check=False)
    return int(proc.returncode)


def _run_steps(steps: list[tuple[str, list[str]]]) -> tuple[list[dict[str, object]], int]:
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
        if code != 0:
            return rows, code
    return rows, 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Run local CI gate checks and emit machine-readable summary JSON."
    )
    ap.add_argument(
        "--out",
        default=".artifacts/gate-summary.json",
        help="Output path for gate summary JSON (default: .artifacts/gate-summary.json)",
    )
    ap.add_argument(
        "--python-bin",
        default=sys.executable,
        help="Python interpreter used for Python-based gate steps (default: current interpreter)",
    )
    ns = ap.parse_args(argv)

    out_path = Path(str(ns.out))
    out_path.parent.mkdir(parents=True, exist_ok=True)

    started = _now_iso_utc()
    t0 = time.perf_counter()
    steps, exit_code = _run_steps(_default_steps(str(ns.python_bin)))
    total_duration_ms = int((time.perf_counter() - t0) * 1000)
    finished = _now_iso_utc()

    payload: dict[str, object] = {
        "version": 1,
        "status": "pass" if exit_code == 0 else "fail",
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
