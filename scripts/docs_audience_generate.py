#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import sys
from pathlib import Path

AUDIENCES = [
    "operator",
    "integrator",
    "implementer",
    "maintainer",
    "governance",
    "reviewer",
    "auditor",
]

ROOT = Path(__file__).resolve().parents[1]
SPEC_ROOT = ROOT / "specs"
DOCS_ROOT = ROOT / "docs" / "audience"

AUD_RE = re.compile(r"^\s*audience:\s*([A-Za-z0-9_.-]+)\s*$", re.MULTILINE)


def find_sources() -> dict[str, list[str]]:
    buckets: dict[str, set[str]] = {a: set() for a in AUDIENCES}

    scan_dirs = [SPEC_ROOT / "03_conformance", SPEC_ROOT / "04_governance" / "cases" / "core", SPEC_ROOT / "05_libraries"]
    files: list[Path] = []
    for d in scan_dirs:
        if d.exists():
            files.extend(sorted(d.rglob("*.spec.md")))
    docs_meta_files = [ROOT / "docs" / "book" / "index.md"]
    files.extend([p for p in docs_meta_files if p.exists()])

    for f in files:
        text = f.read_text(encoding="utf-8")
        for m in AUD_RE.finditer(text):
            aud = m.group(1)
            if aud not in buckets:
                raise ValueError(f"non-canonical audience token: {aud} in {f.relative_to(ROOT)}")
            buckets[aud].add("/" + f.relative_to(ROOT).as_posix())

    return {a: sorted(v) for a, v in buckets.items()}


def render_audience_dir(audience: str, paths: list[str], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)

    index_lines = [f"# {audience.capitalize()} Audience Docs", "", "Source paths:", ""]
    if paths:
        for p in paths:
            index_lines.append(f"- `{p}`")
    else:
        index_lines.append("- (none)")
    (out_dir / "index.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")

    manifest_lines = ["version: 1", f"audience: {audience}", "chapters:"]
    for p in paths:
        manifest_lines.append(f"  - path: {p}")
        manifest_lines.append(f"    title: {Path(p).name}")
    (out_dir / "reference_manifest.yaml").write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")

    ref_lines = ["# Reference Index", ""]
    if paths:
        for idx, p in enumerate(paths, 1):
            ref_lines.append(f"{idx}. [{Path(p).name}]({p})")
    else:
        ref_lines.append("1. [(none)](/docs/audience/{audience}/index.md)")
    (out_dir / "reference_index.md").write_text("\n".join(ref_lines) + "\n", encoding="utf-8")

    digest = hashlib.sha256("\n".join(paths).encode("utf-8")).hexdigest()
    cov_lines = [
        "# Reference Coverage",
        "",
        f"- audience: `{audience}`",
        f"- chapter_count: `{len(paths)}`",
        f"- source_digest_sha256: `{digest}`",
    ]
    (out_dir / "reference_coverage.md").write_text("\n".join(cov_lines) + "\n", encoding="utf-8")


def generate(output_root: Path) -> None:
    buckets = find_sources()
    if output_root.exists():
        shutil.rmtree(output_root)
    for audience in AUDIENCES:
        render_audience_dir(audience, buckets[audience], output_root / audience)


def compare_dirs(a: Path, b: Path) -> list[str]:
    diffs: list[str] = []
    a_files = sorted([p.relative_to(a).as_posix() for p in a.rglob("*") if p.is_file()])
    b_files = sorted([p.relative_to(b).as_posix() for p in b.rglob("*") if p.is_file()])
    if a_files != b_files:
        diffs.append("file list differs")
        return diffs
    for rel in a_files:
        if (a / rel).read_bytes() != (b / rel).read_bytes():
            diffs.append(f"content differs: {rel}")
    return diffs


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate audience docs surfaces from spec metadata.")
    ap.add_argument("--check", action="store_true", help="Fail on drift instead of writing files.")
    ns = ap.parse_args()

    target = DOCS_ROOT
    if ns.check:
        tmp = ROOT / ".artifacts" / "audience_docs_tmp"
        if tmp.exists():
            shutil.rmtree(tmp)
        tmp.mkdir(parents=True, exist_ok=True)
        generate(tmp)
        if not target.exists():
            print("ERROR: missing docs/audience output root", file=sys.stderr)
            return 1
        diffs = compare_dirs(tmp, target)
        if diffs:
            print("ERROR: audience docs surfaces are out of sync", file=sys.stderr)
            for d in diffs:
                print(f"- {d}", file=sys.stderr)
            return 1
        print("OK: audience docs surfaces are synchronized")
        return 0

    generate(target)
    print("OK: audience docs surfaces generated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
