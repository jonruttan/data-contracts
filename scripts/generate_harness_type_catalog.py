#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from spec_runner.docs_generators import (
    parse_generated_block,
    replace_generated_block,
    write_json,
)
from spec_runner.schema_registry import compile_registry


def _resolve_cli_path(repo_root: Path, raw: str) -> Path:
    path = Path(raw)
    if path.is_absolute():
        return path
    return repo_root / str(raw).lstrip("/")


def _build_payload(repo_root: Path) -> dict[str, Any]:
    compiled, errs = compile_registry(repo_root)
    if compiled is None:
        raise ValueError("; ".join(errs))
    profiles = dict(compiled.get("type_profiles") or {})
    rows: list[dict[str, Any]] = []
    for case_type, prof in sorted(profiles.items()):
        fields = sorted(dict(prof.get("fields") or {}).keys())
        rows.append(
            {
                "case_type": case_type,
                "field_count": len(fields),
                "fields": fields,
                "required_top_level": list(prof.get("required_top_level") or []),
                "allowed_top_level_extra": list(prof.get("allowed_top_level_extra") or []),
            }
        )
    return {
        "version": 1,
        "summary": {
            "type_profile_count": len(rows),
            "total_type_field_count": sum(int(r.get("field_count", 0)) for r in rows),
        },
        "type_profiles": rows,
    }


def _render_md(payload: dict[str, Any]) -> str:
    summary = dict(payload.get("summary") or {})
    lines = [
        "## Generated Harness Type Catalog",
        "",
        f"- type_profile_count: {int(summary.get('type_profile_count', 0))}",
        f"- total_type_field_count: {int(summary.get('total_type_field_count', 0))}",
        "",
        "| case_type | field_count | required_top_level | allowed_top_level_extra |",
        "|---|---|---|---|",
    ]
    for row in payload.get("type_profiles") or []:
        req = ", ".join(f"`{x}`" for x in row.get("required_top_level") or []) or "-"
        extra = ", ".join(f"`{x}`" for x in row.get("allowed_top_level_extra") or []) or "-"
        lines.append(
            f"| `{row.get('case_type', '')}` | {int(row.get('field_count', 0))} | {req} | {extra} |"
        )
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Generate harness type catalog from schema registry.")
    ap.add_argument("--out", default=".artifacts/harness-type-catalog.json")
    ap.add_argument("--doc-out", default="docs/book/92_appendix_harness_type_reference.md")
    ap.add_argument("--check", action="store_true")
    ns = ap.parse_args(argv)

    repo_root = Path(__file__).resolve().parents[1]
    payload = _build_payload(repo_root)
    out_path = _resolve_cli_path(repo_root, str(ns.out))
    doc_path = _resolve_cli_path(repo_root, str(ns.doc_out))
    md_block = _render_md(payload)
    updated_doc = replace_generated_block(
        doc_path.read_text(encoding="utf-8"),
        surface_id="harness_type_catalog",
        body=md_block,
    )

    import json

    expected_json = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if ns.check:
        if parse_generated_block(doc_path.read_text(encoding="utf-8"), surface_id="harness_type_catalog").strip() != md_block.strip():
            print(f"{ns.doc_out}: generated content out of date")
            return 1
        if out_path.exists() and out_path.read_text(encoding="utf-8") != expected_json:
            print(f"{ns.out}: generated content out of date")
            return 1
        return 0

    write_json(out_path, payload)
    doc_path.write_text(updated_doc, encoding="utf-8")
    print(f"wrote {ns.out}")
    print(f"wrote {ns.doc_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
