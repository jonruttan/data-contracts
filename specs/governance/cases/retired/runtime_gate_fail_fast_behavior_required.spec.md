```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-FAILFAST-001
    title: gate summary enforces fail-fast orchestration semantics
    purpose: Ensures CI gate orchestration supports deterministic fail-fast with explicit abort
      markers.
    harness:
      root: .
      gate_fail_fast:
        files:
        - /dc-runner-python
        - /dc-runner-rust
        required_tokens:
        - fail_fast
        - gate.fail_fast.abort
        - fail_fast.after_failure
      check:
        profile: governance.scan
        config:
          check: runtime.gate_fail_fast_behavior_required
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
