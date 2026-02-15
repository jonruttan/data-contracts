#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from spec_runner.schema_registry import compile_registry, write_compiled_registry_artifact


def _render_md(payload: dict) -> str:
    summary = payload.get("summary") or {}
    lines = [
        "# Schema Registry Report",
        "",
        f"- profile_count: {int(summary.get('profile_count', 0))}",
        f"- top_level_field_count: {int(summary.get('top_level_field_count', 0))}",
        f"- type_profile_count: {int(summary.get('type_profile_count', 0))}",
        f"- errors: {int(summary.get('error_count', 0))}",
        "",
    ]
    errors = payload.get("errors") or []
    if errors:
        lines += ["## Errors", ""]
        for e in errors:
            lines.append(f"- {e}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Emit schema registry compiled report.")
    ap.add_argument("--out", default=".artifacts/schema_registry_report.md")
    ap.add_argument("--format", choices=("json", "md"), default="md")
    ap.add_argument("--check", action="store_true")
    ns = ap.parse_args(argv)

    repo_root = Path(__file__).resolve().parents[1]
    compiled, errs = compile_registry(repo_root)
    payload = {
        "version": 1,
        "summary": {
            "profile_count": int(compiled.get("profile_count", 0)) if compiled else 0,
            "top_level_field_count": len((compiled or {}).get("top_level_fields") or {}),
            "type_profile_count": len((compiled or {}).get("type_profiles") or {}),
            "error_count": len(errs),
        },
        "errors": errs,
    }
    if compiled:
        payload["compiled"] = compiled

    if compiled:
        write_compiled_registry_artifact(repo_root, compiled)
    raw = _render_md(payload) if ns.format == "md" else json.dumps(payload, indent=2, sort_keys=True) + "\n"
    out = Path(str(ns.out))
    out.parent.mkdir(parents=True, exist_ok=True)
    if ns.check:
        if not out.exists():
            print(f"{out}: missing report artifact")
            return 1
        if out.read_text(encoding="utf-8") != raw:
            print(f"{out}: stale report artifact")
            return 1
        print("OK: schema registry report is up to date")
        return 0
    out.write_text(raw, encoding="utf-8")
    print(f"wrote {out}")
    return 0 if not errs else 1


if __name__ == "__main__":
    raise SystemExit(main())
