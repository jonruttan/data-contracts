```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-ENTRY-002
    title: public runner defaults to rust mode
    purpose: Ensures the canonical runner launcher targets the rust runtime lane and
      forbids python runtime dispatch.
    harness:
      root: .
      public_runner_default:
        path: /scripts/runner_bin.sh
        required_tokens:
        - dc-runner-rust
        - unsupported platform
        - dc-runner-rust release artifact
        forbidden_tokens:
        - dc-runner-python
      check:
        profile: governance.scan
        config:
          check: runtime.public_runner_default_rust
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
            - check_id
          - runtime.public_runner_default_rust
        - std.logic.eq:
          - std.object.get:
            - {var: summary_json}
            - passed
          - true
        imports:
        - from: artifact
          names:
          - summary_json
```
