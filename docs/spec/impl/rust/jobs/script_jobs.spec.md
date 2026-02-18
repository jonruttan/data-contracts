# Rust Job Script Cases

## SRRUST-JOB-001

```yaml contract-spec
id: SRRUST-JOB-001
title: governance scan bundle helper smoke
purpose: Contract job entrypoint for Rust-native helper dispatch and scalar path#id job refs.
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-001'
    mode: check
    helper: helper.governance.scan_bundle
    inputs:
      path: /docs/spec
      patterns:
      - contract-spec
    outputs:
      summary: .artifacts/job-scan-summary.json
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - std.logic.neq:
    - std.object.get:
      - var: subject
      - scanned_files
    - null
```
