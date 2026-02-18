# Governance Cases

## SRGOV-RUNTIME-JOB-DISPATCH-003

```yaml contract-spec
id: SRGOV-RUNTIME-JOB-DISPATCH-003
title: contract.job legacy harness.job fields are forbidden
purpose: Enforces hard-cut removal of singular harness.job and nested ref declarations.
type: governance.check
check: runtime.harness_job_legacy_forbidden
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
