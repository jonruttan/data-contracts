#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import yaml

from spec_runner.codecs import load_external_cases


def _render_markdown(cases: list[dict[str, Any]]) -> str:
    parts: list[str] = []
    for case in cases:
        cid = str(case.get("id", "")).strip() or "CASE"
        parts.append(f"## {cid}\n")
        parts.append("```yaml contract-spec\n")
        parts.append(yaml.safe_dump(case, sort_keys=False, allow_unicode=False))
        parts.append("```\n")
    return "\n".join(parts)


def _write_cases(cases: list[dict[str, Any]], out_path: Path, out_format: str) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_format == "json":
        payload: Any = cases[0] if len(cases) == 1 else cases
        out_path.write_text(json.dumps(payload, indent=2, sort_keys=False) + "\n", encoding="utf-8")
        return
    if out_format == "yaml":
        payload = cases[0] if len(cases) == 1 else cases
        out_path.write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=False), encoding="utf-8")
        return
    if out_format == "md":
        out_path.write_text(_render_markdown(cases), encoding="utf-8")
        return
    raise ValueError(f"unsupported out format: {out_format}")


def _infer_format(path: Path) -> str:
    name = path.name
    if name.endswith(".spec.md") or name.endswith(".md"):
        return "md"
    if name.endswith(".spec.yaml") or name.endswith(".spec.yml") or name.endswith(".yaml") or name.endswith(".yml"):
        return "yaml"
    if name.endswith(".spec.json") or name.endswith(".json"):
        return "json"
    raise ValueError("cannot infer output format from file extension")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Convert spec case docs across md/yaml/json external formats.")
    ap.add_argument("--in", dest="in_path", required=True, help="Input case file or directory")
    ap.add_argument("--out", dest="out_path", required=True, help="Output file path")
    ap.add_argument("--out-format", choices=["md", "yaml", "json"], default=None)
    ap.add_argument(
        "--formats",
        default="md,yaml,json",
        help="Comma-separated input formats to load (default: md,yaml,json)",
    )
    ns = ap.parse_args(argv)

    in_path = Path(str(ns.in_path))
    out_path = Path(str(ns.out_path))
    if not in_path.exists():
        print(f"ERROR: input path does not exist: {in_path}", file=sys.stderr)
        return 2

    formats = {x.strip() for x in str(ns.formats).split(",") if x.strip()}
    if not formats:
        print("ERROR: --formats requires at least one format", file=sys.stderr)
        return 2

    cases = [case for _doc, case in load_external_cases(in_path, formats=formats)]
    if not cases:
        print("ERROR: no cases loaded", file=sys.stderr)
        return 2

    out_format = str(ns.out_format).strip() if ns.out_format else _infer_format(out_path)
    try:
        _write_cases(cases, out_path=out_path, out_format=out_format)
    except Exception as e:  # noqa: BLE001
        print(f"ERROR: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
