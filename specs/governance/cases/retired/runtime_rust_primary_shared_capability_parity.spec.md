```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUST-PRIMARY-004
  title: rust-primary gate path includes shared-capability parity step
  purpose: Ensures gate orchestration keeps conformance parity as part of Rust-primary-compatible gate flow.
  harness:
    root: "."
    runner_interface:
      required_paths:
      - "/scripts/runner_bin.sh"
      - "/dc-runner-rust"
      files:
      - dc-runner-python
      required_tokens:
      - conformance-parity
      forbidden_tokens: []
    check:
      profile: governance.scan
      config:
        check: runtime.runner_interface_gate_sync
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
        - runtime.runner_interface_gate_sync
      imports:
      - from: artifact
        names:
        - summary_json
```
