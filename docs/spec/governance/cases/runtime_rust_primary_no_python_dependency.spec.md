# Governance Cases

## SRGOV-RUST-PRIMARY-002

```yaml spec-test
id: SRGOV-RUST-PRIMARY-002
title: rust-primary gate scripts avoid direct python runner entrypoints
purpose: Ensures gate scripts stay runner-interface based and do not hardcode Python runner commands.
type: governance.check
check: runtime.runner_interface_gate_sync
harness:
  root: .
  runner_interface:
    required_paths:
    - scripts/runner_adapter.sh
    - scripts/rust/runner_adapter.sh
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
  policy_evaluate:
  - is_empty:
    - get:
      - subject: []
      - violations
assert:
- target: text
  must:
  - contain:
    - 'PASS: runtime.runner_interface_gate_sync'
```
