#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

import yaml


_FENCE_RE = re.compile(r"```yaml spec-test\n(.*?)\n```", re.DOTALL)


def _iter_files(path: Path):
    if path.is_file():
        if path.suffix == ".md":
            yield path
        return
    if path.is_dir():
        for p in sorted(path.rglob("*.md")):
            if p.is_file():
                yield p


def _split_ref(raw_ref: str) -> tuple[str | None, str | None]:
    ref = str(raw_ref).strip()
    if "#" in ref:
        path, frag = ref.split("#", 1)
        return (path.strip() or None), (frag.strip() or None)
    return (ref or None), None


def _expand_entries(raw_entries: Any) -> list[dict[str, Any]]:
    if not isinstance(raw_entries, list):
        return []
    out: list[dict[str, Any]] = []
    for raw in raw_entries:
        if not isinstance(raw, dict):
            continue
        if "symbols" in raw:
            from_source = str(raw.get("from", "")).strip()
            required = bool(raw.get("required", True))
            prefix = str(raw.get("prefix", "")).strip()
            symbols = raw.get("symbols")
            if not isinstance(symbols, list):
                continue
            for sym in symbols:
                name = str(sym).strip()
                if not name:
                    continue
                full = f"{prefix}.{name}" if prefix else name
                out.append(
                    {
                        "as": full,
                        "from": from_source,
                        "path": f"/{full.lstrip('/')}",
                        "required": required,
                    }
                )
            continue
        name = str(raw.get("as", "")).strip()
        if not name:
            continue
        item: dict[str, Any] = {
            "as": name,
            "from": str(raw.get("from", "")).strip(),
            "path": str(raw.get("path", "")).strip(),
            "required": bool(raw.get("required", True)),
        }
        if "params" in raw:
            item["params"] = raw.get("params")
        out.append(item)
    return out


def _load_cases(doc_path: Path) -> list[tuple[str, dict[str, Any]]]:
    text = doc_path.read_text(encoding="utf-8")
    out: list[tuple[str, dict[str, Any]]] = []
    for m in _FENCE_RE.finditer(text):
        block = m.group(1)
        try:
            case = yaml.safe_load(block)
        except Exception:
            continue
        if isinstance(case, dict):
            out.append((block, case))
    return out


def _rewrite_doc(text: str, mutate_case) -> tuple[str, bool]:
    out: list[str] = []
    last = 0
    changed = False
    for m in _FENCE_RE.finditer(text):
        out.append(text[last : m.start(1)])
        block = m.group(1)
        try:
            case = yaml.safe_load(block)
        except Exception:
            out.append(block)
            last = m.end(1)
            continue
        if not isinstance(case, dict):
            out.append(block)
            last = m.end(1)
            continue
        updated = mutate_case(case)
        if updated:
            changed = True
            out.append(yaml.safe_dump(case, sort_keys=False).rstrip("\n"))
        else:
            out.append(block)
        last = m.end(1)
    out.append(text[last:])
    return "".join(out), changed


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Move consumer step exports/imports to producer harness.chain.exports.")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    ap.add_argument("paths", nargs="+")
    ns = ap.parse_args(argv)

    repo_root = Path(__file__).resolve().parents[1]
    changed_docs: set[Path] = set()

    # First pass: collect moved exports keyed by producer doc/case.
    moved: dict[tuple[Path, str | None], list[dict[str, Any]]] = {}
    consumer_files: list[Path] = []
    for raw in ns.paths:
        for doc in _iter_files(Path(raw)):
            consumer_files.append(doc)
            text = doc.read_text(encoding="utf-8")
            for m in _FENCE_RE.finditer(text):
                try:
                    case = yaml.safe_load(m.group(1))
                except Exception:
                    continue
                if not isinstance(case, dict):
                    continue
                harness = case.get("harness")
                if not isinstance(harness, dict):
                    continue
                chain = harness.get("chain")
                if not isinstance(chain, dict):
                    continue
                steps = chain.get("steps")
                if not isinstance(steps, list):
                    continue
                for step in steps:
                    if not isinstance(step, dict):
                        continue
                    raw_entries = step.get("exports")
                    if raw_entries is None:
                        raw_entries = step.get("imports")
                    entries = _expand_entries(raw_entries)
                    if not entries:
                        continue
                    ref_path, ref_case = _split_ref(str(step.get("ref", "")).strip())
                    if not ref_path:
                        producer_doc = doc
                    else:
                        producer_doc = (repo_root / ref_path.lstrip("/")).resolve()
                    moved.setdefault((producer_doc, ref_case), []).extend(entries)

    # Second pass: remove step-level declarations from consumers.
    for doc in consumer_files:
        original = doc.read_text(encoding="utf-8")

        def _mutate_consumer(case: dict[str, Any]) -> bool:
            harness = case.get("harness")
            if not isinstance(harness, dict):
                return False
            chain = harness.get("chain")
            if not isinstance(chain, dict):
                return False
            steps = chain.get("steps")
            if not isinstance(steps, list):
                return False
            touched = False
            for step in steps:
                if not isinstance(step, dict):
                    continue
                if "imports" in step:
                    del step["imports"]
                    touched = True
                if "exports" in step:
                    del step["exports"]
                    touched = True
            return touched

        updated, changed = _rewrite_doc(original, _mutate_consumer)
        if changed:
            changed_docs.add(doc)
            if ns.write:
                doc.write_text(updated, encoding="utf-8")

    # Third pass: inject producer harness.chain.exports
    for (producer_doc, producer_case_id), entries in moved.items():
        if not producer_doc.exists():
            continue
        original = producer_doc.read_text(encoding="utf-8")

        def _mutate_producer(case: dict[str, Any]) -> bool:
            if producer_case_id and str(case.get("id", "")).strip() != producer_case_id:
                return False
            harness = case.get("harness")
            if not isinstance(harness, dict):
                harness = {}
                case["harness"] = harness
            chain = harness.get("chain")
            if not isinstance(chain, dict):
                chain = {}
                harness["chain"] = chain
            exports = chain.get("exports")
            if not isinstance(exports, list):
                exports = []
                chain["exports"] = exports
            seen = {str(x.get("as", "")).strip() for x in exports if isinstance(x, dict)}
            touched = False
            for item in entries:
                name = str(item.get("as", "")).strip()
                if not name or name in seen:
                    continue
                payload = {
                    "as": name,
                    "from": "assert.function",
                    "path": str(item.get("path", "")).strip(),
                    "required": bool(item.get("required", True)),
                }
                params = item.get("params")
                if params is not None:
                    payload["params"] = params
                exports.append(payload)
                seen.add(name)
                touched = True
            return touched

        updated, changed = _rewrite_doc(original, _mutate_producer)
        if changed:
            changed_docs.add(producer_doc)
            if ns.write:
                producer_doc.write_text(updated, encoding="utf-8")

    if ns.check:
        if changed_docs:
            for p in sorted(changed_docs):
                print(f"{p.as_posix()}: producer-export migration drift")
            return 1
        print("OK: producer-owned exports are canonical")
        return 0

    print(f"OK: rewrote {len(changed_docs)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

