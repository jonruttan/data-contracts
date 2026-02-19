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
    path: /runners/rust/spec_runner_cli/src/spec_lang.rs
    required_tokens:
    - runtime.dispatch.nested_forbidden
  check:
    profile: governance.scan
    config:
      check: runtime.ops_job_nested_dispatch_forbidden
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    target: violation_count
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
```
