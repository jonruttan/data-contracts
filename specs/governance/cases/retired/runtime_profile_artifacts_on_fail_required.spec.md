```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-FAILFAST-003
    title: gate failures emit profile artifacts when profile-on-fail is enabled
    purpose: Ensures failure paths generate deterministic run-trace and run-trace-summary artifacts.
    harness:
      root: .
      profile_on_fail:
        files:
        - /dc-runner-python
        - /dc-runner-rust
        required_tokens:
        - profile-on-fail
        - .artifacts/run-trace.json
        - .artifacts/run-trace-summary.md
      check:
        profile: governance.scan
        config:
          check: runtime.profile_artifacts_on_fail_required
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
```
