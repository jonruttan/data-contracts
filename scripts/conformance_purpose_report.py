#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from spec_runner.conformance_purpose import conformance_purpose_report_jsonable


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Emit conformance purpose report as JSON.")
    ap.add_argument(
        "--cases",
        default="docs/spec/conformance/cases",
        help="Path to conformance case docs directory",
    )
    ap.add_argument("--out", help="Optional output path for JSON report.")
    ns = ap.parse_args(argv)

    repo_root = Path(__file__).resolve().parents[3]
    payload = conformance_purpose_report_jsonable(Path(ns.cases), repo_root=repo_root)
    raw = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if ns.out:
        out = Path(ns.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(raw, encoding="utf-8")
        print(f"wrote {out}")
    else:
        print(raw, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
