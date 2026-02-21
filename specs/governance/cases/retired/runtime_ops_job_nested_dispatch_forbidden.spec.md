```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-JOB-DISPATCH-005
    title: ops.job.dispatch nested dispatch is forbidden
    purpose: Ensures runtime emits deterministic failure token when nested dispatch is attempted.
    harness:
      root: .
      ops_job_nested_dispatch:
        path: /dc-runner-rust
        required_tokens:
        - runtime.dispatch.nested_forbidden
      check:
        profile: governance.scan
        config:
          check: runtime.ops_job_nested_dispatch_forbidden
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
