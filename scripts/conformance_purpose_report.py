#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path

from spec_runner.conformance_purpose import conformance_purpose_report_jsonable


def _to_markdown(payload: dict) -> str:
    summary = payload.get("summary") or {}
    code_counts = summary.get("warning_code_counts") or {}
    lines = [
        "# Conformance Purpose Report",
        "",
        f"- total cases: {int(summary.get('total_rows', 0))}",
        f"- rows with warnings: {int(summary.get('rows_with_warnings', 0))}",
        f"- total warnings: {int(summary.get('total_warning_count', 0))}",
    ]
    if code_counts:
        parts = [f"{k}={int(v)}" for k, v in sorted(code_counts.items())]
        lines.append(f"- warning codes: {', '.join(parts)}")
    lines.extend(
        [
        "",
        "## Warnings",
        "",
        "| id | type | code | warning | hint | file |",
        "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    had_any = False
    for row in payload.get("rows", []):
        rid = str(row.get("id", "")).strip()
        rtype = str(row.get("type", "")).strip()
        file_ = str(row.get("file", "")).strip()
        for w in row.get("warnings", []) or []:
            had_any = True
            if isinstance(w, dict):
                code = str(w.get("code", "")).strip()
                message = str(w.get("message", "")).strip()
                hint = str(w.get("hint", "")).strip()
            else:
                code = "PUR004"
                message = str(w).strip()
                hint = "Review warning details and update purpose lint configuration."
            ww = message.replace("|", "\\|")
            hh = hint.replace("|", "\\|")
            lines.append(f"| {rid} | {rtype} | {code} | {ww} | {hh} | {file_} |")
    if not had_any:
        lines.append("| - | - | - | none | - | - |")
    return "\n".join(lines) + "\n"


def _filtered_only_warnings(payload: dict) -> dict:
    out = copy.deepcopy(payload)
    rows = [r for r in out.get("rows", []) if (r.get("warnings") or [])]
    out["rows"] = rows
    summary = out.get("summary") or {}
    summary["total_rows"] = len(rows)
    summary["rows_with_warnings"] = len(rows)
    summary["row_warning_count"] = sum(len(r.get("warnings") or []) for r in rows)
    summary["total_warning_count"] = int(summary.get("row_warning_count", 0)) + int(summary.get("policy_error_count", 0))
    code_counts: dict[str, int] = {}
    for r in rows:
        for w in r.get("warnings") or []:
            if isinstance(w, dict):
                code = str(w.get("code", "")).strip() or "PUR004"
            else:
                code = "PUR004"
            code_counts[code] = code_counts.get(code, 0) + 1
    if int(summary.get("policy_error_count", 0)) > 0:
        code_counts["PUR004"] = code_counts.get("PUR004", 0) + int(summary.get("policy_error_count", 0))
    summary["warning_code_counts"] = code_counts
    summary["only_warnings"] = True
    out["summary"] = summary
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Emit conformance purpose report.")
    ap.add_argument(
        "--cases",
        default="docs/spec/conformance/cases",
        help="Path to conformance case docs directory",
    )
    ap.add_argument("--out", help="Optional output path for report.")
    ap.add_argument(
        "--format",
        choices=("json", "md"),
        default="json",
        help="Output format.",
    )
    ap.add_argument(
        "--fail-on-warn",
        action="store_true",
        help="Return non-zero exit when the report contains warnings.",
    )
    ap.add_argument(
        "--only-warnings",
        action="store_true",
        help="Emit only rows that contain warnings.",
    )
    ns = ap.parse_args(argv)

    repo_root = Path(__file__).resolve().parents[3]
    payload = conformance_purpose_report_jsonable(Path(ns.cases), repo_root=repo_root)
    if ns.only_warnings:
        payload = _filtered_only_warnings(payload)
    if ns.format == "md":
        raw = _to_markdown(payload)
    else:
        raw = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if ns.out:
        out = Path(ns.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(raw, encoding="utf-8")
        print(f"wrote {out}")
    else:
        print(raw, end="")
    total_warn = int((payload.get("summary") or {}).get("total_warning_count", 0))
    if ns.fail_on_warn and total_warn > 0:
        print(
            f"ERROR: conformance purpose report has {total_warn} warning(s)",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
