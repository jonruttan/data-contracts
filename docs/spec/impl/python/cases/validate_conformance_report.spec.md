# Python Validate Conformance Report Command Cases

## SRPY-VALREP-001

```yaml spec-test
id: SRPY-VALREP-001
title: validate_report_main passes for valid report payload
type: cli.run
argv:
- docs/spec/impl/python/fixtures/conformance_report_valid.json
exit_code: 0
harness:
  entrypoint: spec_runner.cli:validate_report_main
assert:
- id: assert_1
  class: must
  target: stdout
  checks:
  - std.string.contains:
    - var: subject
    - 'OK: valid conformance report'
```

## SRPY-VALREP-002

```yaml spec-test
id: SRPY-VALREP-002
title: validate_report_main fails for invalid report payload
type: cli.run
argv:
- docs/spec/impl/python/fixtures/conformance_report_invalid.json
exit_code: 1
harness:
  entrypoint: spec_runner.cli:validate_report_main
assert:
- id: assert_1
  class: must
  target: stderr
  checks:
  - std.string.contains:
    - var: subject
    - 'ERROR: report.version must equal 1'
```
