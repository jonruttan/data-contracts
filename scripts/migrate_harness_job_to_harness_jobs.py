#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
FENCE_RE = re.compile(r"```yaml contract-spec\n(.*?)\n```", re.DOTALL)


def _load_yaml(payload: str) -> dict[str, Any] | None:
    try:
        data = yaml.safe_load(payload)
    except Exception:
        return None
    if isinstance(data, dict):
        return data
    return None


def _dump_yaml(data: dict[str, Any]) -> str:
    return yaml.safe_dump(data, sort_keys=False).rstrip("\n")


def _inject_dispatch(contract: Any) -> Any:
    if not isinstance(contract, list):
        return contract
    dispatch_expr = {"ops.job.dispatch": ["main"]}

    def has_dispatch(expr: Any) -> bool:
        if isinstance(expr, dict):
            if "ops.job.dispatch" in expr:
                return True
            return any(has_dispatch(v) for v in expr.values())
        if isinstance(expr, list):
            return any(has_dispatch(v) for v in expr)
        return False

    if has_dispatch(contract):
        return contract

    for step in contract:
        if isinstance(step, dict):
            asserts = step.get("asserts")
            if isinstance(asserts, list):
                asserts.insert(0, dispatch_expr)
                return contract
    contract.insert(
        0,
        {
            "id": "dispatch_main",
            "class": "must",
            "target": "summary_json",
            "asserts": [dispatch_expr],
        },
    )
    return contract


def _migrate_case(case: dict[str, Any]) -> tuple[dict[str, Any], bool]:
    changed = False
    if str(case.get("type", "")).strip() != "contract.job":
        return case, False
    harness = case.get("harness")
    if not isinstance(harness, dict):
        return case, False

    if "job" in harness:
        job = harness.pop("job")
        if isinstance(job, dict) and "ref" in job:
            job.pop("ref", None)
        jobs = harness.get("jobs")
        if not isinstance(jobs, dict):
            jobs = {}
        if "main" not in jobs:
            jobs["main"] = job
        harness["jobs"] = jobs
        changed = True
    if isinstance(harness.get("jobs"), dict):
        for entry in harness["jobs"].values():
            if isinstance(entry, dict) and "ref" in entry:
                entry.pop("ref", None)
                changed = True

    contract = case.get("contract")
    migrated_contract = _inject_dispatch(contract)
    if migrated_contract is not contract:
        case["contract"] = migrated_contract
        changed = True

    spec_lang = harness.get("spec_lang")
    if not isinstance(spec_lang, dict):
        spec_lang = {}
        harness["spec_lang"] = spec_lang
    caps = spec_lang.get("capabilities")
    if not isinstance(caps, list):
        caps = []
    if "ops.job" not in caps:
        caps.append("ops.job")
        spec_lang["capabilities"] = caps
        changed = True

    return case, changed


def migrate_file(path: Path, write: bool) -> bool:
    raw = path.read_text(encoding="utf-8")
    changed_any = False

    def repl(m: re.Match[str]) -> str:
        nonlocal changed_any
        payload = m.group(1)
        case = _load_yaml(payload)
        if case is None:
            return m.group(0)
        migrated, changed = _migrate_case(case)
        if not changed:
            return m.group(0)
        changed_any = True
        return "```yaml contract-spec\n" + _dump_yaml(migrated) + "\n```"

    updated = FENCE_RE.sub(repl, raw)
    if changed_any and write:
        path.write_text(updated, encoding="utf-8")
    return changed_any


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*", default=["docs/spec"])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--write", action="store_true")
    ns = ap.parse_args()
    if ns.check == ns.write:
        ap.error("choose exactly one of --check or --write")

    files: list[Path] = []
    for p in ns.paths:
        target = (ROOT / p).resolve() if not p.startswith("/") else Path(p)
        if target.is_file() and target.suffix == ".md":
            files.append(target)
        elif target.is_dir():
            files.extend(sorted(x for x in target.rglob("*.spec.md") if x.is_file()))

    changed_files: list[Path] = []
    for f in files:
        if migrate_file(f, write=ns.write):
            changed_files.append(f)

    if ns.check:
        if changed_files:
            for f in changed_files:
                print(f"NEEDS_MIGRATION: {f.relative_to(ROOT).as_posix()}")
            return 1
        print("OK: no harness.job migration needed")
        return 0
    print(f"OK: rewrote {len(changed_files)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
