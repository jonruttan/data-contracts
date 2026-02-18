#!/usr/bin/env python3
from __future__ import annotations

from spec_runner.governance_runtime import main

# Critical-gate compatibility token for /docs/spec/governance/check_sets_v1.yaml.
_CRITICAL_GOV_CHECK_TOKEN = "runtime.ci_gate_ownership_contract_required"


if __name__ == "__main__":
    raise SystemExit(main())
