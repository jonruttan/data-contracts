# Rust Report Job Cases

## SRRUST-JOB-REP-001

```yaml contract-spec
id: SRRUST-JOB-REP-001
title: conformance purpose json report
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-REP-001'
    mode: report
    helper: helper.report.emit
    inputs:
      report_name: conformance-purpose
      format: json
      out: .artifacts/conformance-purpose.json
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - std.string.contains:
    - std.object.get:
      - var: subject
      - written_path
    - .artifacts/conformance-purpose.json
```

## SRRUST-JOB-REP-002

```yaml contract-spec
id: SRRUST-JOB-REP-002
title: conformance purpose markdown report
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-REP-002'
    mode: report
    helper: helper.report.emit
    inputs:
      report_name: conformance-purpose
      format: md
      out: .artifacts/conformance-purpose-summary.md
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - std.string.contains:
    - std.object.get:
      - var: subject
      - written_path
    - .artifacts/conformance-purpose-summary.md
```

## SRRUST-JOB-REP-003

```yaml contract-spec
id: SRRUST-JOB-REP-003
title: spec portability json report
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-REP-003'
    mode: report
    helper: helper.report.emit
    inputs:
      report_name: spec-portability
      format: json
      out: .artifacts/spec-portability.json
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - std.string.contains:
    - std.object.get:
      - var: subject
      - written_path
    - .artifacts/spec-portability.json
```

## SRRUST-JOB-REP-004

```yaml contract-spec
id: SRRUST-JOB-REP-004
title: spec portability markdown report
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-REP-004'
    mode: report
    helper: helper.report.emit
    inputs:
      report_name: spec-portability
      format: md
      out: .artifacts/spec-portability-summary.md
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - std.string.contains:
    - std.object.get:
      - var: subject
      - written_path
    - .artifacts/spec-portability-summary.md
```

## SRRUST-JOB-REP-005

```yaml contract-spec
id: SRRUST-JOB-REP-005
title: contract assertions json report
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-REP-005'
    mode: report
    helper: helper.report.emit
    inputs:
      report_name: contract-assertions
      format: json
      out: .artifacts/contract-assertions.json
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - std.string.contains:
    - std.object.get:
      - var: subject
      - written_path
    - .artifacts/contract-assertions.json
```

## SRRUST-JOB-REP-006

```yaml contract-spec
id: SRRUST-JOB-REP-006
title: contract assertions markdown report
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-REP-006'
    mode: report
    helper: helper.report.emit
    inputs:
      report_name: contract-assertions
      format: md
      out: .artifacts/contract-assertions-summary.md
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - std.string.contains:
    - std.object.get:
      - var: subject
    - written_path
    - .artifacts/contract-assertions-summary.md
```

## SRRUST-JOB-REP-007

```yaml contract-spec
id: SRRUST-JOB-REP-007
title: spec lang adoption json report
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-REP-007'
    mode: report
    helper: helper.report.emit
    inputs:
      report_name: spec-lang-adoption
      format: json
      out: .artifacts/spec-lang-adoption.json
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - std.string.contains:
    - std.object.get:
      - var: subject
      - written_path
    - .artifacts/spec-lang-adoption.json
```

## SRRUST-JOB-REP-008

```yaml contract-spec
id: SRRUST-JOB-REP-008
title: spec lang adoption markdown report
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-REP-008'
    mode: report
    helper: helper.report.emit
    inputs:
      report_name: spec-lang-adoption
      format: md
      out: .artifacts/spec-lang-adoption-summary.md
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - std.string.contains:
    - std.object.get:
      - var: subject
      - written_path
    - .artifacts/spec-lang-adoption-summary.md
```

## SRRUST-JOB-REP-009

```yaml contract-spec
id: SRRUST-JOB-REP-009
title: runner independence json report
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-REP-009'
    mode: report
    helper: helper.report.emit
    inputs:
      report_name: runner-independence
      format: json
      out: .artifacts/runner-independence.json
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - std.string.contains:
    - std.object.get:
      - var: subject
      - written_path
    - .artifacts/runner-independence.json
```

## SRRUST-JOB-REP-010

```yaml contract-spec
id: SRRUST-JOB-REP-010
title: runner independence markdown report
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-REP-010'
    mode: report
    helper: helper.report.emit
    inputs:
      report_name: runner-independence
      format: md
      out: .artifacts/runner-independence-summary.md
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - std.string.contains:
    - std.object.get:
      - var: subject
      - written_path
    - .artifacts/runner-independence-summary.md
```

## SRRUST-JOB-REP-011

```yaml contract-spec
id: SRRUST-JOB-REP-011
title: python dependency json report
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-REP-011'
    mode: report
    helper: helper.report.emit
    inputs:
      report_name: python-dependency
      format: json
      out: .artifacts/python-dependency.json
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - std.string.contains:
    - std.object.get:
      - var: subject
      - written_path
    - .artifacts/python-dependency.json
```

## SRRUST-JOB-REP-012

```yaml contract-spec
id: SRRUST-JOB-REP-012
title: python dependency markdown report
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-REP-012'
    mode: report
    helper: helper.report.emit
    inputs:
      report_name: python-dependency
      format: md
      out: .artifacts/python-dependency-summary.md
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - std.string.contains:
    - std.object.get:
      - var: subject
      - written_path
    - .artifacts/python-dependency-summary.md
```

## SRRUST-JOB-REP-013

```yaml contract-spec
id: SRRUST-JOB-REP-013
title: docs operability json report
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-REP-013'
    mode: report
    helper: helper.report.emit
    inputs:
      report_name: docs-operability
      format: json
      out: .artifacts/docs-operability.json
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - std.string.contains:
    - std.object.get:
      - var: subject
      - written_path
    - .artifacts/docs-operability.json
```

## SRRUST-JOB-REP-014

```yaml contract-spec
id: SRRUST-JOB-REP-014
title: docs operability markdown report
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-REP-014'
    mode: report
    helper: helper.report.emit
    inputs:
      report_name: docs-operability
      format: md
      out: .artifacts/docs-operability-summary.md
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - std.string.contains:
    - std.object.get:
      - var: subject
      - written_path
    - .artifacts/docs-operability-summary.md
```

## SRRUST-JOB-REP-015

```yaml contract-spec
id: SRRUST-JOB-REP-015
title: objective scorecard json report
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-REP-015'
    mode: report
    helper: helper.report.emit
    inputs:
      report_name: objective-scorecard
      format: json
      out: .artifacts/objective-scorecard.json
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - std.string.contains:
    - std.object.get:
      - var: subject
      - written_path
    - .artifacts/objective-scorecard.json
```

## SRRUST-JOB-REP-016

```yaml contract-spec
id: SRRUST-JOB-REP-016
title: objective scorecard markdown report
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-REP-016'
    mode: report
    helper: helper.report.emit
    inputs:
      report_name: objective-scorecard
      format: md
      out: .artifacts/objective-scorecard-summary.md
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - std.string.contains:
    - std.object.get:
      - var: subject
      - written_path
    - .artifacts/objective-scorecard-summary.md
```

## SRRUST-JOB-REP-017

```yaml contract-spec
id: SRRUST-JOB-REP-017
title: spec lang stdlib json report
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-REP-017'
    mode: report
    helper: helper.report.emit
    inputs:
      report_name: spec-lang-stdlib
      format: json
      out: .artifacts/spec-lang-stdlib.json
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - std.string.contains:
    - std.object.get:
      - var: subject
      - written_path
    - .artifacts/spec-lang-stdlib.json
```

## SRRUST-JOB-REP-018

```yaml contract-spec
id: SRRUST-JOB-REP-018
title: spec lang stdlib markdown report
type: contract.job
harness:
  spec_lang:
    capabilities:
    - ops.helper
  job:
    ref: '#SRRUST-JOB-REP-018'
    mode: report
    helper: helper.report.emit
    inputs:
      report_name: spec-lang-stdlib
      format: md
      out: .artifacts/spec-lang-stdlib-summary.md
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - std.string.contains:
    - std.object.get:
      - var: subject
      - written_path
    - .artifacts/spec-lang-stdlib-summary.md
```
