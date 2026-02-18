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

## SRRUST-JOB-004

```yaml contract-spec
id: SRRUST-JOB-004
title: schema registry build via contract.job
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-004'
    mode: build
    helper: helper.schema.registry_report
    inputs:
      format: json
      out: .artifacts/schema_registry_report.json
      check: false
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

## SRRUST-JOB-005

```yaml contract-spec
id: SRRUST-JOB-005
title: schema registry check via contract.job
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-005'
    mode: check
    helper: helper.schema.registry_report
    inputs:
      format: json
      out: .artifacts/schema_registry_report.json
      check: true
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

## SRRUST-JOB-006

```yaml contract-spec
id: SRRUST-JOB-006
title: docs lint via contract.job
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-006'
    mode: lint
    helper: helper.docs.lint
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

## SRRUST-JOB-007

```yaml contract-spec
id: SRRUST-JOB-007
title: docs generate build via contract.job
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-007'
    mode: build
    helper: helper.docs.generate_all
    inputs:
      action: build
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

## SRRUST-JOB-008

```yaml contract-spec
id: SRRUST-JOB-008
title: docs generate check via contract.job
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-008'
    mode: check
    helper: helper.docs.generate_all
    inputs:
      action: check
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

## SRRUST-JOB-009

```yaml contract-spec
id: SRRUST-JOB-009
title: docs build reference book via contract.job
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-009'
    mode: build
    helper: helper.docs.generate_all
    inputs:
      action: build
      surface: reference_book
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

## SRRUST-JOB-010

```yaml contract-spec
id: SRRUST-JOB-010
title: docs build check reference book via contract.job
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-010'
    mode: check
    helper: helper.docs.generate_all
    inputs:
      action: check
      surface: reference_book
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

## SRRUST-JOB-011

```yaml contract-spec
id: SRRUST-JOB-011
title: docs graph export via contract.job
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-011'
    mode: build
    helper: helper.docs.generate_all
    inputs:
      action: build
      surface: docs_graph
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
