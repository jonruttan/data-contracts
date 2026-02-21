```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-PROFILE-REDACT-001
    title: run trace redaction policy prevents secret leakage
    purpose: Ensures profiling env metadata does not store raw values and trace payloads do not
      include common secret-like tokens.
    harness:
      root: .
      profiling_redaction:
        trace_path: specs/governance/cases/fixtures/run_trace_sample.json
      check:
        profile: governance.scan
        config:
          check: runtime.profiling_redaction_policy
      use:
      - ref: /specs/libraries/policy/policy_assertions.spec.md
        as: lib_policy_core_spec
        symbols:
        - policy.assert.no_violations
        - policy.assert.summary_passed
        - policy.assert.summary_check_id
        - policy.assert.scan_pass
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - violation_count
      predicates:
      - id: assert_1
        assert:
          call:
          - {var: policy.assert.no_violations}
          - std.object.assoc:
            - violation_count
            - {var: violation_count}
            - lit: {}
```

