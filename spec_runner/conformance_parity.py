from __future__ import annotations

import io
import json
import os
import subprocess
from contextlib import contextmanager, redirect_stderr, redirect_stdout
from dataclasses import dataclass
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from typing import Any, Iterator

from spec_runner.conformance import (
    ConformanceResult,
    compare_conformance_results,
    load_expected_results,
    report_to_jsonable,
    run_conformance_cases,
    validate_conformance_report_payload,
)
from spec_runner.dispatcher import SpecRunContext


@dataclass(frozen=True)
class ParityConfig:
    cases_dir: Path
    php_runner: Path


class _MiniMonkeyPatch:
    def __init__(self) -> None:
        self._undo: list[tuple[str, Any, Any, Any]] = []

    @contextmanager
    def context(self) -> Iterator[_MiniMonkeyPatch]:
        mark = len(self._undo)
        try:
            yield self
        finally:
            while len(self._undo) > mark:
                mode, obj, key, old = self._undo.pop()
                if mode == "attr":
                    if old is _MISSING:
                        delattr(obj, key)
                    else:
                        setattr(obj, key, old)
                elif mode == "item":
                    if old is _MISSING:
                        del obj[key]
                    else:
                        obj[key] = old
                elif mode == "env":
                    if old is _MISSING:
                        os.environ.pop(key, None)
                    else:
                        os.environ[key] = old

    def setattr(self, obj: Any, name: str, value: Any) -> None:
        old = getattr(obj, name, _MISSING)
        self._undo.append(("attr", obj, name, old))
        setattr(obj, name, value)

    def setitem(self, mapping: Any, key: Any, value: Any) -> None:
        old = mapping[key] if key in mapping else _MISSING
        self._undo.append(("item", mapping, key, old))
        mapping[key] = value

    def setenv(self, name: str, value: str) -> None:
        old = os.environ[name] if name in os.environ else _MISSING
        self._undo.append(("env", None, name, old))
        os.environ[name] = value

    def delenv(self, name: str, raising: bool = True) -> None:
        if name not in os.environ:
            if raising:
                raise KeyError(name)
            return
        old = os.environ[name]
        self._undo.append(("env", None, name, old))
        del os.environ[name]


_MISSING = object()


class _MiniCapsys:
    def __init__(self) -> None:
        self._stdout = io.StringIO()
        self._stderr = io.StringIO()

    @contextmanager
    def capture(self) -> Iterator[None]:
        self._stdout = io.StringIO()
        self._stderr = io.StringIO()
        with redirect_stdout(self._stdout), redirect_stderr(self._stderr):
            yield

    def readouterr(self) -> SimpleNamespace:
        out = self._stdout.getvalue()
        err = self._stderr.getvalue()
        self._stdout.seek(0)
        self._stdout.truncate(0)
        self._stderr.seek(0)
        self._stderr.truncate(0)
        return SimpleNamespace(out=out, err=err)


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


def _shared_expectation_ids(cases_dir: Path) -> set[str]:
    py_expected = load_expected_results(cases_dir, implementation="python")
    php_expected = load_expected_results(cases_dir, implementation="php")
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
        monkeypatch = _MiniMonkeyPatch()
        capsys = _MiniCapsys()
        ctx = SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys)
        with capsys.capture():
            results = run_conformance_cases(
                cases_dir,
                ctx=ctx,
                implementation="python",
            )
    return report_to_jsonable(results)


def run_php_report(cases_dir: Path, php_runner: Path) -> dict[str, Any]:
    with TemporaryDirectory(prefix="spec-runner-parity-") as td:
        out_path = Path(td) / "php-conformance-report.json"
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
        )
        if cp.returncode != 0:
            stderr = cp.stderr.strip()
            raise RuntimeError(
                f"php conformance runner failed with exit {cp.returncode}"
                + (f": {stderr}" if stderr else "")
            )
        return json.loads(out_path.read_text(encoding="utf-8"))


def run_parity_check(config: ParityConfig) -> list[str]:
    python_payload = run_python_report(config.cases_dir)
    php_payload = run_php_report(config.cases_dir, config.php_runner)

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
    errors.extend(
        compare_parity_reports(
            python_payload,
            php_payload,
            include_ids=_shared_expectation_ids(config.cases_dir),
        )
    )
    return errors
