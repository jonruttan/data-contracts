#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HARNESS_FILES = (
    "spec_runner/harnesses/text_file.py",
    "spec_runner/harnesses/cli_run.py",
    "spec_runner/harnesses/orchestration_run.py",
    "spec_runner/harnesses/docs_generate.py",
    "spec_runner/harnesses/api_http.py",
)
REQUIRED_COMPONENT_TOKENS = (
    "build_execution_context(",
    "run_assertions_with_context(",
    "resolve_subject_for_target(",
)
LEGACY_WORKFLOW_TOKENS = (
    "compile_import_bindings(",
    "limits_from_harness(",
    "load_spec_lang_symbols_for_case(",
    "evaluate_internal_assert_tree(",
)


def _line_for(text: str, token: str) -> int:
    idx = text.find(token)
    if idx < 0:
        return 1
    return text[:idx].count("\n") + 1


def build_report() -> dict[str, object]:
    rows: list[dict[str, object]] = []
    componentized = 0
    duplicated = 0
    for rel in HARNESS_FILES:
        p = ROOT / rel
        text = p.read_text(encoding="utf-8") if p.exists() else ""
        required_missing = [tok for tok in REQUIRED_COMPONENT_TOKENS if tok not in text]
        legacy_hits = [
            {"token": tok, "line": _line_for(text, tok)}
            for tok in LEGACY_WORKFLOW_TOKENS
            if tok in text
        ]
        is_componentized = p.exists() and not required_missing
        if is_componentized:
            componentized += 1
        if legacy_hits:
            duplicated += 1
        rows.append(
            {
                "path": rel,
                "exists": p.exists(),
                "componentized": is_componentized,
                "required_missing": required_missing,
                "legacy_hits": legacy_hits,
            }
        )
    summary = {
        "harness_count": len(HARNESS_FILES),
        "componentized_count": componentized,
        "legacy_duplication_file_count": duplicated,
    }
    return {"summary": summary, "harnesses": rows}


def _render_summary_md(payload: dict[str, object]) -> str:
    summary = payload.get("summary") or {}
    rows = payload.get("harnesses") or []
    lines = [
        "# Harness Component Surface",
        "",
        f"- harness_count: {summary.get('harness_count', 0)}",
        f"- componentized_count: {summary.get('componentized_count', 0)}",
        f"- legacy_duplication_file_count: {summary.get('legacy_duplication_file_count', 0)}",
        "",
        "| harness | componentized | missing required tokens | legacy hits |",
        "|---|---:|---|---:|",
    ]
    for row in rows:
        if not isinstance(row, dict):
            continue
        missing = ", ".join(row.get("required_missing") or []) or "-"
        legacy_hits = row.get("legacy_hits") or []
        lines.append(
            f"| `{row.get('path')}` | {'yes' if row.get('componentized') else 'no'} | {missing} | {len(legacy_hits)} |"
        )
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=".artifacts/harness-component-surface.json")
    ap.add_argument("--summary-out", default=".artifacts/harness-component-surface-summary.md")
    ns = ap.parse_args(argv)
    payload = build_report()
    out = ROOT / str(ns.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    summary_out = ROOT / str(ns.summary_out)
    summary_out.parent.mkdir(parents=True, exist_ok=True)
    summary_out.write_text(_render_summary_md(payload), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

