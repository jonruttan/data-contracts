from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import yaml

from spec_runner.dispatcher import SpecRunContext, run_case
from spec_runner.doc_parser import SpecDocTest


@dataclass(frozen=True)
class ConformanceResult:
    id: str
    status: str
    category: str | None
    message: str | None = None


def _read_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def load_conformance_cases(cases_dir: Path) -> list[tuple[Path, dict[str, Any]]]:
    out: list[tuple[Path, dict[str, Any]]] = []
    for p in sorted(cases_dir.glob("*.y*ml")):
        payload = _read_yaml(p)
        if not isinstance(payload, dict):
            raise TypeError(f"conformance cases file must be a mapping: {p}")
        cases = payload.get("cases") or []
        if not isinstance(cases, list):
            raise TypeError(f"conformance cases must be a list: {p}")
        for c in cases:
            if not isinstance(c, dict):
                raise TypeError(f"conformance case must be a mapping: {p}")
            if "id" not in c or "type" not in c:
                raise ValueError(f"conformance case must include 'id' and 'type': {p}")
            out.append((p, c))
    return out


def load_expected_results(expected_dir: Path) -> dict[str, ConformanceResult]:
    out: dict[str, ConformanceResult] = {}
    for p in sorted(expected_dir.glob("*.y*ml")):
        payload = _read_yaml(p)
        if not isinstance(payload, dict):
            raise TypeError(f"conformance expected file must be a mapping: {p}")
        results = payload.get("results") or []
        if not isinstance(results, list):
            raise TypeError(f"conformance expected results must be a list: {p}")
        for r in results:
            if not isinstance(r, dict):
                raise TypeError(f"conformance expected item must be a mapping: {p}")
            rid = str(r.get("id", "")).strip()
            if not rid:
                raise ValueError(f"conformance expected item missing id: {p}")
            out[rid] = ConformanceResult(
                id=rid,
                status=str(r.get("status", "")).strip(),
                category=None if r.get("category") is None else str(r.get("category")),
                message=None if r.get("message") is None else str(r.get("message")),
            )
    return out


def _category_for_exception(exc: BaseException) -> str:
    if isinstance(exc, AssertionError):
        return "assertion"
    if isinstance(exc, (TypeError, ValueError)):
        return "schema"
    return "runtime"


def run_conformance_cases(
    cases_dir: Path,
    *,
    ctx: SpecRunContext,
) -> list[ConformanceResult]:
    results: list[ConformanceResult] = []
    for fixture_path, case in load_conformance_cases(cases_dir):
        test = dict(case)
        case_id = str(test.get("id", ""))
        try:
            run_case(
                SpecDocTest(doc_path=fixture_path, test=test),
                ctx=ctx,
            )
            results.append(ConformanceResult(id=case_id, status="pass", category=None, message=None))
        except BaseException as e:  # noqa: BLE001
            results.append(
                ConformanceResult(
                    id=case_id,
                    status="fail",
                    category=_category_for_exception(e),
                    message=str(e) or e.__class__.__name__,
                )
            )
    return results


def compare_conformance_results(
    expected: dict[str, ConformanceResult],
    actual: list[ConformanceResult],
) -> list[str]:
    errs: list[str] = []
    actual_by_id = {r.id: r for r in actual}
    for rid, exp in expected.items():
        got = actual_by_id.get(rid)
        if got is None:
            errs.append(f"missing actual result for id: {rid}")
            continue
        if got.status != exp.status:
            errs.append(f"status mismatch for {rid}: expected={exp.status} actual={got.status}")
        if got.category != exp.category:
            errs.append(f"category mismatch for {rid}: expected={exp.category} actual={got.category}")
    for rid in actual_by_id:
        if rid not in expected:
            errs.append(f"unexpected actual result id: {rid}")
    return errs


def results_to_jsonable(results: list[ConformanceResult]) -> list[dict[str, Any]]:
    return [asdict(r) for r in results]
