#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from spec_runner.conformance_parity import ParityConfig, run_parity_check


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
    ns = ap.parse_args(argv)

    if shutil.which("php") is None:
        print("ERROR: php executable not found in PATH", file=sys.stderr)
        return 2

    cfg = ParityConfig(
        cases_dir=Path(ns.cases),
        php_runner=Path(ns.php_runner),
    )
    try:
        errs = run_parity_check(cfg)
    except RuntimeError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1
    if errs:
        print("ERROR: conformance parity check failed", file=sys.stderr)
        for e in errs:
            print(f"- {e}", file=sys.stderr)
        return 1

    print(f"OK: conformance parity matched for {cfg.cases_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
