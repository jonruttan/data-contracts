#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REPLACEMENTS = (
    ("when.can", "when.may"),
    ("when.cannot", "when.must_not"),
    ("when.maynot", "when.must_not"),
    ("must/can/cannot", "must/may/must_not"),
    ("must, can, cannot", "must, may, must_not"),
    ("harness_on_", "when_"),
    ("HARNESS_ON_", "WHEN_"),
    ("runtime.harness_on_", "runtime.when_"),
    ("harness.harness_on_", "harness.when_"),
    ('"MAY": "can"', '"MAY": "may"'),
    ('"MUST_NOT": "cannot"', '"MUST_NOT": "must_not"'),
)

LINE_KEY_REPLACEMENTS = (
    ("can:", "may:"),
    ("cannot:", "must_not:"),
)


def _iter_targets() -> list[Path]:
    out: list[Path] = []
    globs = (
        "docs/spec/**/*.md",
        "docs/book/**/*.md",
        "scripts/**/*.py",
        "scripts/**/*.sh",
        "scripts/rust/spec_runner_cli/src/*.rs",
        "spec_runner/**/*.py",
        "README.md",
        "docs/development.md",
        "Makefile",
        ".github/workflows/ci.yml",
    )
    for g in globs:
        out.extend(sorted(x for x in ROOT.glob(g) if x.is_file()))
    # de-dupe
    seen: set[Path] = set()
    uniq: list[Path] = []
    for p in out:
        if p in seen:
            continue
        seen.add(p)
        uniq.append(p)
    return uniq


def _apply(raw: str) -> str:
    updated = raw
    for old, new in REPLACEMENTS:
        updated = updated.replace(old, new)
    lines = updated.splitlines(keepends=True)
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        indent = line[: len(line) - len(stripped)]
        for old, new in LINE_KEY_REPLACEMENTS:
            if stripped == old + ("\n" if stripped.endswith("\n") else ""):
                break
        if stripped.strip() == "can:":
            lines[i] = f"{indent}may:\n"
        elif stripped.strip() == "cannot:":
            lines[i] = f"{indent}must_not:\n"
    return "".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Codemod hook/event terms to must|may|must_not")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--write", action="store_true")
    ns = ap.parse_args(argv)
    if ns.check == ns.write:
        ap.error("set exactly one of --check or --write")

    changed = 0
    for p in _iter_targets():
        raw = p.read_text(encoding="utf-8")
        updated = _apply(raw)
        if updated != raw:
            changed += 1
            if ns.write:
                p.write_text(updated, encoding="utf-8")
            else:
                print(p.relative_to(ROOT).as_posix())
    if ns.check and changed:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
