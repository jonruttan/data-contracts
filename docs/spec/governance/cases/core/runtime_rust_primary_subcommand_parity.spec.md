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
    adapter_path: /scripts/rust/runner_adapter.sh
    cli_main_path: /scripts/rust/spec_runner_cli/src/main.rs
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
      check: runtime.rust_adapter_subcommand_parity
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
    - runtime.rust_adapter_subcommand_parity
  target: summary_json
```
