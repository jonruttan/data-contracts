# Governance Cases

## SRGOV-RUNTIME-JOB-DISPATCH-002

```yaml contract-spec
id: SRGOV-RUNTIME-JOB-DISPATCH-002
title: contract.job harness uses jobs metadata map
purpose: Ensures contract.job cases declare helper metadata under harness.jobs entries.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.harness_jobs_metadata_map_required
contract:
  defaults:
    class: MUST
  imports:
    subject:
      from: artifact
      key: violation_count
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
```
