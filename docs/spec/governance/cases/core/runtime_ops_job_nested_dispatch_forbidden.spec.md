# Governance Cases

## SRGOV-RUNTIME-JOB-DISPATCH-005

```yaml contract-spec
id: SRGOV-RUNTIME-JOB-DISPATCH-005
title: ops.job.dispatch nested dispatch is forbidden
purpose: Ensures runtime emits deterministic failure token when nested dispatch is attempted.
type: contract.check
harness:
  root: .
  ops_job_nested_dispatch:
    path: /scripts/rust/spec_runner_cli/src/spec_lang.rs
    required_tokens:
    - runtime.dispatch.nested_forbidden
  check:
    profile: governance.scan
    config:
      check: runtime.ops_job_nested_dispatch_forbidden
contract:
- id: assert_1
  class: MUST
  target: violation_count
  asserts:
  - evaluate:
    - lit:
        std.logic.eq:
        - {var: subject}
        - 0
```
