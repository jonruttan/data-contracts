```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-STATUS-005
    title: missing compatibility status remains visible
    purpose: Ensures missing compatibility status is visible and policy-scored in matrix output.
    harness:
      root: .
      status_visibility:
        path: /scripts/runner_status_ingest.sh
        required_tokens:
        - freshness_state
        - missing
        - policy_effect
        - non_blocking_fail
      check:
        profile: governance.scan
        config:
          check: runtime.compatibility_missing_status_visibility_required
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

