# Governance Cases

## SRGOV-RUST-PRIMARY-005

```yaml spec-test
id: SRGOV-RUST-PRIMARY-005
title: rust-primary adapter executes and returns deterministic smoke output
purpose: Ensures the Rust adapter is executable in governance and emits deterministic output/exit-code
  behavior for a smoke command.
type: governance.check
check: runtime.rust_adapter_exec_smoke
harness:
  root: .
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  rust_adapter_exec_smoke:
    command:
    - scripts/rust/runner_adapter.sh
    - normalize-check
    expected_exit_codes:
    - 0
    required_output_tokens: []
    forbidden_output_tokens: []
    timeout_seconds: 180
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: violation_count
  must:
  - evaluate:
    - eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
    - eq:
      - get:
        - {var: subject}
        - check_id
      - runtime.rust_adapter_exec_smoke
```
