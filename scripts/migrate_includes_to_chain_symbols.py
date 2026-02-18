#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

import yaml

from spec_runner.codecs import load_external_cases
from spec_runner.virtual_paths import contract_root_for, resolve_contract_path


_FENCE = re.compile(r"```yaml contract-spec\n(.*?)\n```", re.DOTALL)


def _iter_files(path: Path):
    if path.is_file():
        if path.suffix == ".md":
            yield path
        return
    if path.is_dir():
        for p in sorted(path.rglob("*.md")):
            if p.is_file():
                yield p


def _dump_case(case: dict[str, Any]) -> str:
    return yaml.safe_dump(case, sort_keys=False, allow_unicode=False).rstrip("\n")


def _public_symbols_for_library(path: Path) -> list[str]:
    out: list[str] = []
    loaded = load_external_cases(path, formats={"md", "yaml", "json"})
    for _doc_path, case in loaded:
        if str(case.get("type", "")).strip() != "spec_lang.export":
            continue
        defines = case.get("defines")
        if not isinstance(defines, dict):
            continue
        public = defines.get("public")
        if not isinstance(public, dict):
            continue
        for name in public.keys():
            sym = str(name).strip()
            if sym:
                out.append(sym)
    seen: set[str] = set()
    ordered: list[str] = []
    for sym in out:
        if sym in seen:
            continue
        seen.add(sym)
        ordered.append(sym)
    return ordered


def _next_step_id(existing: set[str], seed: str) -> str:
    base = re.sub(r"[^a-z0-9]+", "_", seed.lower()).strip("_") or "lib"
    cand = f"lib_{base}"
    i = 1
    while cand in existing:
        i += 1
        cand = f"lib_{base}_{i}"
    existing.add(cand)
    return cand


def _doc_contract_root(doc_path: Path) -> Path:
    resolved = doc_path.resolve()
    cur = resolved.parent if resolved.is_file() else resolved
    for candidate in (cur, *cur.parents):
        if (candidate / "docs/spec").exists():
            return candidate
    return contract_root_for(doc_path)


def _migrate_case(case: dict[str, Any], *, doc_path: Path) -> tuple[dict[str, Any], bool]:
    case_type = str(case.get("type", "")).strip()
    if case_type == "spec_lang.export":
        return case, False
    harness = case.get("harness")
    if not isinstance(harness, dict):
        return case, False
    spec_lang = harness.get("spec_lang")
    if not isinstance(spec_lang, dict):
        return case, False
    includes = spec_lang.get("includes")
    if not isinstance(includes, list) or not includes:
        return case, False

    export_allow_raw = spec_lang.get("exports")
    export_allow: set[str] = set()
    if isinstance(export_allow_raw, list):
        export_allow = {str(x).strip() for x in export_allow_raw if str(x).strip()}

    chain = harness.get("chain")
    if chain is None:
        chain = {}
    if not isinstance(chain, dict):
        raise ValueError("harness.chain must be mapping when present")
    steps = chain.get("steps")
    if steps is None:
        steps = []
    if not isinstance(steps, list):
        raise ValueError("harness.chain.steps must be list when present")
    imports = chain.get("imports")
    if imports is None:
        imports = []
    if not isinstance(imports, list):
        raise ValueError("harness.chain.imports must be list when present")

    existing_step_ids = {
        str(s.get("id", "")).strip()
        for s in steps
        if isinstance(s, dict) and str(s.get("id", "")).strip()
    }
    root = _doc_contract_root(doc_path)
    changed = False

    for raw_inc in includes:
        inc = str(raw_inc).strip()
        if not inc:
            continue
        if inc.startswith("external://"):
            continue
        resolved = resolve_contract_path(root, inc, field="harness.spec_lang.includes")
        symbols = _public_symbols_for_library(resolved)
        if export_allow:
            symbols = [s for s in symbols if s in export_allow]
        if not symbols:
            continue
        step_id = _next_step_id(existing_step_ids, Path(inc).stem)
        exports = [
            {
                "from": "library.symbol",
                "required": True,
                "symbols": symbols,
            }
        ]
        steps.append(
            {
                "id": step_id,
                "class": "must",
                "ref": inc,
                "exports": exports,
            }
        )
        imports.append(
            {
                "from": step_id,
                "names": symbols,
            }
        )
        changed = True

    if not changed:
        return case, False

    spec_lang.pop("includes", None)
    spec_lang.pop("exports", None)
    if not spec_lang:
        harness.pop("spec_lang", None)
    chain["steps"] = steps
    chain["imports"] = imports
    harness["chain"] = chain
    case["harness"] = harness
    return case, True


def _rewrite(text: str, *, doc_path: Path) -> tuple[str, bool]:
    cursor = 0
    out: list[str] = []
    changed = False
    for m in _FENCE.finditer(text):
        out.append(text[cursor:m.start()])
        raw_block = m.group(1)
        try:
            case = yaml.safe_load(raw_block)
        except Exception:
            out.append(m.group(0))
            cursor = m.end()
            continue
        if not isinstance(case, dict):
            out.append(m.group(0))
            cursor = m.end()
            continue
        updated_case, did_change = _migrate_case(case, doc_path=doc_path)
        if did_change:
            changed = True
            out.append("```yaml contract-spec\n" + _dump_case(updated_case) + "\n```")
        else:
            out.append(m.group(0))
        cursor = m.end()
    out.append(text[cursor:])
    return "".join(out), changed


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Migrate executable harness.spec_lang.includes to harness.chain symbol steps.")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    ap.add_argument("paths", nargs="+", help="file or directory paths")
    ns = ap.parse_args(argv)

    changed: list[Path] = []
    for raw in ns.paths:
        p = Path(raw)
        for f in _iter_files(p):
            original = f.read_text(encoding="utf-8")
            updated, did_change = _rewrite(original, doc_path=f)
            if did_change and updated != original:
                changed.append(f)
                if ns.write:
                    f.write_text(updated, encoding="utf-8")

    if ns.check:
        if changed:
            for f in changed:
                print(f"{f.as_posix()}: includes-to-chain migration drift")
            return 1
        print("OK: executable cases are chain-first for library symbol loading")
        return 0

    print(f"OK: rewrote {len(changed)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
