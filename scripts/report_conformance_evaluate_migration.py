#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

from spec_runner.doc_parser import iter_spec_doc_tests
from spec_runner.quality_metrics import _collect_leaf_ops


def _classify(*, eval_count: int, total_count: int, case_type: str) -> str:
    if total_count <= 0 or eval_count >= total_count:
        return "already_evaluate_primary"
    if case_type in {"text.file", "cli.run", "api.http"}:
        return "convertible_now_simple"
    if case_type == "governance.check":
        return "convertible_now_with_library"
    return "blocked_needs_subject_shape_change"


def report(cases_dir: Path) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    classes = Counter()
    op_totals = Counter()
    for case in iter_spec_doc_tests(cases_dir, file_pattern="*.spec.md"):
        t = case.test
        case_id = str(t.get("id", "")).strip()
        case_type = str(t.get("type", "")).strip()
        ops = _collect_leaf_ops(t.get("contract", []) or [])
        counts = Counter(ops)
        total = len(ops)
        eval_count = counts.get("evaluate", 0)
        ratio = float(eval_count) / float(total) if total else 1.0
        classification = _classify(eval_count=eval_count, total_count=total, case_type=case_type)
        classes[classification] += 1
        op_totals.update(counts)
        rows.append(
            {
                "id": case_id,
                "type": case_type,
                "file": str(case.doc_path).replace("\\", "/"),
                "total_leaf_ops": total,
                "evaluate_leaf_ops": eval_count,
                "evaluate_ratio": ratio,
                "leaf_ops": dict(sorted(counts.items())),
                "classification": classification,
            }
        )
    rows.sort(key=lambda r: (r["classification"], r["file"], r["id"]))
    total_cases = len(rows)
    ratio = (
        float(sum(float(r["evaluate_leaf_ops"]) for r in rows)) / float(sum(float(r["total_leaf_ops"]) for r in rows))
        if rows and sum(float(r["total_leaf_ops"]) for r in rows) > 0
        else 1.0
    )
    return {
        "version": 1,
        "summary": {
            "total_cases": total_cases,
            "mean_logic_self_contained_ratio": ratio,
            "classification_counts": dict(sorted(classes.items())),
            "leaf_op_totals": dict(sorted(op_totals.items())),
        },
        "cases": rows,
    }


def _to_md(payload: dict[str, Any]) -> str:
    summary = payload.get("summary", {})
    lines = [
        "# Conformance Evaluate Migration",
        "",
        f"- total_cases: `{summary.get('total_cases', 0)}`",
        f"- mean_logic_self_contained_ratio: `{summary.get('mean_logic_self_contained_ratio', 0.0):.6f}`",
        "",
        "## Classification Counts",
    ]
    for key, value in sorted((summary.get("classification_counts") or {}).items()):
        lines.append(f"- `{key}`: `{value}`")
    lines.append("")
    lines.append("## Leaf Op Totals")
    for key, value in sorted((summary.get("leaf_op_totals") or {}).items()):
        lines.append(f"- `{key}`: `{value}`")
    lines.append("")
    lines.append("## Non Evaluate-Primary Cases")
    pending = [r for r in payload.get("cases", []) if r.get("classification") != "already_evaluate_primary"]
    if not pending:
        lines.append("- none")
    else:
        for row in pending:
            lines.append(
                "- "
                + f"`{row.get('id','')}` | `{row.get('type','')}` | "
                + f"`{row.get('evaluate_ratio', 0.0):.3f}` | `{row.get('classification','')}` | `{row.get('file','')}`"
            )
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Report conformance evaluate migration status.")
    parser.add_argument("--cases", default="docs/spec/conformance/cases", help="Conformance cases directory")
    parser.add_argument(
        "--out-json",
        default=".artifacts/conformance-evaluate-migration.json",
        help="Output JSON path",
    )
    parser.add_argument(
        "--out-md",
        default=".artifacts/conformance-evaluate-migration-summary.md",
        help="Output Markdown summary path",
    )
    args = parser.parse_args(argv)
    payload = report(Path(args.cases))
    out_json = Path(args.out_json)
    out_md = Path(args.out_md)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    out_md.write_text(_to_md(payload), encoding="utf-8")
    print(f"wrote {out_json}")
    print(f"wrote {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
