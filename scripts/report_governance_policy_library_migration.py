#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from spec_runner.doc_parser import iter_spec_doc_tests


def _is_library_backed(harness: dict[str, Any]) -> bool:
    spec_lang = harness.get("spec_lang")
    if not isinstance(spec_lang, dict):
        return False
    paths = spec_lang.get("library_paths")
    return isinstance(paths, list) and any(isinstance(x, str) and x.strip() for x in paths)


def _classify_policy(policy: Any, check_id: str) -> str:
    if isinstance(policy, list) and len(policy) == 1 and isinstance(policy[0], dict):
        first = policy[0]
        call = first.get("call")
        if isinstance(call, list) and len(call) >= 2:
            callee = call[0]
            if isinstance(callee, dict):
                var = callee.get("var")
                if isinstance(var, list) and var and var[0] == "policy.pass_when_no_violations":
                    return "no_violations_pass_policy"
    if "non_regression" in check_id:
        return "metric_non_regression_policy"
    if any(tok in check_id for tok in ("naming.", "runtime.", "docs.", "conformance.")):
        return "path_or_token_policy"
    return "special_case_custom_policy"


def report(cases_dir: Path) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    counts: dict[str, int] = {}
    for case in iter_spec_doc_tests(cases_dir, file_pattern="*.spec.md"):
        t = case.test
        if str(t.get("type", "")).strip() != "governance.check":
            continue
        harness = t.get("harness")
        if not isinstance(harness, dict):
            harness = {}
        check_id = str(t.get("check", "")).strip()
        policy = harness.get("policy_evaluate")
        category = _classify_policy(policy, check_id)
        counts[category] = counts.get(category, 0) + 1
        rows.append(
            {
                "id": str(t.get("id", "")).strip(),
                "check": check_id,
                "file": str(case.doc_path).replace("\\", "/"),
                "library_backed": _is_library_backed(harness),
                "category": category,
            }
        )
    rows.sort(key=lambda r: (r["category"], r["check"], r["id"], r["file"]))
    total = len(rows)
    backed = sum(1 for r in rows if r["library_backed"])
    return {
        "version": 1,
        "summary": {
            "total_governance_cases": total,
            "library_backed_cases": backed,
            "library_backed_ratio": (float(backed) / float(total)) if total else 0.0,
            "categories": counts,
        },
        "cases": rows,
    }


def _to_md(payload: dict[str, Any]) -> str:
    s = payload.get("summary", {})
    lines = [
        "# Governance Policy Library Migration",
        "",
        f"- total_governance_cases: `{s.get('total_governance_cases', 0)}`",
        f"- library_backed_cases: `{s.get('library_backed_cases', 0)}`",
        f"- library_backed_ratio: `{s.get('library_backed_ratio', 0.0):.6f}`",
        "",
        "## Categories",
    ]
    cats = s.get("categories", {})
    if isinstance(cats, dict):
        for k in sorted(cats):
            lines.append(f"- `{k}`: `{cats[k]}`")
    lines.append("")
    lines.append("## Non Library-Backed Cases")
    missing = [r for r in payload.get("cases", []) if not r.get("library_backed")]
    if not missing:
        lines.append("- none")
    else:
        for row in missing:
            lines.append(f"- `{row['id']}` | `{row['check']}` | `{row['file']}`")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Report governance policy library migration coverage.")
    parser.add_argument("--cases", default="docs/spec/governance/cases", help="Governance cases directory")
    parser.add_argument(
        "--out-json",
        default=".artifacts/governance-policy-library-migration.json",
        help="Output JSON path",
    )
    parser.add_argument(
        "--out-md",
        default=".artifacts/governance-policy-library-migration-summary.md",
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
