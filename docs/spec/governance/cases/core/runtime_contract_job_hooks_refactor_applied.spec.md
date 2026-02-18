# Governance Cases

## SRGOV-RUNTIME-JOB-HOOKS-001

```yaml contract-spec
id: SRGOV-RUNTIME-JOB-HOOKS-001
title: rust contract.job specs adopt fail and complete lifecycle hooks
purpose: Ensures Rust job contract-spec cases include when fail and complete dispatches
  with matching hook job metadata.
type: governance.check
check: runtime.contract_job_hooks_refactor_applied
harness:
  root: .
contract:
- id: assert_1
  class: MUST
  target: violation_count
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
```
