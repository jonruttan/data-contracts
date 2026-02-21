```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUST-PRIMARY-001
    title: rust-primary ci lane runs core gate via runner interface
    purpose: Ensures CI includes a Rust-primary lane that executes core gate through SPEC_RUNNER_BIN.
    harness:
      root: .
      runner_interface_ci_lane:
        workflow: .github/workflows/ci.yml
        required_tokens:
        - 'core-gate-rust-adapter:'
        - 'SPEC_RUNNER_BIN: ./scripts/runner_bin.sh'
        - 'run: ./scripts/ci_gate.sh'
      check:
        profile: governance.scan
        config:
          check: runtime.runner_interface_ci_lane
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
          - runtime.runner_interface_ci_lane
        imports:
        - from: artifact
          names:
          - summary_json
```
