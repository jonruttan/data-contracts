#!/usr/bin/env python3
from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any

from spec_runner.dispatcher import SpecRunContext, iter_cases, run_case
from spec_runner.runtime_context import MiniCapsys, MiniMonkeyPatch
from spec_runner.settings import case_file_name
from spec_runner.virtual_paths import resolve_contract_path


def _resolve_out(repo_root: Path, raw: str, *, field: str) -> Path:
    try:
        return resolve_contract_path(repo_root, raw, field=field)
    except Exception:
        return repo_root / str(raw).lstrip("/")


def _surface_id(case_test: dict[str, Any]) -> str:
    harness = case_test.get("harness") if isinstance(case_test, dict) else None
    if not isinstance(harness, dict):
        return ""
    docs_generate = harness.get("docs_generate")
    if not isinstance(docs_generate, dict):
        return ""
    return str(docs_generate.get("surface_id", "")).strip()


def _render_summary(payload: dict[str, Any]) -> str:
    lines = [
        "# Docs Generate Specs Summary",
        "",
        f"- status: {payload.get('status', 'fail')}",
        f"- case_count: {int(payload.get('summary', {}).get('case_count', 0))}",
        f"- passed_count: {int(payload.get('summary', {}).get('passed_count', 0))}",
        f"- failed_count: {int(payload.get('summary', {}).get('failed_count', 0))}",
        "",
        "| case_id | surface_id | status |",
        "|---|---|---|",
    ]
    for row in payload.get("cases") or []:
        lines.append(
            f"| `{row.get('case_id', '')}` | `{row.get('surface_id', '')}` | `{row.get('status', 'fail')}` |"
        )
    lines.append("")
    errors = payload.get("errors") or []
    if errors:
        lines += ["## Errors", ""]
        for err in errors:
            lines.append(f"- {err}")
        lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Run docs.generate executable specs.")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--build", action="store_true")
    mode.add_argument("--check", action="store_true")
    ap.add_argument("--surface", default="", help="Optional docs surface_id filter")
    ap.add_argument("--cases", default="docs/spec/impl/docs_generate/cases")
    ap.add_argument("--jobs", type=int, default=0, help="Parallel jobs for independent docs surfaces (0=auto)")
    ap.add_argument("--report-out", default=".artifacts/docs-generator-report.json")
    ap.add_argument("--summary-out", default=".artifacts/docs-generator-summary.md")
    ns = ap.parse_args(argv)

    repo_root = Path(__file__).resolve().parents[1]
    mode_value = "check" if ns.check else "write"
    case_dir = _resolve_out(repo_root, str(ns.cases), field="docs_generate_specs.cases")
    if not case_dir.exists():
        print(f"missing docs generate cases path: {ns.cases}")
        return 1

    selected = []
    for case in iter_cases(case_dir, file_pattern=case_file_name("*")):
        if str(case.test.get("type", "")).strip() != "docs.generate":
            continue
        sid = _surface_id(case.test)
        if str(ns.surface).strip() and sid != str(ns.surface).strip():
            continue
        selected.append((case, sid))

    errors: list[str] = []
    if str(ns.surface).strip() and not selected:
        errors.append(f"unknown surface_id: {str(ns.surface).strip()}")

    rows: list[dict[str, Any]] = []
    env = dict(os.environ)
    env["SPEC_DOCS_GENERATE_MODE"] = mode_value

    with TemporaryDirectory(prefix="spec-runner-docs-generate-") as td:
        td_path = Path(td)

        def _run_one(task: tuple[int, Any, str]) -> tuple[int, dict[str, Any], str | None]:
            idx, case, sid = task
            case_id = str(case.test.get("id", "")).strip() or "<unknown>"
            case_tmp = td_path / f"case_{idx}"
            case_tmp.mkdir(parents=True, exist_ok=True)
            ctx = SpecRunContext(
                tmp_path=case_tmp,
                patcher=MiniMonkeyPatch(),
                capture=MiniCapsys(),
                env=env,
            )
            try:
                run_case(case, ctx=ctx)
                return idx, {"case_id": case_id, "surface_id": sid, "status": "pass"}, None
            except BaseException as exc:  # noqa: BLE001
                return idx, {"case_id": case_id, "surface_id": sid, "status": "fail"}, f"{case_id}: {exc}"

        indexed = [(idx, case, sid) for idx, (case, sid) in enumerate(selected)]
        if len(indexed) <= 1:
            for task in indexed:
                _idx, row, err = _run_one(task)
                rows.append(row)
                if err:
                    errors.append(err)
        else:
            auto_workers = max(1, os.cpu_count() or 1)
            requested = int(ns.jobs)
            if requested <= 0:
                max_workers = min(auto_workers, len(indexed))
            else:
                max_workers = min(max(1, requested), len(indexed))
            results: list[tuple[int, dict[str, Any], str | None]] = []
            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
                for result in executor.map(_run_one, indexed):
                    results.append(result)
            for _idx, row, err in sorted(results, key=lambda x: x[0]):
                rows.append(row)
                if err:
                    errors.append(err)

    passed = sum(1 for x in rows if x["status"] == "pass")
    failed = len(rows) - passed
    payload = {
        "version": 1,
        "status": "pass" if not errors and failed == 0 else "fail",
        "summary": {
            "case_count": len(rows),
            "passed_count": passed,
            "failed_count": failed,
        },
        "cases": rows,
        "errors": errors,
    }

    report_path = _resolve_out(repo_root, str(ns.report_out), field="docs_generate_specs.report_out")
    summary_path = _resolve_out(repo_root, str(ns.summary_out), field="docs_generate_specs.summary_out")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    summary_path.write_text(_render_summary(payload), encoding="utf-8")
    print(f"wrote {ns.report_out}")
    print(f"wrote {ns.summary_out}")
    if errors:
        for err in errors:
            print(err)
    return 0 if payload["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
