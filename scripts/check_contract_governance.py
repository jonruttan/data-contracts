#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

from spec_runner.contract_governance import check_contract_governance


def main() -> int:
    print(
        "INFO: check_contract_governance.py is an optional wrapper. "
        "Primary enforcement runs via scripts/run_governance_specs.py (contract.governance_check)."
    )
    repo_root = Path(__file__).resolve().parents[1]
    errs = check_contract_governance(repo_root)
    if errs:
        for e in errs:
            print(f"ERROR: {e}", file=sys.stderr)
        return 1
    print("OK: contract governance checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
