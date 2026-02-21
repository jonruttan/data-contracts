```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-JOB-DISPATCH-004
    title: ops.job.dispatch requires ops.job capability
    purpose: Ensures cases that call ops.job.dispatch declare harness.spec_lang.capabilities including
      ops.job.
    harness:
      root: .
      check:
        profile: governance.scan
        config:
          check: runtime.ops_job_capability_required
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
