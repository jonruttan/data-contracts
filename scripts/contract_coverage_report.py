#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from spec_runner.contract_governance import contract_coverage_jsonable


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=(
            "Emit optional spec_runner contract coverage report as JSON "
            "(artifact/reporting helper; not a primary gate)."
        )
    )
    ap.add_argument("--out", help="Optional output path for JSON report.")
    ns = ap.parse_args(argv)

    repo_root = Path(__file__).resolve().parents[1]
    payload = contract_coverage_jsonable(repo_root)
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
