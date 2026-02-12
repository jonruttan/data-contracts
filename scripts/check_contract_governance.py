#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

from spec_runner.contract_governance import check_contract_governance


def main() -> int:
    repo_root = Path(__file__).resolve().parents[3]
    errs = check_contract_governance(repo_root)
    if errs:
        for e in errs:
            print(f"ERROR: {e}", file=sys.stderr)
        return 1
    print("OK: contract governance checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
