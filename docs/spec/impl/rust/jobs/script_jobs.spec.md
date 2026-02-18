# Rust Job Script Cases

## SRRUST-JOB-001

```yaml contract-spec
id: SRRUST-JOB-001
title: governance scan bundle helper smoke
purpose: Contract job entrypoint for Rust-native helper dispatch and scalar path#id
  job refs.
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
    - ops.job
  jobs:
    main:
      mode: check
      helper: helper.governance.scan_bundle
      inputs:
        path: /docs/spec
        patterns:
        - contract-spec
      outputs:
        summary: .artifacts/job-scan-summary.json
    on_fail:
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/SRRUST-JOB-001.fail.json
        format: json
        report_name: SRRUST-JOB-001.fail
    on_complete:
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/SRRUST-JOB-001.complete.json
        format: json
        report_name: SRRUST-JOB-001.complete
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - ops.job.dispatch:
    - main
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
    - ops.job
  jobs:
    main:
      mode: check
      helper: helper.parity.run_conformance
      inputs:
        cases: docs/spec/conformance/cases
        php_runner: scripts/php/conformance_runner.php
        out: .artifacts/conformance-parity.json
    on_fail:
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/SRRUST-JOB-002.fail.json
        format: json
        report_name: SRRUST-JOB-002.fail
    on_complete:
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/SRRUST-JOB-002.complete.json
        format: json
        report_name: SRRUST-JOB-002.complete
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - ops.job.dispatch:
    - main
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
    - ops.job
  jobs:
    main:
      mode: warn
      helper: helper.perf.run_smoke
      inputs:
        report_out: .artifacts/perf-smoke-report.json
    on_fail:
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/SRRUST-JOB-003.fail.json
        format: json
        report_name: SRRUST-JOB-003.fail
    on_complete:
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/SRRUST-JOB-003.complete.json
        format: json
        report_name: SRRUST-JOB-003.complete
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - ops.job.dispatch:
    - main
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
    - ops.job
  jobs:
    main:
      mode: build
      helper: helper.schema.registry_report
      inputs:
        format: json
        out: .artifacts/schema_registry_report.json
        check: false
    on_fail:
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/SRRUST-JOB-004.fail.json
        format: json
        report_name: SRRUST-JOB-004.fail
    on_complete:
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/SRRUST-JOB-004.complete.json
        format: json
        report_name: SRRUST-JOB-004.complete
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - ops.job.dispatch:
    - main
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
    - ops.job
  jobs:
    main:
      mode: check
      helper: helper.schema.registry_report
      inputs:
        format: json
        out: .artifacts/schema_registry_report.json
        check: true
    on_fail:
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/SRRUST-JOB-005.fail.json
        format: json
        report_name: SRRUST-JOB-005.fail
    on_complete:
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/SRRUST-JOB-005.complete.json
        format: json
        report_name: SRRUST-JOB-005.complete
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - ops.job.dispatch:
    - main
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
    - ops.job
  jobs:
    main:
      mode: lint
      helper: helper.docs.lint
    on_fail:
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/SRRUST-JOB-006.fail.json
        format: json
        report_name: SRRUST-JOB-006.fail
    on_complete:
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/SRRUST-JOB-006.complete.json
        format: json
        report_name: SRRUST-JOB-006.complete
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - ops.job.dispatch:
    - main
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
    - ops.job
  jobs:
    main:
      mode: build
      helper: helper.docs.generate_all
      inputs:
        action: build
    on_fail:
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/SRRUST-JOB-007.fail.json
        format: json
        report_name: SRRUST-JOB-007.fail
    on_complete:
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/SRRUST-JOB-007.complete.json
        format: json
        report_name: SRRUST-JOB-007.complete
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - ops.job.dispatch:
    - main
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
    - ops.job
  jobs:
    main:
      mode: check
      helper: helper.docs.generate_all
      inputs:
        action: check
    on_fail:
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/SRRUST-JOB-008.fail.json
        format: json
        report_name: SRRUST-JOB-008.fail
    on_complete:
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/SRRUST-JOB-008.complete.json
        format: json
        report_name: SRRUST-JOB-008.complete
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - ops.job.dispatch:
    - main
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
    - ops.job
  jobs:
    main:
      mode: build
      helper: helper.docs.generate_all
      inputs:
        action: build
        surface: reference_book
    on_fail:
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/SRRUST-JOB-009.fail.json
        format: json
        report_name: SRRUST-JOB-009.fail
    on_complete:
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/SRRUST-JOB-009.complete.json
        format: json
        report_name: SRRUST-JOB-009.complete
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - ops.job.dispatch:
    - main
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
    - ops.job
  jobs:
    main:
      mode: check
      helper: helper.docs.generate_all
      inputs:
        action: check
        surface: reference_book
    on_fail:
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/SRRUST-JOB-010.fail.json
        format: json
        report_name: SRRUST-JOB-010.fail
    on_complete:
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/SRRUST-JOB-010.complete.json
        format: json
        report_name: SRRUST-JOB-010.complete
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - ops.job.dispatch:
    - main
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
    - ops.job
  jobs:
    main:
      mode: build
      helper: helper.docs.generate_all
      inputs:
        action: build
        surface: docs_graph
    on_fail:
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/SRRUST-JOB-011.fail.json
        format: json
        report_name: SRRUST-JOB-011.fail
    on_complete:
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/SRRUST-JOB-011.complete.json
        format: json
        report_name: SRRUST-JOB-011.complete
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - ops.job.dispatch:
    - main
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - ok
    - true
```
