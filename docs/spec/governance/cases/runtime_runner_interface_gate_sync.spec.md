# Governance Cases

## SRGOV-RUNTIME-CONFIG-003

```yaml spec-test
id: SRGOV-RUNTIME-CONFIG-003
title: gate scripts call runner interface boundary
purpose: Ensures gate scripts call a runner command boundary instead of hardcoding Python implementation entrypoints.
type: governance.check
check: runtime.runner_interface_gate_sync
harness:
  root: .
  runner_interface:
    required_paths:
      - scripts/runner_adapter.sh
    files:
      - scripts/ci_gate.sh
      - scripts/docs_doctor.sh
      - scripts/core_gate.sh
    required_tokens:
      - SPEC_RUNNER_BIN
      - scripts/runner_adapter.sh
    forbidden_tokens:
      - scripts/run_governance_specs.py
      - scripts/evaluate_style.py --check docs/spec
      - scripts/conformance_purpose_report.py
      - scripts/compare_conformance_parity.py
assert:
  - target: text
    must:
      - contain: ["PASS: runtime.runner_interface_gate_sync"]
```
