# Python Validate Conformance Report Command Cases

## SRPY-VALREP-001

```yaml contract-spec
id: SRPY-VALREP-001
title: validate_report_main passes for valid report payload
type: contract.check
harness:
  entrypoint: spec_runner.spec_lang_commands:validate_report_main
  check:
    profile: cli.run
    config:
      argv:
      - specs/impl/python/fixtures/conformance_report_valid.json
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
      - 'OK: valid conformance report'
```

## SRPY-VALREP-002

```yaml contract-spec
id: SRPY-VALREP-002
title: validate_report_main fails for invalid report payload
type: contract.check
harness:
  entrypoint: spec_runner.spec_lang_commands:validate_report_main
  check:
    profile: cli.run
    config:
      argv:
      - specs/impl/python/fixtures/conformance_report_invalid.json
      exit_code: 1
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    target: stderr
    assert:
      std.string.contains:
      - {var: subject}
      - 'ERROR: report.version must equal 1'
```
