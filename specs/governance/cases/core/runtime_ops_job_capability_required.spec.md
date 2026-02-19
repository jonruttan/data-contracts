# Governance Cases

## SRGOV-RUNTIME-JOB-DISPATCH-004

```yaml contract-spec
id: SRGOV-RUNTIME-JOB-DISPATCH-004
title: ops.job.dispatch requires ops.job capability
purpose: Ensures cases that call ops.job.dispatch declare harness.spec_lang.capabilities including
  ops.job.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.ops_job_capability_required
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    'on': violation_count
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
```
