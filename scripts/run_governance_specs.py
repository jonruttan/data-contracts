#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from spec_runner.assertions import assert_text_op, eval_assert_tree, iter_leaf_assertions
from spec_runner.dispatcher import SpecRunContext, iter_cases, run_case
from spec_runner.runtime_context import MiniCapsys, MiniMonkeyPatch
from spec_runner.settings import SETTINGS, governed_config_literals
from spec_runner.conformance_purpose import PURPOSE_WARNING_CODES


_SECURITY_WARNING_DOCS = (
    "README.md",
    "docs/book/00_first_10_minutes.md",
    "docs/spec/schema/schema_v1.md",
)
_SECURITY_WARNING_TOKENS = (
    "not a sandbox",
    "trusted inputs",
    "untrusted spec",
)
_V1_SCOPE_DOC = "docs/spec/contract/08_v1_scope.md"
_V1_SCOPE_REQUIRED_TOKENS = (
    "v1 in scope",
    "v1 non-goals",
    "compatibility commitments",
)
_PYTHON_RUNTIME_ROOTS = ("spec_runner", "scripts/python")
_CONFORMANCE_CASE_ID_PATTERN = r"\bSRCONF-[A-Z0-9-]+\b"


def _scan_pending_no_resolved_markers(root: Path) -> list[str]:
    pending_dir = root / "docs/spec/pending"
    if not pending_dir.exists():
        return []
    violations: list[str] = []
    for p in sorted(pending_dir.glob("*.md")):
        lower = p.read_text(encoding="utf-8").lower()
        for tok in ("resolved:", "completed:"):
            if tok in lower:
                rel = p.relative_to(root)
                violations.append(f"{rel}: found '{tok}'")
    return violations


def _scan_security_warning_docs(root: Path) -> list[str]:
    violations: list[str] = []
    for rel in _SECURITY_WARNING_DOCS:
        p = root / rel
        if not p.exists():
            violations.append(f"{rel}: missing required doc")
            continue
        lower = p.read_text(encoding="utf-8").lower()
        missing = [tok for tok in _SECURITY_WARNING_TOKENS if tok not in lower]
        if missing:
            violations.append(f"{rel}: missing token(s): {', '.join(missing)}")
    return violations


def _scan_v1_scope_doc(root: Path) -> list[str]:
    p = root / _V1_SCOPE_DOC
    if not p.exists():
        return [f"{_V1_SCOPE_DOC}: missing required doc"]
    lower = p.read_text(encoding="utf-8").lower()
    missing = [tok for tok in _V1_SCOPE_REQUIRED_TOKENS if tok not in lower]
    if missing:
        return [f"{_V1_SCOPE_DOC}: missing token(s): {', '.join(missing)}"]
    return []


def _scan_runtime_config_literals(root: Path) -> list[str]:
    violations: list[str] = []
    governed = governed_config_literals()
    for rel_root in _PYTHON_RUNTIME_ROOTS:
        runtime_root = root / rel_root
        if not runtime_root.exists():
            continue
        for p in sorted(runtime_root.rglob("*.py")):
            if p.name == "settings.py":
                continue
            raw = p.read_text(encoding="utf-8")
            rel = p.relative_to(root)
            for literal, const_path in governed.items():
                if f'"{literal}"' in raw or f"'{literal}'" in raw:
                    violations.append(
                        f"{rel}: literal {literal!r} duplicated; use {const_path}"
                    )
    return violations


def _scan_runtime_settings_import_policy(root: Path) -> list[str]:
    violations: list[str] = []
    for rel_root in _PYTHON_RUNTIME_ROOTS:
        runtime_root = root / rel_root
        if not runtime_root.exists():
            continue
        for p in sorted(runtime_root.rglob("*.py")):
            if p.name == "settings.py":
                continue
            rel = p.relative_to(root)
            for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), start=1):
                s = line.strip()
                if not s.startswith("from spec_runner.settings import "):
                    continue
                imported = s.split("import ", 1)[1]
                names = [x.strip() for x in imported.split(",")]
                bad = [n for n in names if n.isupper() and n.startswith(("DEFAULT_", "ENV_"))]
                if bad:
                    violations.append(f"{rel}:{i}: banned settings constant import(s): {', '.join(bad)}")
    return violations


def _collect_conformance_fixture_ids(root: Path) -> set[str]:
    ids: set[str] = set()
    cases_dir = root / "docs/spec/conformance/cases"
    if not cases_dir.exists():
        return ids
    for spec in iter_cases(cases_dir, file_pattern=SETTINGS.case.default_file_pattern):
        rid = str(spec.test.get("id", "")).strip()
        if rid:
            ids.add(rid)
    return ids


def _scan_conformance_case_index_sync(root: Path) -> list[str]:
    import re

    violations: list[str] = []
    cases_dir = root / "docs/spec/conformance/cases"
    fixture_ids = _collect_conformance_fixture_ids(root)
    index_path = cases_dir / "README.md"
    if not fixture_ids and not index_path.exists():
        return violations
    if not index_path.exists():
        return [f"{index_path.relative_to(root)}: missing conformance case index"]

    raw = index_path.read_text(encoding="utf-8")
    indexed_ids = set(re.findall(_CONFORMANCE_CASE_ID_PATTERN, raw))
    for rid in sorted(fixture_ids - indexed_ids):
        violations.append(f"{index_path.relative_to(root)}: missing id {rid}")
    for rid in sorted(indexed_ids - fixture_ids):
        violations.append(f"{index_path.relative_to(root)}: stale id {rid}")
    return violations


def _scan_conformance_purpose_warning_codes_sync(root: Path) -> list[str]:
    import re

    p = root / "docs/spec/conformance/purpose_warning_codes.md"
    if not p.exists():
        return [f"{p.relative_to(root)}: missing purpose warning code doc"]
    raw = p.read_text(encoding="utf-8")
    doc_codes = set(re.findall(r"\bPUR\d{3}\b", raw))
    impl_codes = set(PURPOSE_WARNING_CODES)
    violations: list[str] = []
    for c in sorted(impl_codes - doc_codes):
        violations.append(f"{p.relative_to(root)}: missing code {c}")
    for c in sorted(doc_codes - impl_codes):
        violations.append(f"{p.relative_to(root)}: stale code {c}")
    return violations


GovernanceCheck = Callable[[Path], list[str]]

_CHECKS: dict[str, GovernanceCheck] = {
    "pending.no_resolved_markers": _scan_pending_no_resolved_markers,
    "docs.security_warning_contract": _scan_security_warning_docs,
    "docs.v1_scope_contract": _scan_v1_scope_doc,
    "runtime.config_literals": _scan_runtime_config_literals,
    "runtime.settings_import_policy": _scan_runtime_settings_import_policy,
    "conformance.case_index_sync": _scan_conformance_case_index_sync,
    "conformance.purpose_warning_codes_sync": _scan_conformance_purpose_warning_codes_sync,
}


def run_governance_check(case, *, ctx) -> None:
    t = case.test
    check_id = str(t.get("check", "")).strip()
    if not check_id:
        raise ValueError("governance.check requires 'check'")
    fn = _CHECKS.get(check_id)
    if fn is None:
        supported = ", ".join(sorted(_CHECKS))
        raise ValueError(f"unknown governance check: {check_id} (supported: {supported})")

    h = t.get("harness") or {}
    if not isinstance(h, dict):
        raise TypeError("harness must be a mapping")
    root = Path(str(h.get("root", "."))).resolve()
    violations = fn(root)

    text = (
        f"PASS: {check_id}"
        if not violations
        else f"FAIL: {check_id}\n" + "\n".join(violations)
    )

    assert_spec = t.get("assert", []) or []

    def _eval_leaf(leaf: dict, *, inherited_target: str | None = None, assert_path: str = "assert") -> None:
        for target, op, value, is_true in iter_leaf_assertions(leaf, target_override=inherited_target):
            if target != "text":
                raise ValueError(f"unknown assert target for governance.check: {target}")
            assert_text_op(text, op, value, is_true=is_true)

    eval_assert_tree(assert_spec, eval_leaf=_eval_leaf)
    if violations:
        raise AssertionError(text)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Run governance spec cases with project-owned governance.check harness."
    )
    ap.add_argument("--cases", default="docs/spec/governance/cases", help="Path to governance case docs directory")
    ap.add_argument(
        "--case-file-pattern",
        default=SETTINGS.case.default_file_pattern,
        help="Glob pattern for case files when --cases points to a directory",
    )
    ns = ap.parse_args(argv)

    case_pattern = str(ns.case_file_pattern).strip()
    if not case_pattern:
        print("ERROR: --case-file-pattern requires a non-empty value", file=sys.stderr)
        return 2

    cases_path = Path(str(ns.cases))
    if not cases_path.exists():
        print(f"ERROR: cases path does not exist: {cases_path}", file=sys.stderr)
        return 2

    failures: list[str] = []
    with TemporaryDirectory(prefix="spec-runner-governance-") as td:
        ctx = SpecRunContext(
            tmp_path=Path(td),
            patcher=MiniMonkeyPatch(),
            capture=MiniCapsys(),
        )
        for case in iter_cases(cases_path, file_pattern=case_pattern):
            try:
                run_case(case, ctx=ctx, type_runners={"governance.check": run_governance_check})
            except BaseException as e:  # noqa: BLE001
                failures.append(f"{case.test.get('id', '<unknown>')}: {e}")

    if failures:
        for line in failures:
            print(f"ERROR: {line}", file=sys.stderr)
        return 1

    print(f"OK: governance specs passed ({cases_path})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
