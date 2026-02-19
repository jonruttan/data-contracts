# Python Contract Coverage Report Command Cases

## SRPY-CONTRACT-REP-001

```yaml contract-spec
id: SRPY-CONTRACT-REP-001
title: contract_coverage_report_main emits json payload to stdout
type: contract.check
harness:
  entrypoint: spec_runner.spec_lang_commands:contract_coverage_report_main
  check:
    profile: cli.run
    config:
      argv: []
      exit_code: 0
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    target: stdout
    assert:
    - std.string.contains:
      - {var: subject}
      - '"version": 1'
    - std.string.contains:
      - {var: subject}
      - '"summary"'
    - std.string.contains:
      - {var: subject}
      - '"rules"'
```

## SRPY-CONTRACT-REP-002

```yaml contract-spec
id: SRPY-CONTRACT-REP-002
title: contract_coverage_report_main writes output file with --out
type: contract.check
harness:
  entrypoint: spec_runner.spec_lang_commands:contract_coverage_report_main
  check:
    profile: cli.run
    config:
      argv:
      - --out
      - .artifacts/contract-coverage-impl-case.json
      exit_code: 0
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    target: stdout
    assert:
      std.string.contains:
      - {var: subject}
      - wrote .artifacts/contract-coverage-impl-case.json
```
