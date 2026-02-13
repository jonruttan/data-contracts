from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any

from spec_runner.conformance import (
    ConformanceResult,
    compare_conformance_results,
    load_expected_results,
    report_to_jsonable,
    run_conformance_cases,
    validate_conformance_report_payload,
)
from spec_runner.dispatcher import SpecRunContext
from spec_runner.runtime_context import MiniCapsys, MiniMonkeyPatch


@dataclass(frozen=True)
class ParityConfig:
    cases_dir: Path
    php_runner: Path
    php_timeout_seconds: int = 30


def _normalize_report(payload: dict[str, Any]) -> dict[str, tuple[str, str | None]]:
    out: dict[str, tuple[str, str | None]] = {}
    for raw in payload.get("results", []):
        rid = str(raw.get("id", ""))
        out[rid] = (
            str(raw.get("status", "")),
            None if raw.get("category") is None else str(raw.get("category")),
        )
    return out


def compare_parity_reports(
    python_payload: dict[str, Any],
    php_payload: dict[str, Any],
    *,
    include_ids: set[str] | None = None,
) -> list[str]:
    py = _normalize_report(python_payload)
    php = _normalize_report(php_payload)
    if include_ids is None:
        ids = set(py.keys()) | set(php.keys())
    else:
        ids = set(include_ids)
    diffs: list[str] = []
    for rid in sorted(ids):
        if rid not in py:
            diffs.append(f"missing in python report: {rid}")
            continue
        if rid not in php:
            diffs.append(f"missing in php report: {rid}")
            continue
        if py[rid] != php[rid]:
            diffs.append(
                "mismatch for "
                f"{rid}: python(status={py[rid][0]}, category={py[rid][1]}) "
                f"!= php(status={php[rid][0]}, category={php[rid][1]})"
            )
    return diffs


def build_parity_artifact(errors: list[str]) -> dict[str, Any]:
    artifact: dict[str, Any] = {
        "version": 1,
        "missing": [],
        "mismatch": [],
        "shape_errors": [],
    }
    missing = artifact["missing"]
    mismatch = artifact["mismatch"]
    shape = artifact["shape_errors"]
    for e in errors:
        if e.startswith("missing in "):
            missing.append(e)
            continue
        if e.startswith("mismatch for "):
            mismatch.append(e)
            continue
        if e.startswith("python vs expected:") or e.startswith("php vs expected:"):
            mismatch.append(e)
            continue
        # Keep all non-diff failures visible in shape_errors for CI diagnostics.
        shape.append(e)
    return artifact


def _shared_expectation_ids_from_expected(
    py_expected: dict[str, Any],
    php_expected: dict[str, Any],
) -> set[str]:
    shared: set[str] = set()
    for rid in sorted(set(py_expected.keys()) & set(php_expected.keys())):
        py = py_expected[rid]
        php = php_expected[rid]
        if py.status == php.status and py.category == php.category:
            shared.add(rid)
    return shared


def run_python_report(cases_dir: Path) -> dict[str, Any]:
    with TemporaryDirectory(prefix="spec-runner-parity-") as td:
        tmp_path = Path(td)
        monkeypatch = MiniMonkeyPatch()
        capsys = MiniCapsys()
        ctx = SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys)
        with capsys.capture():
            results = run_conformance_cases(
                cases_dir,
                ctx=ctx,
                implementation="python",
            )
    return report_to_jsonable(results)


def run_php_report(cases_dir: Path, php_runner: Path, *, timeout_seconds: int = 30) -> dict[str, Any]:
    with TemporaryDirectory(prefix="spec-runner-parity-") as td:
        out_path = Path(td) / "php-conformance-report.json"
        try:
            cp = subprocess.run(
                [
                    "php",
                    str(php_runner),
                    "--cases",
                    str(cases_dir),
                    "--out",
                    str(out_path),
                ],
                check=False,
                capture_output=True,
                text=True,
                timeout=timeout_seconds,
            )
        except subprocess.TimeoutExpired as e:
            raise RuntimeError(
                f"php conformance runner timed out after {timeout_seconds}s "
                f"(runner={php_runner}, cases={cases_dir})"
            ) from e
        if cp.returncode != 0:
            stderr = cp.stderr.strip()
            raise RuntimeError(
                f"php conformance runner failed with exit {cp.returncode}"
                + (f": {stderr}" if stderr else "")
            )
        return json.loads(out_path.read_text(encoding="utf-8"))


def run_parity_check(config: ParityConfig) -> list[str]:
    python_payload = run_python_report(config.cases_dir)
    php_payload = run_php_report(
        config.cases_dir,
        config.php_runner,
        timeout_seconds=int(config.php_timeout_seconds),
    )

    errors: list[str] = []
    py_shape = validate_conformance_report_payload(python_payload)
    php_shape = validate_conformance_report_payload(php_payload)
    errors.extend([f"python report invalid: {e}" for e in py_shape])
    errors.extend([f"php report invalid: {e}" for e in php_shape])
    if errors:
        return errors

    expected = load_expected_results(config.cases_dir, implementation="python")
    python_actual = [
        ConformanceResult(
            id=str(r.get("id", "")),
            status=str(r.get("status", "")),
            category=None if r.get("category") is None else str(r.get("category")),
            message=None if r.get("message") is None else str(r.get("message")),
        )
        for r in python_payload.get("results", [])
    ]
    php_expected = load_expected_results(config.cases_dir, implementation="php")
    php_actual = [
        ConformanceResult(
            id=str(r.get("id", "")),
            status=str(r.get("status", "")),
            category=None if r.get("category") is None else str(r.get("category")),
            message=None if r.get("message") is None else str(r.get("message")),
        )
        for r in php_payload.get("results", [])
    ]
    errors.extend([f"python vs expected: {e}" for e in compare_conformance_results(expected, python_actual)])
    errors.extend([f"php vs expected: {e}" for e in compare_conformance_results(php_expected, php_actual)])
    errors.extend(compare_parity_reports(python_payload, php_payload, include_ids=_shared_expectation_ids_from_expected(expected, php_expected)))
    return errors
