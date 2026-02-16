# Governance Cases

## SRGOV-RUST-PRIMARY-006

```yaml spec-test
id: SRGOV-RUST-PRIMARY-006
title: rust-primary adapter executes success-path smoke command deterministically
purpose: Ensures the Rust adapter can execute a supported success-path command with deterministic
  success output and exit-code behavior.
type: governance.check
check: runtime.rust_adapter_exec_smoke
harness:
  root: .
  rust_adapter_exec_smoke:
    command:
    - scripts/rust/runner_adapter.sh
    - style-check
    expected_exit_codes:
    - 0
    required_output_tokens:
    - 'OK: evaluate style formatting is canonical'
    forbidden_output_tokens:
    - unsupported runner adapter subcommand
    - rust runner adapter subcommand not yet implemented
    timeout_seconds: 180
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
      exports:
        policy.pass_when_no_violations:
          from: library.symbol
          path: /policy.pass_when_no_violations
          required: true
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
  target: violation_count
- id: assert_2
  class: must
  checks:
  - evaluate:
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
