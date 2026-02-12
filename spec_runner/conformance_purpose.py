from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from spec_runner.doc_parser import iter_spec_doc_tests
from spec_runner.purpose_lint import POLICY_REL_PATH, load_purpose_lint_policy, resolve_purpose_lint_config


@dataclass(frozen=True)
class ConformancePurposeRow:
    id: str
    title: str
    purpose: str
    type: str
    file: str
    purpose_lint: dict[str, Any]


def _display_path(path: Path, *, cwd: Path) -> str:
    try:
        return str(path.resolve().relative_to(cwd.resolve()))
    except ValueError:
        return str(path.resolve())


def collect_conformance_purpose_rows(cases_dir: Path, *, purpose_policy: dict[str, Any]) -> list[ConformancePurposeRow]:
    cwd = Path.cwd()
    rows: list[ConformancePurposeRow] = []
    for spec in iter_spec_doc_tests(cases_dir):
        test = dict(spec.test)
        rows.append(
            ConformancePurposeRow(
                id=str(test.get("id", "")).strip(),
                title=str(test.get("title", "")).strip(),
                purpose=str(test.get("purpose", "")).strip(),
                type=str(test.get("type", "")).strip(),
                file=_display_path(spec.doc_path, cwd=cwd),
                purpose_lint=resolve_purpose_lint_config(test, purpose_policy)[0],
            )
        )
    rows.sort(key=lambda r: (r.id, r.file))
    return rows


def conformance_purpose_report_jsonable(cases_dir: Path, *, repo_root: Path) -> dict[str, Any]:
    policy, policy_errs, policy_path = load_purpose_lint_policy(repo_root)
    rows = collect_conformance_purpose_rows(cases_dir, purpose_policy=policy)
    return {
        "version": 1,
        "policy": {
            "path": POLICY_REL_PATH,
            "exists": policy_path.exists(),
            "config": policy,
            "errors": policy_errs,
        },
        "rows": [asdict(r) for r in rows],
    }
