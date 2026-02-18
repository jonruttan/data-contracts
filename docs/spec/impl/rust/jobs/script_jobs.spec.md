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

## SRRUST-JOB-002

```yaml contract-spec
id: SRRUST-JOB-002
title: conformance parity command via contract.job
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-002'
    mode: check
    helper: helper.parity.run_conformance
    inputs:
      cases: docs/spec/conformance/cases
      php_runner: scripts/php/conformance_runner.php
      out: .artifacts/conformance-parity.json
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - ok
    - true
```

## SRRUST-JOB-003

```yaml contract-spec
id: SRRUST-JOB-003
title: perf smoke command via contract.job
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-003'
    mode: warn
    helper: helper.perf.run_smoke
    inputs:
      report_out: .artifacts/perf-smoke-report.json
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - ok
    - true
```
