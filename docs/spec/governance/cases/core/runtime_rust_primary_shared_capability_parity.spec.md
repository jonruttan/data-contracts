# Governance Cases

## SRGOV-RUST-PRIMARY-004

```yaml contract-spec
id: SRGOV-RUST-PRIMARY-004
title: rust-primary gate path includes shared-capability parity step
purpose: Ensures gate orchestration keeps conformance parity as part of Rust-primary-compatible
  gate flow.
type: contract.check
harness:
  root: .
  runner_interface:
    required_paths:
    - /scripts/runner_adapter.sh
    - /scripts/rust/runner_adapter.sh
    files:
    - scripts/ci_gate_summary.py
    required_tokens:
    - conformance-parity
    forbidden_tokens: []
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: runtime.runner_interface_gate_sync
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - passed
    - true
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - check_id
    - runtime.runner_interface_gate_sync
  target: summary_json
```
