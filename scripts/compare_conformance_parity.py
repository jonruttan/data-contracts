#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

from spec_runner.conformance_parity import ParityConfig, build_parity_artifact, run_parity_check


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
    ns = ap.parse_args(argv)
    out_path = Path(str(ns.out)).resolve() if str(ns.out).strip() else None

    if shutil.which("php") is None:
        msg = "php executable not found in PATH"
        if out_path is not None:
            _write_artifact(out_path, build_parity_artifact([msg]))
        print(f"ERROR: {msg}", file=sys.stderr)
        return 2

    cfg = ParityConfig(
        cases_dir=Path(ns.cases),
        php_runner=Path(ns.php_runner),
        python_runner=Path(ns.python_runner),
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

    print(f"OK: conformance parity matched for {cfg.cases_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
