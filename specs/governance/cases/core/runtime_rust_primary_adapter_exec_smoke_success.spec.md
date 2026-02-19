# Governance Cases

## SRGOV-RUST-PRIMARY-006

```yaml contract-spec
id: SRGOV-RUST-PRIMARY-006
title: rust-primary adapter executes success-path smoke command deterministically
purpose: Ensures the Rust adapter can execute a supported success-path command with deterministic
  success output and exit-code behavior.
type: contract.check
harness:
  root: .
  rust_adapter_exec_smoke:
    command:
    - runners/rust/spec_runner_cli/target/debug/spec_runner_cli
    - style-check
    expected_exit_codes:
    - 0
    required_output_tokens:
    - 'OK: evaluate style formatting is canonical'
    forbidden_output_tokens:
    - unsupported runner adapter subcommand
    - rust runner adapter subcommand not yet implemented
    timeout_seconds: 180
  check:
    profile: governance.scan
    config:
      check: runtime.rust_adapter_exec_smoke
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
      - runtime.rust_adapter_exec_smoke
```
