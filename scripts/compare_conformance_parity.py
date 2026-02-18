#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

from spec_runner.conformance import ConformanceResult, compare_conformance_results, load_expected_results
from spec_runner.conformance_parity import (
    ParityConfig,
    build_parity_artifact,
    run_parity_check,
    run_python_report,
)


def _write_artifact(path: Path, artifact: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(artifact, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Run Python/PHP conformance and report normalized parity diffs by case id."
    )
    ap.add_argument(
        "--cases",
        default="docs/spec/conformance/cases",
        help="Path to conformance case docs directory",
    )
    ap.add_argument(
        "--php-runner",
        default="scripts/php/conformance_runner.php",
        help="Path to PHP conformance runner script",
    )
    ap.add_argument(
        "--python-runner",
        default="scripts/python/conformance_runner.py",
        help="Path to Python conformance runner script",
    )
    ap.add_argument(
        "--out",
        default="",
        help="Optional path to write JSON parity artifact",
    )
    ap.add_argument(
        "--case-formats",
        default="md",
        help="Comma-separated case formats to load (md,yaml,json). Default: md",
    )
    ap.add_argument(
        "--php-timeout-seconds",
        type=int,
        default=30,
        help="Timeout in seconds for the PHP parity runner subprocess (default: 30)",
    )
    ap.add_argument(
        "--python-timeout-seconds",
        type=int,
        default=30,
        help="Timeout in seconds for the Python parity runner subprocess (default: 30)",
    )
    ap.add_argument(
        "--python-only",
        action="store_true",
        help="Validate only Python conformance against expected results (skip PHP parity).",
    )
    ns = ap.parse_args(argv)
    out_path = Path(str(ns.out)).resolve() if str(ns.out).strip() else None

    if not ns.python_only and shutil.which("php") is None:
        msg = "php executable not found in PATH"
        if out_path is not None:
            _write_artifact(out_path, build_parity_artifact([msg]))
        print(f"ERROR: {msg}", file=sys.stderr)
        return 2

    case_formats = {x.strip() for x in str(ns.case_formats).split(",") if x.strip()}
    if not case_formats:
        msg = "--case-formats requires at least one format"
        if out_path is not None:
            _write_artifact(out_path, build_parity_artifact([msg]))
        print(f"ERROR: {msg}", file=sys.stderr)
        return 2

    if ns.python_only:
        try:
            python_payload = run_python_report(
                Path(ns.cases),
                Path(ns.python_runner),
                case_formats=case_formats,
                timeout_seconds=int(ns.python_timeout_seconds),
            )
            expected = load_expected_results(
                Path(ns.cases),
                implementation="python",
                case_formats=case_formats,
            )
            python_actual = [
                ConformanceResult(
                    id=str(r.get("id", "")),
                    status=str(r.get("status", "")),
                    category=None if r.get("category") is None else str(r.get("category")),
                    message=None if r.get("message") is None else str(r.get("message")),
                )
                for r in python_payload.get("results", [])
            ]
            errs = [f"python vs expected: {e}" for e in compare_conformance_results(expected, python_actual)]
        except RuntimeError as e:
            if out_path is not None:
                _write_artifact(out_path, build_parity_artifact([str(e)]))
            print(f"ERROR: {e}", file=sys.stderr)
            return 1
    else:
        cfg = ParityConfig(
            cases_dir=Path(ns.cases),
            php_runner=Path(ns.php_runner),
            python_runner=Path(ns.python_runner),
            case_formats=case_formats,
            python_timeout_seconds=int(ns.python_timeout_seconds),
            php_timeout_seconds=int(ns.php_timeout_seconds),
        )
        try:
            errs = run_parity_check(cfg)
        except RuntimeError as e:
            if out_path is not None:
                _write_artifact(out_path, build_parity_artifact([str(e)]))
            print(f"ERROR: {e}", file=sys.stderr)
            return 1
    if out_path is not None:
        _write_artifact(out_path, build_parity_artifact(errs))
    if errs:
        print("ERROR: conformance parity check failed", file=sys.stderr)
        for e in errs:
            print(f"- {e}", file=sys.stderr)
        return 1

    print(f"OK: conformance parity matched for {Path(ns.cases)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
