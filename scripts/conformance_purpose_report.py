#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from spec_runner.conformance_purpose import conformance_purpose_report_jsonable


def _to_markdown(payload: dict) -> str:
    summary = payload.get("summary") or {}
    lines = [
        "# Conformance Purpose Report",
        "",
        f"- total cases: {int(summary.get('total_rows', 0))}",
        f"- rows with warnings: {int(summary.get('rows_with_warnings', 0))}",
        f"- total warnings: {int(summary.get('total_warning_count', 0))}",
        "",
        "## Warnings",
        "",
        "| id | type | warning | file |",
        "| --- | --- | --- | --- |",
    ]
    had_any = False
    for row in payload.get("rows", []):
        rid = str(row.get("id", "")).strip()
        rtype = str(row.get("type", "")).strip()
        file_ = str(row.get("file", "")).strip()
        for w in row.get("warnings", []) or []:
            had_any = True
            ww = str(w).replace("|", "\\|")
            lines.append(f"| {rid} | {rtype} | {ww} | {file_} |")
    if not had_any:
        lines.append("| - | - | none | - |")
    return "\n".join(lines) + "\n"


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
    ns = ap.parse_args(argv)

    repo_root = Path(__file__).resolve().parents[3]
    payload = conformance_purpose_report_jsonable(Path(ns.cases), repo_root=repo_root)
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
