# Governance Cases

## SRGOV-RUST-PRIMARY-001

```yaml spec-test
id: SRGOV-RUST-PRIMARY-001
title: rust-primary ci lane runs core gate via runner interface
purpose: Ensures CI includes a Rust-primary lane that executes core gate through SPEC_RUNNER_BIN.
type: governance.check
check: runtime.runner_interface_ci_lane
harness:
  root: .
  runner_interface_ci_lane:
    workflow: .github/workflows/ci.yml
    required_tokens:
    - 'core-gate-rust-adapter:'
    - 'SPEC_RUNNER_BIN: ./scripts/rust/runner_adapter.sh'
    - 'run: ./scripts/core_gate.sh'
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
      - runtime.runner_interface_ci_lane
```
