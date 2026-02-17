# Python Contract Coverage Report Command Cases

## SRPY-CONTRACT-REP-001

```yaml spec-test
id: SRPY-CONTRACT-REP-001
title: contract_coverage_report_main emits json payload to stdout
type: cli.run
argv: []
exit_code: 0
harness:
  entrypoint: spec_runner.cli:contract_coverage_report_main
assert:
- id: assert_1
  class: must
  target: stdout
  checks:
  - std.string.contains:
    - var: subject
    - '"version": 1'
  - std.string.contains:
    - var: subject
    - '"summary"'
  - std.string.contains:
    - var: subject
    - '"rules"'
```

## SRPY-CONTRACT-REP-002

```yaml spec-test
id: SRPY-CONTRACT-REP-002
title: contract_coverage_report_main writes output file with --out
type: cli.run
argv:
- --out
- .artifacts/contract-coverage-impl-case.json
exit_code: 0
harness:
  entrypoint: spec_runner.cli:contract_coverage_report_main
assert:
- id: assert_1
  class: must
  target: stdout
  checks:
  - std.string.contains:
    - var: subject
    - 'wrote .artifacts/contract-coverage-impl-case.json'
```
