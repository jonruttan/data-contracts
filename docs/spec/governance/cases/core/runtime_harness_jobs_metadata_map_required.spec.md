# Governance Cases

## SRGOV-RUNTIME-JOB-DISPATCH-002

```yaml contract-spec
id: SRGOV-RUNTIME-JOB-DISPATCH-002
title: contract.job harness uses jobs metadata map
purpose: Ensures contract.job cases declare helper metadata under harness.jobs entries.
type: governance.check
check: runtime.harness_jobs_metadata_map_required
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
