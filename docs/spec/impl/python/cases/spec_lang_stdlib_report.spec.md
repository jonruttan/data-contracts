# Python Spec-Lang Stdlib Report Command Cases

## SRPY-STDLIB-REP-001

```yaml contract-spec
id: SRPY-STDLIB-REP-001
title: spec_lang_stdlib_report_main emits json by default
type: contract.check
harness:
  entrypoint: spec_runner.spec_lang_commands:spec_lang_stdlib_report_main
  check:
    profile: cli.run
    config:
      argv: []
      exit_code: 0
contract:
- id: assert_1
  class: MUST
  target: stdout
  asserts:
  - evaluate:
    - lit:
        std.string.contains:
        - {var: subject}
        - '"version": 1'
  - evaluate:
    - lit:
        std.string.contains:
        - {var: subject}
        - '"summary"'
```

## SRPY-STDLIB-REP-002

```yaml contract-spec
id: SRPY-STDLIB-REP-002
title: spec_lang_stdlib_report_main emits markdown with format md
type: contract.check
harness:
  entrypoint: spec_runner.spec_lang_commands:spec_lang_stdlib_report_main
  check:
    profile: cli.run
    config:
      argv:
      - --format
      - md
      exit_code: 0
contract:
- id: assert_1
  class: MUST
  target: stdout
  asserts:
  - evaluate:
    - lit:
        std.string.contains:
        - {var: subject}
        - '# Spec-Lang Stdlib Profile Report'
  - evaluate:
    - lit:
        std.string.contains:
        - {var: subject}
        - '- profile symbols:'
```
