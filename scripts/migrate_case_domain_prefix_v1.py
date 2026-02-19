#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from spec_runner.spec_domain import normalize_case_domain, normalize_export_symbol

FENCE_RE = re.compile(r"```yaml contract-spec\n(.*?)\n```", re.DOTALL)


@dataclass(frozen=True)
class ExportRename:
    file: Path
    case_id: str
    old: str
    new: str
    domain: str


def _infer_domain(path: Path) -> str | None:
    parts = path.as_posix().split("/")
    if "specs" not in parts:
        return None
    try:
        idx = parts.index("libraries")
    except ValueError:
        return None
    if idx + 1 >= len(parts):
        return None
    candidate = parts[idx + 1].strip()
    if not candidate:
        return None
    return candidate


def _iter_var_nodes(node: Any):
    if isinstance(node, dict):
        if "var" in node:
            yield node
        for value in node.values():
            yield from _iter_var_nodes(value)
    elif isinstance(node, list):
        for value in node:
            yield from _iter_var_nodes(value)


def _rewrite_case_refs(case: dict[str, Any], rename_map: dict[str, str]) -> int:
    rewrites = 0
    harness = case.get("harness")
    if isinstance(harness, dict):
        use = harness.get("use")
        if isinstance(use, list):
            for item in use:
                if not isinstance(item, dict):
                    continue
                symbols = item.get("symbols")
                if not isinstance(symbols, list):
                    continue
                for idx, raw in enumerate(symbols):
                    symbol = str(raw).strip()
                    if symbol in rename_map:
                        symbols[idx] = rename_map[symbol]
                        rewrites += 1
        spec_lang = harness.get("spec_lang")
        if isinstance(spec_lang, dict):
            exports = spec_lang.get("exports")
            if isinstance(exports, list):
                for idx, raw in enumerate(exports):
                    symbol = str(raw).strip()
                    if symbol in rename_map:
                        exports[idx] = rename_map[symbol]
                        rewrites += 1

    contract = case.get("contract")
    if isinstance(contract, dict):
        steps = contract.get("steps")
        if isinstance(steps, list):
            for step in steps:
                if not isinstance(step, dict):
                    continue
                assert_node = step.get("assert")
                for var_node in _iter_var_nodes(assert_node):
                    symbol = var_node.get("var")
                    if isinstance(symbol, str) and symbol in rename_map:
                        var_node["var"] = rename_map[symbol]
                        rewrites += 1
    return rewrites


def _dump_case(case: dict[str, Any]) -> str:
    return yaml.safe_dump(case, sort_keys=False, allow_unicode=False).rstrip()


def _collect_renames(case: dict[str, Any], *, doc_path: Path, explicit_domain: str | None) -> tuple[list[ExportRename], str | None]:
    if str(case.get("type", "")).strip() != "contract.export":
        return [], None
    if case.get("domain") is not None:
        return [], None
    harness = case.get("harness")
    exports = harness.get("exports") if isinstance(harness, dict) else None
    if not isinstance(exports, list):
        return [], None
    domain = explicit_domain or _infer_domain(doc_path)
    if not domain:
        return [], None
    domain = normalize_case_domain(domain)
    case_id = str(case.get("id", "")).strip() or "<unknown>"
    out: list[ExportRename] = []
    for item in exports:
        if not isinstance(item, dict):
            continue
        raw_as = str(item.get("as", "")).strip()
        if not raw_as:
            continue
        canonical = normalize_export_symbol(domain, raw_as)
        if canonical != raw_as:
            out.append(ExportRename(file=doc_path, case_id=case_id, old=raw_as, new=canonical, domain=domain))
    return out, domain


def _rewrite_file(path: Path, *, rename_map: dict[str, str], explicit_domain: str | None, write: bool) -> tuple[int, int, list[str]]:
    text = path.read_text(encoding="utf-8")
    rewrites = 0
    changed_blocks = 0
    unresolved: list[str] = []

    def repl(match: re.Match[str]) -> str:
        nonlocal rewrites, changed_blocks
        block = match.group(1)
        case = yaml.safe_load(block)
        if not isinstance(case, dict):
            return match.group(0)
        case_changed = False
        file_renames, inferred_domain = _collect_renames(case, doc_path=path, explicit_domain=explicit_domain)
        if str(case.get("type", "")).strip() == "contract.export" and case.get("domain") is None:
            if inferred_domain:
                case["domain"] = inferred_domain
                case_changed = True
                changed_blocks += 1
            else:
                cid = str(case.get("id", "")).strip() or "<unknown>"
                unresolved.append(f"{path.as_posix()}: case {cid}: unable to infer domain (pass --domain)")

        rewrites += _rewrite_case_refs(case, rename_map)
        if rewrites > 0:
            case_changed = True

        if not case_changed:
            return match.group(0)
        return "```yaml contract-spec\n" + _dump_case(case) + "\n```"

    updated = FENCE_RE.sub(repl, text)
    if write and updated != text:
        path.write_text(updated, encoding="utf-8")
    return changed_blocks, rewrites, unresolved


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Report or apply root domain export-prefix migration for contract.export cases.")
    ap.add_argument("paths", nargs="*", default=["specs"])
    ap.add_argument("--domain", default=None, help="Explicit domain to apply when adding root domain.")
    ap.add_argument("--check", action="store_true", help="Report-only mode; exits 1 when migration is needed.")
    ap.add_argument("--write", action="store_true", help="Apply rewrites in place.")
    ns = ap.parse_args(argv)

    if ns.check and ns.write:
        print("ERROR: choose either --check or --write")
        return 2

    explicit_domain: str | None = None
    if ns.domain is not None:
        try:
            explicit_domain = normalize_case_domain(ns.domain)
        except (TypeError, ValueError) as exc:
            print(f"ERROR: invalid --domain ({exc})")
            return 2

    spec_files: list[Path] = []
    for raw in ns.paths:
        p = Path(raw)
        if p.is_file() and p.name.endswith(".spec.md"):
            spec_files.append(p)
        elif p.exists():
            spec_files.extend(sorted(x for x in p.rglob("*.spec.md") if x.is_file()))

    rename_records: list[ExportRename] = []
    unresolved: list[str] = []
    for path in spec_files:
        text = path.read_text(encoding="utf-8")
        for match in FENCE_RE.finditer(text):
            case = yaml.safe_load(match.group(1))
            if not isinstance(case, dict):
                continue
            renames, domain = _collect_renames(case, doc_path=path, explicit_domain=explicit_domain)
            rename_records.extend(renames)
            if str(case.get("type", "")).strip() == "contract.export" and case.get("domain") is None and domain is None:
                cid = str(case.get("id", "")).strip() or "<unknown>"
                unresolved.append(f"{path.as_posix()}: case {cid}: unable to infer domain (pass --domain)")

    rename_map = {r.old: r.new for r in rename_records}
    changed_blocks_total = 0
    rewrites_total = 0
    if ns.write:
        for path in spec_files:
            changed_blocks, rewrites, file_unresolved = _rewrite_file(
                path,
                rename_map=rename_map,
                explicit_domain=explicit_domain,
                write=True,
            )
            changed_blocks_total += changed_blocks
            rewrites_total += rewrites
            unresolved.extend(file_unresolved)

    if rename_records:
        print("planned export renames:")
        for row in rename_records:
            print(
                f"- {row.file.as_posix()}: case {row.case_id}: {row.old} -> {row.new} (domain={row.domain})"
            )
    if unresolved:
        print("unresolved cases:")
        for line in sorted(set(unresolved)):
            print(f"- {line}")

    if ns.check:
        if rename_records or unresolved:
            return 1
        print("OK: no domain-prefix migration required")
        return 0

    if ns.write:
        print(f"updated contract.export domain blocks: {changed_blocks_total}")
        print(f"rewritten symbol references: {rewrites_total}")
        if unresolved:
            return 1
        return 0

    print("No mode selected. Use --check or --write.")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
