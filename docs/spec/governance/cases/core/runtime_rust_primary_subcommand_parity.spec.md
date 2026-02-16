# Governance Cases

## SRGOV-RUST-PRIMARY-007

```yaml spec-test
id: SRGOV-RUST-PRIMARY-007
title: rust adapter and rust cli expose the same runner subcommand set
purpose: Ensures the shell adapter and Rust CLI subcommand surfaces stay synchronized to prevent
  runtime interface drift.
type: governance.check
check: runtime.rust_adapter_subcommand_parity
harness:
  root: .
  rust_subcommand_parity:
    adapter_path: /scripts/rust/runner_adapter.sh
    cli_main_path: /scripts/rust/spec_runner_cli/src/main.rs
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
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: must
  checks:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - runtime.rust_adapter_subcommand_parity
  target: summary_json
```
