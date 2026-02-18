#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

import importlib.util


def _load_inventory_builder() -> object:
    script_path = Path(__file__).resolve().parent / "docs_inventory.py"
    spec = importlib.util.spec_from_file_location("docs_inventory", script_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("unable to load docs_inventory.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module.build_inventory


build_inventory = _load_inventory_builder()

_FORBIDDEN_TOKENS = {
    "spec-test": r"\bspec-test\b",
    "policy_evaluate": r"\bpolicy_evaluate\b",
}

_SOURCE_OF_TRUTH_RE = re.compile(r"^Source of truth:\s*([^\s]+)\s*$", re.IGNORECASE)
_EXPECTED_SPEC_INDEX_LINKS = {
    "/docs/spec/schema/index.md",
    "/docs/spec/contract/index.md",
    "/docs/spec/governance/index.md",
    "/docs/spec/libraries/index.md",
    "/docs/spec/impl/index.md",
    "/docs/spec/current.md",
}


def _load_check_map(root: Path) -> dict[str, Any]:
    path = root / "docs/spec/governance/check_catalog_map_v1.yaml"
    if not path.exists():
        return {}
    prefixes: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped.startswith("check_prefix:"):
            continue
        value = stripped.split(":", 1)[1].strip().strip("'\"")
        if value:
            prefixes.append(value)
    return {"families": [{"check_prefix": p} for p in prefixes]}


def _check_source_of_truth(root: Path) -> list[str]:
    seen: dict[str, str] = {}
    violations: list[str] = []
    for path in sorted((root / "docs").rglob("*.md")):
        rel = path.relative_to(root).as_posix()
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            m = _SOURCE_OF_TRUTH_RE.match(line.strip())
            if not m:
                continue
            key = m.group(1).strip()
            prev = seen.get(key)
            if prev and prev != rel:
                violations.append(
                    f"{rel}:{line_no}: duplicate source-of-truth marker '{key}' already declared in {prev}"
                )
            else:
                seen[key] = rel
    return violations


def _check_forbidden_tokens(root: Path) -> list[str]:
    violations: list[str] = []
    for path in sorted((root / "docs").rglob("*.md")):
        rel = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8")
        for label, pattern in _FORBIDDEN_TOKENS.items():
            if re.search(pattern, text):
                violations.append(f"{rel}: contains forbidden stale token '{label}'")
    return violations


def _check_spec_index_contract(root: Path) -> list[str]:
    path = root / "docs/spec/index.md"
    if not path.exists():
        return ["docs/spec/index.md missing"]
    text = path.read_text(encoding="utf-8")
    violations: list[str] = []
    for rel in _EXPECTED_SPEC_INDEX_LINKS:
        if rel not in text:
            violations.append(f"docs/spec/index.md missing canonical link {rel}")
    return violations


def _check_governance_family_map(root: Path) -> list[str]:
    mapping = _load_check_map(root)
    families = mapping.get("families") if isinstance(mapping, dict) else None
    if not isinstance(families, list) or not families:
        return ["docs/spec/governance/check_catalog_map_v1.yaml must declare non-empty families list"]

    prefixes: set[str] = set()
    for entry in families:
        if not isinstance(entry, dict):
            return ["docs/spec/governance/check_catalog_map_v1.yaml families entries must be mappings"]
        prefix = str(entry.get("check_prefix", "")).strip()
        if not prefix:
            return ["docs/spec/governance/check_catalog_map_v1.yaml families[].check_prefix required"]
        prefixes.add(prefix)

    violations: list[str] = []
    for path in sorted((root / "docs/spec/governance/cases/core").glob("*.spec.md")):
        name = path.name
        stem = name[:-8] if name.endswith(".spec.md") else name
        if "_" not in stem:
            violations.append(f"{path.relative_to(root).as_posix()}: expected '<family>_*.spec.md' naming")
            continue
        family = stem.split("_", 1)[0]
        check_prefix = family + "."
        if check_prefix not in prefixes:
            violations.append(
                f"{path.relative_to(root).as_posix()}: no check-family mapping for prefix '{check_prefix}'"
            )
    return violations


def _run_docs_generate_check(root: Path) -> list[str]:
    cp = subprocess.run(
        [sys.executable, "scripts/docs_generate_all.py", "--check"],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    if cp.returncode == 0:
        return []
    out = (cp.stdout + cp.stderr).strip()
    if out:
        return [f"docs_generate_all --check failed:\n{out}"]
    return ["docs_generate_all --check failed with no output"]


def main() -> int:
    parser = argparse.ArgumentParser(description="Strict docs/spec freshness and organization checks")
    parser.add_argument("--strict", action="store_true", help="return non-zero when violations are detected")
    parser.add_argument("--out", default=".artifacts/docs-freshness-report.json", help="report output path")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    inventory = build_inventory(root)
    violations: list[str] = []

    for item in inventory.get("missing_links", []):
        if isinstance(item, dict):
            violations.append(f"{item.get('file')}: broken link target {item.get('target')}")

    violations.extend(_check_source_of_truth(root))
    violations.extend(_check_forbidden_tokens(root))
    violations.extend(_check_spec_index_contract(root))
    violations.extend(_check_governance_family_map(root))
    violations.extend(_run_docs_generate_check(root))

    report: dict[str, Any] = {
        "version": 1,
        "strict": args.strict,
        "ok": len(violations) == 0,
        "violations": violations,
        "inventory_summary": inventory.get("summary", {}),
    }

    out_path = root / args.out
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {out_path.relative_to(root).as_posix()}")

    if violations:
        for item in violations:
            print(f"DOC-FRESHNESS: {item}")
        return 1 if args.strict else 0
    print("OK: docs freshness checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
