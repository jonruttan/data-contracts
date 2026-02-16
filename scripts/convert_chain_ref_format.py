#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def _iter_files(path: Path):
    if path.is_file():
        if path.suffix == ".md":
            yield path
        return
    if path.is_dir():
        for p in sorted(path.rglob("*.md")):
            if p.is_file():
                yield p


def _indent_width(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _rewrite(text: str) -> str:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped != "ref:":
            out.append(line)
            i += 1
            continue
        ref_indent = _indent_width(line)
        j = i + 1
        children: list[str] = []
        while j < len(lines):
            child = lines[j]
            if child.strip() == "":
                children.append(child)
                j += 1
                continue
            child_indent = _indent_width(child)
            if child_indent <= ref_indent:
                break
            children.append(child)
            j += 1
        kv: dict[str, str] = {}
        child_indent_target = ref_indent + 2
        valid = True
        for child in children:
            raw = child.strip()
            if raw == "":
                continue
            if _indent_width(child) != child_indent_target:
                valid = False
                break
            if ":" not in raw:
                valid = False
                break
            key, value = raw.split(":", 1)
            k = key.strip()
            v = value.strip()
            if k not in {"path", "case_id"}:
                valid = False
                break
            kv[k] = v
        if not valid or not kv:
            out.append(line)
            out.extend(children)
            i = j
            continue
        path = kv.get("path", "")
        case_id = kv.get("case_id", "")
        if path and case_id:
            ref_value = f"{path}#{case_id}"
        elif path:
            ref_value = path
        elif case_id:
            ref_value = f"#{case_id}"
        else:
            out.append(line)
            out.extend(children)
            i = j
            continue
        out.append(" " * ref_indent + f"ref: {ref_value}\n")
        i = j
    return "".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Convert legacy harness.chain step ref mapping to scalar [path][#case_id].")
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
            updated = _rewrite(original)
            if updated != original:
                changed.append(f)
                if ns.write:
                    f.write_text(updated, encoding="utf-8")

    if ns.check:
        if changed:
            for f in changed:
                print(f"{f.as_posix()}: chain ref format drift")
            return 1
        print("OK: chain ref format is canonical")
        return 0

    print(f"OK: rewrote {len(changed)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
