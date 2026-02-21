```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUST-PRIMARY-005
  title: rust-primary adapter executes and returns deterministic smoke output
  purpose: Ensures the Rust adapter is executable in governance and emits deterministic output/exit-code behavior for a smoke command.
  harness:
    root: "."
    rust_adapter_exec_smoke:
      command:
      - dc-runner-rust
      - critical-gate
      expected_exit_codes:
      - 0
      required_output_tokens:
      - critical-gate-summary.json
      forbidden_output_tokens: []
      timeout_seconds: 30
    check:
      profile: governance.scan
      config:
        check: runtime.required_lane_adapter_exec_smoke
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
        - runtime.required_lane_adapter_exec_smoke
      imports:
      - from: artifact
        names:
        - summary_json
```
