```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-JOB-HOOKS-001
    title: rust contract.job specs adopt fail and complete lifecycle hooks
    purpose: Ensures Rust job contract-spec cases include when fail and complete dispatches with
      matching hook job metadata.
    harness:
      root: .
      check:
        profile: governance.scan
        config:
          check: runtime.contract_job_hooks_refactor_applied
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
