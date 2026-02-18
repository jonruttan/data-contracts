# Governance Cases

## SRGOV-RUST-PRIMARY-005

```yaml contract-spec
id: SRGOV-RUST-PRIMARY-005
title: rust-primary adapter executes and returns deterministic smoke output
purpose: Ensures the Rust adapter is executable in governance and emits deterministic output/exit-code
  behavior for a smoke command.
type: contract.check
harness:
  root: .
  rust_adapter_exec_smoke:
    command:
    - runners/rust/runner_adapter.sh
    - critical-gate
    expected_exit_codes:
    - 0
    required_output_tokens:
    - critical-gate-summary.json
    forbidden_output_tokens: []
    timeout_seconds: 30
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
      check: runtime.rust_adapter_exec_smoke
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
    - runtime.rust_adapter_exec_smoke
  target: summary_json
```
