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
    - /runners/public/runner_adapter.sh
    - /runners/rust/runner_adapter.sh
    files:
    - runners/python/spec_runner/script_runtime_commands.py
    required_tokens:
    - conformance-parity
    forbidden_tokens: []
  check:
    profile: governance.scan
    config:
      check: runtime.runner_interface_gate_sync
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    target: violation_count
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
  - id: assert_2
    target: summary_json
    assert:
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
```
