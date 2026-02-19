# Governance Cases

## SRGOV-RUST-PRIMARY-007

```yaml contract-spec
id: SRGOV-RUST-PRIMARY-007
title: rust adapter and rust cli expose the same runner subcommand set
purpose: Ensures the shell adapter and Rust CLI subcommand surfaces stay synchronized to prevent
  runtime interface drift.
type: contract.check
harness:
  root: .
  rust_subcommand_parity:
    adapter_path: /runners/rust/runner_adapter.sh
    cli_main_path: /runners/rust/spec_runner_cli/src/main.rs
  check:
    profile: governance.scan
    config:
      check: runtime.rust_adapter_subcommand_parity
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - violation_count
    as:
      violation_count: subject
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
  - id: assert_2
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
      - runtime.rust_adapter_subcommand_parity
    imports:
    - from: artifact
      names:
      - summary_json
      as:
        summary_json: subject
```
