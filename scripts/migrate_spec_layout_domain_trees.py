#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from spec_runner.codecs import load_external_cases


ROOT = Path(__file__).resolve().parents[1]
SCAN_EXTS = (".md", ".yaml", ".yml", ".json", ".py", ".sh", ".toml")


def _iter_text_files(root: Path) -> list[Path]:
    out: list[Path] = []
    for p in sorted(root.rglob("*")):
        if not p.is_file():
            continue
        if p.suffix.lower() in SCAN_EXTS:
            out.append(p)
    return out


def _rel(p: Path) -> str:
    return "/" + p.relative_to(ROOT).as_posix()


def _rewrite_refs(mapping: dict[str, str], *, check_only: bool) -> list[str]:
    changed: list[str] = []
    files = _iter_text_files(ROOT)
    for p in files:
        raw = p.read_text(encoding="utf-8")
        updated = raw
        for old, new in mapping.items():
            updated = updated.replace(old, new)
            updated = updated.replace(old.lstrip("/"), new.lstrip("/"))
        if updated != raw:
            changed.append(p.relative_to(ROOT).as_posix())
            if not check_only:
                p.write_text(updated, encoding="utf-8")
    return changed


def _library_exports_for_file(spec_path: Path) -> list[str]:
    exports: list[str] = []
    for _doc_path, case in load_external_cases(spec_path, formats={"md"}):
        if str(case.get("type", "")).strip() != "spec_lang.library":
            continue
        raw_definitions = case.get("definitions")
        if not isinstance(raw_definitions, dict):
            continue
        raw_public_scope = raw_definitions.get("public")
        if not isinstance(raw_public_scope, dict):
            continue
        for item in raw_public_scope.keys():
            sym = str(item).strip()
            if sym:
                exports.append(sym)
    # Stable unique.
    return sorted(dict.fromkeys(exports))


def _write_domain_index(domain_dir: Path, title: str, spec_files: list[Path], *, check_only: bool) -> bool:
    lines = [
        f"# {title} Domain Index",
        "",
        "Canonical domain index for executable specs in this subtree.",
        "",
        "## Files",
        "",
    ]
    for p in sorted(spec_files):
        rel = "/" + p.relative_to(ROOT).as_posix()
        lines.append(f"- `{rel}`")
    if "/docs/spec/libraries/" in ("/" + domain_dir.relative_to(ROOT).as_posix() + "/"):
        lines.extend(["", "## Exported Symbols", ""])
        for p in sorted(spec_files):
            rel = "/" + p.relative_to(ROOT).as_posix()
            for sym in _library_exports_for_file(p):
                lines.append(f"- `{sym}` ({rel})")
    lines.append("")
    body = "\n".join(lines)
    index_path = domain_dir / "index.md"
    if index_path.exists():
        cur = index_path.read_text(encoding="utf-8")
        if cur == body:
            return False
    if not check_only:
        index_path.parent.mkdir(parents=True, exist_ok=True)
        index_path.write_text(body, encoding="utf-8")
    return True


def _migrate_root(
    cases_root: Path,
    *,
    domain: str,
    title: str,
    check_only: bool,
) -> tuple[dict[str, str], list[str], bool]:
    mapping: dict[str, str] = {}
    moved: list[str] = []
    domain_dir = cases_root / domain
    if not check_only:
        domain_dir.mkdir(parents=True, exist_ok=True)

    spec_files = sorted(
        p for p in cases_root.glob("*.spec.md") if p.is_file()
    )
    for src in spec_files:
        dst = domain_dir / src.name
        mapping[_rel(src)] = _rel(dst)
        moved.append(src.relative_to(ROOT).as_posix())
        if not check_only:
            src.rename(dst)

    final_specs = sorted(p for p in domain_dir.glob("*.spec.md") if p.is_file())
    index_changed = _write_domain_index(domain_dir, title, final_specs, check_only=check_only)
    return mapping, moved, index_changed


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Migrate flat spec case layout to domain-tree layout.")
    ap.add_argument("--check", action="store_true", help="detect pending migration without writing")
    ap.add_argument(
        "--write",
        action="store_true",
        help="apply migration and rewrite references",
    )
    ns = ap.parse_args(argv)
    if ns.check == ns.write:
        ap.error("exactly one of --check or --write is required")

    check_only = bool(ns.check)
    all_mapping: dict[str, str] = {}
    moved: list[str] = []
    index_updates = 0

    roots = [
        (ROOT / "docs/spec/conformance/cases", "core", "Conformance Cases"),
        (ROOT / "docs/spec/governance/cases", "core", "Governance Cases"),
    ]
    for root, domain, title in roots:
        mapping, moved_here, index_changed = _migrate_root(
            root,
            domain=domain,
            title=title,
            check_only=check_only,
        )
        all_mapping.update(mapping)
        moved.extend(moved_here)
        index_updates += 1 if index_changed else 0

    # Always keep library indexes in sync.
    for lib_domain, title in (
        (ROOT / "docs/spec/libraries/conformance", "Conformance Libraries"),
        (ROOT / "docs/spec/libraries/path", "Path Libraries"),
        (ROOT / "docs/spec/libraries/policy", "Policy Libraries"),
    ):
        specs = sorted(p for p in lib_domain.glob("*.spec.md") if p.is_file())
        if _write_domain_index(lib_domain, title, specs, check_only=check_only):
            index_updates += 1

    rewrites = _rewrite_refs(all_mapping, check_only=check_only) if all_mapping else []

    if check_only:
        if moved or rewrites:
            print(
                "pending domain-tree migration: "
                f"{len(moved)} case files to move, {len(rewrites)} files to rewrite refs, "
                f"{index_updates} index updates"
            )
            return 1
        print("OK: domain-tree layout already migrated")
        return 0

    print(
        "OK: migrated domain-tree layout: "
        f"moved={len(moved)} rewritten={len(rewrites)} index_updates={index_updates}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
