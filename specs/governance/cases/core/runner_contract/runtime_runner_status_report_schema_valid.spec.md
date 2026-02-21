```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-STATUS-001
    title: runner status report schema is defined
    purpose: Ensures runner status exchange producer payload shape is declared and stable.
    harness:
      root: .
      runner_status_report_schema:
        path: /specs/schema/runner_status_report_v1.yaml
        required_tokens:
        - type: runtime.runner_status_report
        - runner_id
        - implementation_repo
        - generated_at
        - fresh_until
        - command_results
        - artifact_refs
      check:
        profile: governance.scan
        config:
          check: runtime.runner_status_report_schema_valid
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

