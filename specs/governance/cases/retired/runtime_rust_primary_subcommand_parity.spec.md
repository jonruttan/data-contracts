```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUST-PRIMARY-007
  title: rust adapter and rust cli expose the same runner subcommand set
  purpose: Ensures the shell adapter and Rust CLI subcommand surfaces stay synchronized to prevent runtime interface drift.
  harness:
    root: "."
    rust_subcommand_parity:
      adapter_path: "/dc-runner-rust"
      cli_main_path: "/dc-runner-rust"
    check:
      profile: governance.scan
      config:
        check: runtime.required_lane_adapter_subcommand_parity
    use:
    - ref: "/specs/libraries/policy/policy_core.spec.md"
      as: lib_policy_core_spec
      symbols:
      - policy.pass_when_no_violations
  clauses:
    imports:
    - from: artifact
      names:
      - violation_count
    predicates:
    - id: assert_1
      assert:
        std.logic.eq:
        - var: violation_count
        - 0
    - id: assert_2
      assert:
      - std.logic.eq:
        - std.object.get:
          - var: summary_json
          - passed
        - true
      - std.logic.eq:
        - std.object.get:
          - var: summary_json
          - check_id
        - runtime.required_lane_adapter_subcommand_parity
      imports:
      - from: artifact
        names:
        - summary_json
```
