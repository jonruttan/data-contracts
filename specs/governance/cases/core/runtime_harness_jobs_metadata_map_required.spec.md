```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-JOB-DISPATCH-002
    title: contract.job harness uses jobs metadata list
    purpose: Ensures contract.job cases declare helper metadata under harness.jobs entries.
    harness:
      root: .
      check:
        profile: governance.scan
        config:
          check: runtime.harness_jobs_metadata_list_required
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
