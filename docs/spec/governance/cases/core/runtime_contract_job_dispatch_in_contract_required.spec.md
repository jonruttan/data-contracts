# Governance Cases

## SRGOV-RUNTIME-JOB-DISPATCH-001

```yaml contract-spec
id: SRGOV-RUNTIME-JOB-DISPATCH-001
title: contract.job dispatch must be declared in contract
purpose: Ensures contract.job cases dispatch jobs via ops.job.dispatch in contract assertions.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.contract_job_dispatch_in_contract_required
contract:
- id: assert_1
  class: MUST
  target: violation_count
  asserts:
  - evaluate:
      lit:
        lit:
          std.logic.eq:
          - {var: subject}
          - 0
```
