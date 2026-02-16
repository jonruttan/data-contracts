#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
from typing import Any

from spec_runner.docs_generators import (
    parse_generated_block,
    replace_generated_block,
    write_json,
)


def _resolve_cli_path(repo_root: Path, raw: str) -> Path:
    path = Path(raw)
    if path.is_absolute():
        return path
    return repo_root / str(raw).lstrip("/")


def _parse_shell_case_labels(text: str) -> set[str]:
    labels: set[str] = set()
    for line in text.splitlines():
        m = re.match(r"\s{2}([a-z0-9_-]+)\)", line)
        if m:
            labels.add(m.group(1))
    return labels


def _parse_rust_subcommands(text: str) -> set[str]:
    labels: set[str] = set()
    for m in re.finditer(r'"([a-z0-9_-]+)"\s*=>', text):
        labels.add(m.group(1))
    return labels


def _build_payload(repo_root: Path) -> dict[str, Any]:
    python_text = (repo_root / "scripts/python/runner_adapter.sh").read_text(encoding="utf-8")
    rust_text = (repo_root / "scripts/rust/spec_runner_cli/src/main.rs").read_text(encoding="utf-8")
    public_text = (repo_root / "scripts/runner_adapter.sh").read_text(encoding="utf-8")

    python_cmds = _parse_shell_case_labels(python_text)
    rust_cmds = _parse_rust_subcommands(rust_text)
    public_impls = _parse_shell_case_labels(public_text)

    all_cmds = sorted(python_cmds.union(rust_cmds))
    rows: list[dict[str, Any]] = []
    for cmd in all_cmds:
        rows.append(
            {
                "command": cmd,
                "python_supported": cmd in python_cmds,
                "rust_supported": cmd in rust_cmds,
                "parity": cmd in python_cmds and cmd in rust_cmds,
            }
        )

    return {
        "version": 1,
        "summary": {
            "command_count": len(all_cmds),
            "python_command_count": len(python_cmds),
            "rust_command_count": len(rust_cmds),
            "parity_command_count": sum(1 for r in rows if bool(r.get("parity"))),
            "all_commands_parity": all(bool(r.get("parity")) for r in rows),
            "public_impl_modes": sorted(public_impls),
        },
        "commands": rows,
    }


def _render_md(payload: dict[str, Any]) -> str:
    summary = dict(payload.get("summary") or {})
    lines = [
        "## Generated Runner API Catalog",
        "",
        f"- command_count: {int(summary.get('command_count', 0))}",
        f"- python_command_count: {int(summary.get('python_command_count', 0))}",
        f"- rust_command_count: {int(summary.get('rust_command_count', 0))}",
        f"- parity_command_count: {int(summary.get('parity_command_count', 0))}",
        f"- all_commands_parity: {str(bool(summary.get('all_commands_parity', False))).lower()}",
        "",
        "| command | python | rust | parity |",
        "|---|---|---|---|",
    ]
    for row in payload.get("commands") or []:
        lines.append(
            f"| `{row.get('command', '')}` | "
            f"{str(bool(row.get('python_supported', False))).lower()} | "
            f"{str(bool(row.get('rust_supported', False))).lower()} | "
            f"{str(bool(row.get('parity', False))).lower()} |"
        )
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Generate runner API catalog JSON and markdown section.")
    ap.add_argument("--out", default=".artifacts/runner-api-catalog.json")
    ap.add_argument("--doc-out", default="docs/book/91_appendix_runner_api_reference.md")
    ap.add_argument("--check", action="store_true")
    ns = ap.parse_args(argv)

    repo_root = Path(__file__).resolve().parents[1]
    payload = _build_payload(repo_root)
    out_path = _resolve_cli_path(repo_root, str(ns.out))
    doc_path = _resolve_cli_path(repo_root, str(ns.doc_out))
    md_block = _render_md(payload)
    updated_doc = replace_generated_block(
        doc_path.read_text(encoding="utf-8"),
        surface_id="runner_api_catalog",
        body=md_block,
    )

    if ns.check:
        if (parse_generated_block(doc_path.read_text(encoding="utf-8"), surface_id="runner_api_catalog").strip()
                != md_block.strip()):
            print(f"{ns.doc_out}: generated content out of date")
            return 1
        if out_path.exists():
            expected_json = json.dumps(payload, indent=2, sort_keys=True).strip()
            if out_path.read_text(encoding="utf-8").strip() != expected_json:
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
