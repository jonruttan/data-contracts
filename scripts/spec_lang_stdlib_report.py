#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from spec_runner.spec_lang_stdlib_profile import spec_lang_stdlib_report_jsonable


def _to_markdown(payload: dict) -> str:
    summary = payload.get("summary") or {}
    lines = [
        "# Spec-Lang Stdlib Profile Report",
        "",
        f"- profile symbols: {int(summary.get('profile_symbol_count', 0))}",
        f"- python symbols: {int(summary.get('python_symbol_count', 0))}",
        f"- php symbols: {int(summary.get('php_symbol_count', 0))}",
        f"- missing in python: {int(summary.get('missing_in_python_count', 0))}",
        f"- missing in php: {int(summary.get('missing_in_php_count', 0))}",
        f"- arity mismatch: {int(summary.get('arity_mismatch_count', 0))}",
        f"- docs sync missing: {int(summary.get('docs_sync_missing_count', 0))}",
        "",
    ]
    for key in ("missing_in_python", "missing_in_php", "arity_mismatch", "docs_sync_missing", "errors"):
        vals = payload.get(key) or []
        if vals:
            lines.append(f"## {key.replace('_', ' ').title()}")
            lines.append("")
            for item in vals:
                lines.append(f"- {item}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Emit spec-lang stdlib profile completeness/parity report.")
    ap.add_argument("--out", help="Optional output path.")
    ap.add_argument("--format", choices=("json", "md"), default="json")
    ns = ap.parse_args(argv)

    repo_root = Path(__file__).resolve().parents[1]
    payload = spec_lang_stdlib_report_jsonable(repo_root)
    raw = _to_markdown(payload) if ns.format == "md" else json.dumps(payload, indent=2, sort_keys=True) + "\n"

    if ns.out:
        out = Path(ns.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(raw, encoding="utf-8")
        print(f"wrote {out}")
    else:
        print(raw, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
