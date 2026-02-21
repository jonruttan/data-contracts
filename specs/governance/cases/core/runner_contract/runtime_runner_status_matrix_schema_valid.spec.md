```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-STATUS-002
    title: runner status matrix schema is defined
    purpose: Ensures aggregated status matrix contract shape is declared for governance and docs.
    harness:
      root: .
      runner_status_matrix_schema:
        path: /specs/schema/runner_status_matrix_v1.yaml
        required_tokens:
        - type: runtime.runner_status_matrix
        - matrix_rows
        - freshness_state
        - policy_effect
      check:
        profile: governance.scan
        config:
          check: runtime.runner_status_matrix_schema_valid
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

