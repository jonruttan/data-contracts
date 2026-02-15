# Governance Cases

## SRGOV-RUST-PRIMARY-007

```yaml spec-test
id: SRGOV-RUST-PRIMARY-007
title: rust adapter and rust cli expose the same runner subcommand set
purpose: Ensures the shell adapter and Rust CLI subcommand surfaces stay synchronized to prevent runtime interface drift.
type: governance.check
check: runtime.rust_adapter_subcommand_parity
harness:
  root: .
  rust_subcommand_parity:
    adapter_path: scripts/rust/runner_adapter.sh
    cli_main_path: scripts/rust/spec_runner_cli/src/main.rs
  policy_evaluate:
  - is_empty:
    - get:
      - subject: []
      - violations
assert:
- target: violation_count
  must:
  - evaluate:
    - eq:
      - subject: []
      - 0
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - subject: []
        - passed
      - true
    - eq:
      - get:
        - subject: []
        - check_id
      - runtime.rust_adapter_subcommand_parity
```
