# Governance Cases

## SRGOV-RUNTIME-JOB-DISPATCH-001

```yaml contract-spec
id: SRGOV-RUNTIME-JOB-DISPATCH-001
title: contract.job dispatch must be declared in contract
purpose: Ensures contract.job cases dispatch jobs via ops.job.dispatch in contract assertions.
type: governance.check
check: runtime.contract_job_dispatch_in_contract_required
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
