#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
from typing import Any

from spec_runner.docs_generators import load_docs_generator_registry, resolve_virtual_path


GENERATOR_COMMANDS: dict[str, list[str]] = {
    "docs_build_reference": ["scripts/docs_build_reference.py"],
    "generate_schema_docs": ["scripts/generate_schema_docs.py"],
    "generate_runner_api_catalog": ["scripts/generate_runner_api_catalog.py"],
    "generate_harness_type_catalog": ["scripts/generate_harness_type_catalog.py"],
    "generate_spec_lang_builtin_catalog": ["scripts/generate_spec_lang_builtin_catalog.py"],
    "generate_policy_rule_catalog": ["scripts/generate_policy_rule_catalog.py"],
    "generate_traceability_catalog": ["scripts/generate_traceability_catalog.py"],
    "generate_governance_check_catalog": ["scripts/generate_governance_check_catalog.py"],
    "generate_metrics_field_catalog": ["scripts/generate_metrics_field_catalog.py"],
    "generate_spec_schema_field_catalog": ["scripts/generate_spec_schema_field_catalog.py"],
}


def _run(repo_root: Path, script_args: list[str]) -> tuple[int, str]:
    cmd = [str(repo_root / ".venv/bin/python"), *script_args]
    if not (repo_root / ".venv/bin/python").exists():
        cmd = ["python3", *script_args]
    cp = subprocess.run(cmd, cwd=repo_root, check=False, capture_output=True, text=True)
    out = (cp.stdout or "") + (cp.stderr or "")
    return int(cp.returncode), out


def _surface_rows(registry: dict[str, Any]) -> list[dict[str, Any]]:
    rows = registry.get("surfaces")
    if not isinstance(rows, list):
        return []
    return [r for r in rows if isinstance(r, dict)]


def _exec_surface(repo_root: Path, surface: dict[str, Any], *, check: bool) -> tuple[bool, str]:
    sid = str(surface.get("surface_id", "")).strip()
    gen = str(surface.get("generator", "")).strip()
    base = GENERATOR_COMMANDS.get(gen)
    if not base:
        return False, f"{sid}: unknown generator command id {gen}"
    args = [*base]
    if check:
        args.append("--check")
    rc, out = _run(repo_root, args)
    if rc != 0:
        return False, f"{sid}: generator failed ({gen})\n{out}".rstrip()
    return True, out.strip()


def _validate_registry_paths(repo_root: Path, registry: dict[str, Any]) -> list[str]:
    errs: list[str] = []
    for surface in _surface_rows(registry):
        sid = str(surface.get("surface_id", "")).strip() or "<unknown>"
        for key in ("inputs", "outputs", "owner_contract_docs", "read_only_sections"):
            for idx, raw in enumerate(surface.get(key) or []):
                try:
                    p = resolve_virtual_path(repo_root, str(raw), field=f"{sid}.{key}[{idx}]")
                except Exception as exc:  # noqa: BLE001
                    errs.append(f"{sid}.{key}[{idx}]: invalid path {raw!r} ({exc})")
                    continue
                if key in {"inputs", "owner_contract_docs"} and not p.exists():
                    errs.append(f"{sid}.{key}[{idx}]: missing path {raw}")
    return errs


def _render_summary(payload: dict[str, Any]) -> str:
    lines = [
        "# Docs Generator Summary",
        "",
        f"- status: {payload.get('status', 'fail')}",
        f"- surface_count: {int(payload.get('summary', {}).get('surface_count', 0))}",
        f"- passed_count: {int(payload.get('summary', {}).get('passed_count', 0))}",
        f"- failed_count: {int(payload.get('summary', {}).get('failed_count', 0))}",
        "",
        "| surface_id | generator | status |",
        "|---|---|---|",
    ]
    for row in payload.get("surfaces") or []:
        lines.append(
            f"| `{row.get('surface_id', '')}` | `{row.get('generator', '')}` | `{row.get('status', 'fail')}` |"
        )
    lines.append("")
    errs = payload.get("errors") or []
    if errs:
        lines += ["## Errors", ""]
        for e in errs:
            lines.append(f"- {e}")
        lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Generate and verify all docs surfaces from registry.")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--build", action="store_true")
    mode.add_argument("--check", action="store_true")
    ap.add_argument("--surface", default="", help="Optional surface_id filter")
    ap.add_argument("--report-out", default=".artifacts/docs-generator-report.json")
    ap.add_argument("--summary-out", default=".artifacts/docs-generator-summary.md")
    ns = ap.parse_args(argv)

    repo_root = Path(__file__).resolve().parents[1]
    registry, reg_issues = load_docs_generator_registry(repo_root)
    errors = [x.render() for x in reg_issues]
    if registry is not None:
        errors.extend(_validate_registry_paths(repo_root, registry))
    if registry is None:
        payload = {
            "version": 1,
            "status": "fail",
            "summary": {"surface_count": 0, "passed_count": 0, "failed_count": 0},
            "surfaces": [],
            "errors": errors,
        }
        report_path = resolve_virtual_path(repo_root, str(ns.report_out), field="docs_generate_all.report_out")
        summary_path = resolve_virtual_path(repo_root, str(ns.summary_out), field="docs_generate_all.summary_out")
        report_path.parent.mkdir(parents=True, exist_ok=True)
        summary_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        summary_path.write_text(_render_summary(payload), encoding="utf-8")
        return 1

    target = str(ns.surface).strip()
    selected = []
    for row in _surface_rows(registry):
        sid = str(row.get("surface_id", "")).strip()
        if target and sid != target:
            continue
        selected.append(row)
    if target and not selected:
        errors.append(f"unknown surface_id: {target}")

    rows: list[dict[str, Any]] = []
    for s in selected:
        sid = str(s.get("surface_id", "")).strip()
        gen = str(s.get("generator", "")).strip()
        ok, msg = _exec_surface(repo_root, s, check=bool(ns.check))
        rows.append({"surface_id": sid, "generator": gen, "status": "pass" if ok else "fail"})
        if not ok and msg:
            lines = [x for x in msg.splitlines() if x.strip()]
            errors.extend(lines)

    passed = sum(1 for r in rows if r["status"] == "pass")
    failed = len(rows) - passed
    payload = {
        "version": 1,
        "status": "pass" if failed == 0 and not errors else "fail",
        "summary": {"surface_count": len(rows), "passed_count": passed, "failed_count": failed},
        "surfaces": rows,
        "errors": errors,
    }
    report_path = resolve_virtual_path(repo_root, str(ns.report_out), field="docs_generate_all.report_out")
    summary_path = resolve_virtual_path(repo_root, str(ns.summary_out), field="docs_generate_all.summary_out")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    summary_path.write_text(_render_summary(payload), encoding="utf-8")
    if errors:
        for err in errors:
            print(err)
    print(f"wrote {ns.report_out}")
    print(f"wrote {ns.summary_out}")
    return 0 if payload["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
