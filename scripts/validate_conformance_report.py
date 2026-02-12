#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from spec_runner.conformance import validate_conformance_report_payload


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Validate a conformance JSON report payload.")
    ap.add_argument("report", help="Path to report JSON file")
    ns = ap.parse_args(argv)

    p = Path(ns.report)
    payload = json.loads(p.read_text(encoding="utf-8"))
    errs = validate_conformance_report_payload(payload)
    if errs:
        for e in errs:
            print(f"ERROR: {e}", file=sys.stderr)
        return 1
    print(f"OK: valid conformance report ({p})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
