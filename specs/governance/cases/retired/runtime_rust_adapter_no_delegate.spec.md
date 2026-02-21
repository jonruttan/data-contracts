```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-CONFIG-006R
    title: rust adapter does not delegate to python shell adapter
    purpose: Ensures dc-runner-rust invokes the Rust CLI directly and does not
      call scripts/runner_bin.sh.
    harness:
      root: .
      rust_adapter:
        path: /dc-runner-rust
        required_tokens:
        - spec_runner_cli
        - cargo run --quiet
        forbidden_tokens:
        - scripts/runner_bin.sh
      check:
        profile: governance.scan
        config:
          check: runtime.required_lane_adapter_no_delegate
      use:
      - ref: /specs/libraries/policy/policy_core.spec.md
        as: lib_policy_core_spec
        symbols:
        - policy.pass_when_no_violations
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - violation_count
      predicates:
      - id: assert_1
        assert:
          std.logic.eq:
          - {var: violation_count}
          - 0
      - id: assert_2
        assert:
        - std.logic.eq:
          - std.object.get:
            - {var: summary_json}
            - passed
          - true
        - std.logic.eq:
          - std.object.get:
            - {var: summary_json}
            - check_id
          - runtime.required_lane_adapter_no_delegate
        imports:
        - from: artifact
          names:
          - summary_json
```
