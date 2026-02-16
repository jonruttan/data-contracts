#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import re
from typing import Any

from spec_runner.docs_generators import (
    parse_generated_block,
    replace_generated_block,
    write_json,
)
from spec_runner.spec_lang import _builtin_arity_table


def _resolve_cli_path(repo_root: Path, raw: str) -> Path:
    path = Path(raw)
    if path.is_absolute():
        return path
    return repo_root / str(raw).lstrip("/")


def _php_builtin_symbols(php_text: str) -> set[str]:
    out: set[str] = set()
    for m in re.finditer(r"if \(\$op === '([a-z0-9_.]+)'\)", php_text):
        out.add(m.group(1))
    for m in re.finditer(r"if \(in_array\(\$op,\s*\[([^\]]+)\]", php_text):
        body = m.group(1)
        for lit in re.finditer(r"'([a-z0-9_.]+)'", body):
            out.add(lit.group(1))
    return out


def _classify(name: str) -> str:
    if name.startswith("std."):
        parts = name.split(".")
        if len(parts) > 1:
            return parts[1]
    return "other"


def _build_payload(repo_root: Path) -> dict[str, Any]:
    py = _builtin_arity_table()
    php_text = (repo_root / "scripts/php/spec_runner.php").read_text(encoding="utf-8")
    php_syms = _php_builtin_symbols(php_text)
    builtins = []
    for name in sorted(py):
        builtins.append(
            {
                "symbol": name,
                "arity": int(py[name]),
                "category": _classify(name),
                "python_supported": True,
                "php_supported": name in php_syms,
                "parity": name in php_syms,
            }
        )
    return {
        "version": 1,
        "summary": {
            "builtin_count": len(builtins),
            "parity_count": sum(1 for x in builtins if bool(x.get("parity"))),
            "all_parity": all(bool(x.get("parity")) for x in builtins),
        },
        "builtins": builtins,
    }


def _render_md(payload: dict[str, Any]) -> str:
    summary = dict(payload.get("summary") or {})
    lines = [
        "## Generated Spec-Lang Builtin Catalog",
        "",
        f"- builtin_count: {int(summary.get('builtin_count', 0))}",
        f"- parity_count: {int(summary.get('parity_count', 0))}",
        f"- all_parity: {str(bool(summary.get('all_parity', False))).lower()}",
        "",
        "| symbol | arity | category | python | php | parity |",
        "|---|---|---|---|---|---|",
    ]
    for row in payload.get("builtins") or []:
        lines.append(
            f"| `{row.get('symbol', '')}` | {int(row.get('arity', 0))} | `{row.get('category', 'other')}` | "
            f"{str(bool(row.get('python_supported', False))).lower()} | "
            f"{str(bool(row.get('php_supported', False))).lower()} | "
            f"{str(bool(row.get('parity', False))).lower()} |"
        )
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Generate spec-lang builtin catalog and parity summary.")
    ap.add_argument("--out", default=".artifacts/spec-lang-builtin-catalog.json")
    ap.add_argument("--doc-out", default="docs/book/93_appendix_spec_lang_builtin_catalog.md")
    ap.add_argument("--check", action="store_true")
    ns = ap.parse_args(argv)

    repo_root = Path(__file__).resolve().parents[1]
    payload = _build_payload(repo_root)
    out_path = _resolve_cli_path(repo_root, str(ns.out))
    doc_path = _resolve_cli_path(repo_root, str(ns.doc_out))
    md_block = _render_md(payload)
    updated_doc = replace_generated_block(
        doc_path.read_text(encoding="utf-8"),
        surface_id="spec_lang_builtin_catalog",
        body=md_block,
    )

    import json

    expected_json = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if ns.check:
        if parse_generated_block(doc_path.read_text(encoding="utf-8"), surface_id="spec_lang_builtin_catalog").strip() != md_block.strip():
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
