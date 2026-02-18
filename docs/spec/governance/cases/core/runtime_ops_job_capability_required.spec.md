# Governance Cases

## SRGOV-RUNTIME-JOB-DISPATCH-004

```yaml contract-spec
id: SRGOV-RUNTIME-JOB-DISPATCH-004
title: ops.job.dispatch requires ops.job capability
purpose: Ensures cases that call ops.job.dispatch declare harness.spec_lang.capabilities including ops.job.
type: governance.check
check: runtime.ops_job_capability_required
harness:
  root: .
contract:
- id: assert_1
  class: must
  target: violation_count
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
```
