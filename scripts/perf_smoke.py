#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


def _resolve(root: Path, raw: str) -> Path:
    text = str(raw)
    p = Path(text)
    if text.startswith("/"):
        if p.exists():
            return p
        return root / text.lstrip("/")
    if p.is_absolute():
        return p
    return root / text.lstrip("/")


def _load_json(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"missing file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid json: {path}: {exc.msg}") from exc
    if not isinstance(payload, dict):
        raise ValueError(f"json object required: {path}")
    return payload


def _read_total_ms(path: Path) -> float:
    payload = _load_json(path)
    summary = payload.get("summary")
    if not isinstance(summary, dict):
        raise ValueError(f"timing summary missing: {path}")
    value = summary.get("total_duration_ms")
    if not isinstance(value, (int, float)):
        raise ValueError(f"summary.total_duration_ms missing: {path}")
    return float(value)


def _read_baseline(path: Path) -> tuple[float, float, float]:
    payload = _load_json(path)
    baseline = payload.get("baseline")
    tolerance = payload.get("tolerance")
    if not isinstance(baseline, dict) or not isinstance(tolerance, dict):
        raise ValueError(f"baseline/tolerance mappings required: {path}")
    base_ms = baseline.get("total_duration_ms")
    ratio = tolerance.get("max_regression_ratio")
    absolute = tolerance.get("max_regression_absolute_ms")
    if not isinstance(base_ms, (int, float)):
        raise ValueError(f"baseline.total_duration_ms must be numeric: {path}")
    if not isinstance(ratio, (int, float)):
        raise ValueError(f"tolerance.max_regression_ratio must be numeric: {path}")
    if not isinstance(absolute, (int, float)):
        raise ValueError(f"tolerance.max_regression_absolute_ms must be numeric: {path}")
    return float(base_ms), float(ratio), float(absolute)


def _run(cmd: list[str], *, cwd: Path) -> int:
    cp = subprocess.run(cmd, cwd=cwd, check=False)
    return int(cp.returncode)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Run local perf smoke checks for governance/docs timing.")
    ap.add_argument("--mode", choices=("warn", "strict"), default="warn")
    ap.add_argument("--governance-baseline", default="/docs/spec/metrics/governance_timing_baseline.json")
    ap.add_argument("--docs-baseline", default="/docs/spec/metrics/docs_generate_timing_baseline.json")
    ap.add_argument("--governance-timing", default="/.artifacts/governance-timing.json")
    ap.add_argument("--docs-timing", default="/.artifacts/docs-generate-timing.json")
    ap.add_argument("--report-out", default="/.artifacts/perf-smoke-report.json")
    ap.add_argument("--compare-only", action="store_true", help="Skip command execution and compare existing timing files")
    ns = ap.parse_args(argv)

    root = Path(__file__).resolve().parents[1]
    py = root / ".venv/bin/python"
    py_bin = str(py) if py.exists() else "python3"

    governance_timing = _resolve(root, ns.governance_timing)
    docs_timing = _resolve(root, ns.docs_timing)
    governance_baseline = _resolve(root, ns.governance_baseline)
    docs_baseline = _resolve(root, ns.docs_baseline)
    report_out = _resolve(root, ns.report_out)

    checks: list[dict[str, Any]] = []
    failures: list[str] = []

    if not ns.compare_only:
        code = _run([py_bin, "scripts/run_governance_specs.py", "--timing-out", str(ns.governance_timing)], cwd=root)
        if code != 0:
            return code
        code = _run(
            [py_bin, "scripts/docs_generate_all.py", "--check", "--timing-out", str(ns.docs_timing)],
            cwd=root,
        )
        if code != 0:
            return code

    for label, timing_path, baseline_path in (
        ("governance", governance_timing, governance_baseline),
        ("docs_generate", docs_timing, docs_baseline),
    ):
        current = _read_total_ms(timing_path)
        baseline_ms, ratio, absolute = _read_baseline(baseline_path)
        allowed = baseline_ms * (1.0 + ratio) + absolute
        ok = current <= allowed
        row = {
            "id": label,
            "current_total_duration_ms": round(current, 3),
            "baseline_total_duration_ms": round(baseline_ms, 3),
            "max_allowed_duration_ms": round(allowed, 3),
            "max_regression_ratio": ratio,
            "max_regression_absolute_ms": absolute,
            "status": "pass" if ok else "fail",
        }
        checks.append(row)
        if not ok:
            failures.append(
                f"{label}: timing regression ({current:.3f}ms > allowed {allowed:.3f}ms; baseline {baseline_ms:.3f}ms)"
            )

    payload = {
        "version": 1,
        "mode": ns.mode,
        "status": "pass" if not failures else ("warn" if ns.mode == "warn" else "fail"),
        "checks": checks,
        "errors": failures,
    }
    report_out.parent.mkdir(parents=True, exist_ok=True)
    report_out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {ns.report_out}")
    if failures:
        for msg in failures:
            print(f"WARN: {msg}" if ns.mode == "warn" else f"ERROR: {msg}")
    return 0 if (not failures or ns.mode == "warn") else 1


if __name__ == "__main__":
    raise SystemExit(main())
