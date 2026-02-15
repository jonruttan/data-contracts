# Governance Cases

## SRGOV-RUST-PRIMARY-004

```yaml spec-test
id: SRGOV-RUST-PRIMARY-004
title: rust-primary gate path includes shared-capability parity step
purpose: Ensures gate orchestration keeps conformance parity as part of Rust-primary-compatible gate flow.
type: governance.check
check: runtime.runner_interface_gate_sync
harness:
  root: .
  runner_interface:
    required_paths:
    - scripts/runner_adapter.sh
    - scripts/rust/runner_adapter.sh
    files:
    - scripts/ci_gate_summary.py
    required_tokens:
    - conformance-parity
    forbidden_tokens: []
  policy_evaluate:
  - is_empty:
    - {get: [{subject: []}, violations]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{subject: []}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{subject: []}, passed]}
      - true
    - eq:
      - {get: [{subject: []}, check_id]}
      - runtime.runner_interface_gate_sync
```
