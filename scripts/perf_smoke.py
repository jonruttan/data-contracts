#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any

import yaml


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


def _sha256_hex(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        while True:
            chunk = fh.read(8192)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


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


def _load_baseline_notes(path: Path) -> dict[str, str]:
    try:
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"missing baseline notes file: {path}") from exc
    except yaml.YAMLError as exc:
        raise ValueError(f"invalid yaml baseline notes: {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValueError(f"baseline notes payload must be a mapping: {path}")
    entries = payload.get("entries")
    if not isinstance(entries, list):
        raise ValueError(f"baseline notes entries must be a list: {path}")
    out: dict[str, str] = {}
    for idx, item in enumerate(entries):
        if not isinstance(item, dict):
            raise ValueError(f"baseline notes entry[{idx}] must be a mapping: {path}")
        baseline = str(item.get("baseline", "")).strip()
        sha = str(item.get("sha256", "")).strip()
        if not baseline or not sha:
            continue
        out[baseline] = sha
    return out


def _contract_rel(root: Path, path: Path) -> str:
    try:
        return "/" + path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def _run(cmd: list[str], *, cwd: Path) -> int:
    cp = subprocess.run(cmd, cwd=cwd, check=False)
    return int(cp.returncode)


def _ensure_generated_file(
    *,
    path: Path,
    regenerate_cmd: list[str],
    cwd: Path,
) -> None:
    if path.exists():
        return
    code = _run(regenerate_cmd, cwd=cwd)
    if code != 0:
        raise ValueError(f"failed to regenerate missing file: {path}")
    if not path.exists():
        raise ValueError(f"missing file: {path}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Run local perf smoke checks for governance/docs timing.")
    ap.add_argument("--mode", choices=("warn", "strict"), default="warn")
    ap.add_argument("--governance-baseline", default="/docs/spec/metrics/governance_timing_baseline.json")
    ap.add_argument("--docs-baseline", default="/docs/spec/metrics/docs_generate_timing_baseline.json")
    ap.add_argument("--governance-profile-baseline", default="/docs/spec/metrics/governance_profile_baseline.json")
    ap.add_argument("--docs-profile-baseline", default="/docs/spec/metrics/docs_generate_profile_baseline.json")
    ap.add_argument("--governance-timing", default="/.artifacts/governance-timing.json")
    ap.add_argument("--docs-timing", default="/.artifacts/docs-generate-timing.json")
    ap.add_argument("--governance-profile", default="/.artifacts/governance-profile.json")
    ap.add_argument("--docs-profile", default="/.artifacts/docs-generate-profile.json")
    ap.add_argument("--baseline-notes", default="/docs/spec/metrics/baseline_update_notes.yaml")
    ap.add_argument("--report-out", default="/.artifacts/perf-smoke-report.json")
    ap.add_argument("--compare-only", action="store_true", help="Skip command execution and compare existing timing files")
    ns = ap.parse_args(argv)

    root = Path(__file__).resolve().parents[1]
    py = root / ".venv/bin/python"
    py_bin = str(py) if py.exists() else "python3"

    governance_timing = _resolve(root, ns.governance_timing)
    docs_timing = _resolve(root, ns.docs_timing)
    governance_profile = _resolve(root, ns.governance_profile)
    docs_profile = _resolve(root, ns.docs_profile)
    governance_baseline = _resolve(root, ns.governance_baseline)
    docs_baseline = _resolve(root, ns.docs_baseline)
    governance_profile_baseline = _resolve(root, ns.governance_profile_baseline)
    docs_profile_baseline = _resolve(root, ns.docs_profile_baseline)
    baseline_notes = _resolve(root, ns.baseline_notes)
    report_out = _resolve(root, ns.report_out)

    checks: list[dict[str, Any]] = []
    failures: list[str] = []

    if not ns.compare_only:
        governance_cmd = [
            py_bin,
            "scripts/run_governance_specs.py",
            "--timing-out",
            str(governance_timing),
            "--profile",
            "--profile-out",
            str(governance_profile),
        ]
        code = _run(governance_cmd, cwd=root)
        if code != 0:
            return code
        docs_cmd = [
            py_bin,
            "scripts/docs_generate_all.py",
            "--check",
            "--timing-out",
            str(docs_timing),
            "--profile",
            "--profile-out",
            str(docs_profile),
        ]
        code = _run(docs_cmd, cwd=root)
        if code != 0:
            return code
        # CI can occasionally observe missing profile artifacts despite
        # successful command exits; regenerate once to keep perf checks stable.
        _ensure_generated_file(path=governance_timing, regenerate_cmd=governance_cmd, cwd=root)
        _ensure_generated_file(path=governance_profile, regenerate_cmd=governance_cmd, cwd=root)
        _ensure_generated_file(path=docs_timing, regenerate_cmd=docs_cmd, cwd=root)
        _ensure_generated_file(path=docs_profile, regenerate_cmd=docs_cmd, cwd=root)

    for label, timing_path, baseline_path in (
        ("governance_timing", governance_timing, governance_baseline),
        ("docs_generate_timing", docs_timing, docs_baseline),
        ("governance_profile", governance_profile, governance_profile_baseline),
        ("docs_generate_profile", docs_profile, docs_profile_baseline),
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

    notes = _load_baseline_notes(baseline_notes)
    for baseline_path in (
        governance_baseline,
        docs_baseline,
        governance_profile_baseline,
        docs_profile_baseline,
    ):
        baseline_key = _contract_rel(root, baseline_path)
        expected_sha = _sha256_hex(baseline_path)
        noted_sha = notes.get(baseline_key, "") or notes.get(baseline_key.lstrip("/"), "")
        ok = noted_sha == expected_sha
        checks.append(
            {
                "id": f"baseline_notes:{baseline_key}",
                "baseline": baseline_key,
                "expected_sha256": expected_sha,
                "noted_sha256": noted_sha,
                "status": "pass" if ok else "fail",
            }
        )
        if not ok:
            failures.append(
                f"baseline notes mismatch for {baseline_key} (expected sha256 {expected_sha})"
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
    print(f"wrote {report_out.relative_to(root).as_posix() if report_out.is_relative_to(root) else report_out}")
    if failures:
        for msg in failures:
            print(f"WARN: {msg}" if ns.mode == "warn" else f"ERROR: {msg}")
    return 0 if (not failures or ns.mode == "warn") else 1


if __name__ == "__main__":
    raise SystemExit(main())
