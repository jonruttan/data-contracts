#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


def _classify(body: str) -> str:
    lowered = body.lower()
    if "subprocess.run(" in body or "yaml.safe_load(" in body:
        return "extractor_only"
    if "iter_spec_doc_tests(" in body or "iter_cases(" in body:
        return "extractor_only"
    if "load_external_cases(" in body:
        return "extractor_only"
    if "normalize_policy_evaluate(" in body or "_policy_outcome(" in body:
        return "decision_migratable_now"
    if "compare_metric_non_regression(" in body:
        return "decision_migratable_now"
    if "governance.check requires" in lowered:
        return "decision_migratable_now"
    if "re.compile(" in body and "violations.append" in body:
        return "blocked_by_subject_model"
    return "decision_migratable_now"


def _extract_scan_functions(script_text: str) -> list[dict[str, Any]]:
    funcs: list[dict[str, Any]] = []
    pattern = re.compile(r"^def (_scan_[a-z0-9_]+)\(.*?\):\n", re.MULTILINE)
    matches = list(pattern.finditer(script_text))
    for i, m in enumerate(matches):
        name = m.group(1)
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(script_text)
        body = script_text[start:end]
        funcs.append(
            {
                "name": name,
                "classification": _classify(body),
                "signals": {
                    "uses_subprocess": "subprocess.run(" in body,
                    "uses_policy_outcome": "_policy_outcome(" in body,
                    "uses_regex_scanning": "re.compile(" in body,
                    "reads_cases": "iter_cases(" in body or "iter_spec_doc_tests(" in body,
                },
            }
        )
    return funcs


def _render_md(payload: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append("# Python Decision Surface")
    lines.append("")
    lines.append(f"- script: `{payload['script']}`")
    lines.append(f"- scan_function_count: `{payload['summary']['scan_function_count']}`")
    lines.append("")
    lines.append("## Summary")
    for key, value in payload["summary"]["classification_counts"].items():
        lines.append(f"- `{key}`: `{value}`")
    lines.append("")
    lines.append("## Functions")
    for row in payload["rows"]:
        lines.append(f"- `{row['name']}`: `{row['classification']}`")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Report governance scan function migration status.")
    ap.add_argument(
        "--script",
        default="scripts/run_governance_specs.py",
        help="Path to governance script to inspect.",
    )
    ap.add_argument(
        "--out-json",
        default=".artifacts/python-decision-surface.json",
        help="JSON output path.",
    )
    ap.add_argument(
        "--out-md",
        default=".artifacts/python-decision-surface-summary.md",
        help="Markdown output path.",
    )
    ns = ap.parse_args(argv)

    script_path = Path(str(ns.script))
    if not script_path.exists():
        raise SystemExit(f"missing script: {script_path}")
    text = script_path.read_text(encoding="utf-8")
    rows = _extract_scan_functions(text)
    counts = {
        "extractor_only": 0,
        "decision_migratable_now": 0,
        "blocked_by_subject_model": 0,
    }
    for row in rows:
        counts[row["classification"]] = counts.get(row["classification"], 0) + 1
    rows.sort(key=lambda r: str(r["name"]))

    payload = {
        "version": 1,
        "script": str(script_path),
        "summary": {
            "scan_function_count": len(rows),
            "classification_counts": counts,
        },
        "rows": rows,
    }

    out_json = Path(str(ns.out_json))
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    out_md = Path(str(ns.out_md))
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(_render_md(payload), encoding="utf-8")

    print(f"wrote {out_json}")
    print(f"wrote {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
