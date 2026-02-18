# Python Spec-Lang Stdlib Report Command Cases

## SRPY-STDLIB-REP-001

```yaml contract-spec
id: SRPY-STDLIB-REP-001
title: spec_lang_stdlib_report_main emits json by default
type: cli.run
argv: []
exit_code: 0
harness:
  entrypoint: spec_runner.spec_lang_commands:spec_lang_stdlib_report_main
contract:
- id: assert_1
  class: MUST
  target: stdout
  asserts:
  - std.string.contains:
    - var: subject
    - '"version": 1'
  - std.string.contains:
    - var: subject
    - '"summary"'
```

## SRPY-STDLIB-REP-002

```yaml contract-spec
id: SRPY-STDLIB-REP-002
title: spec_lang_stdlib_report_main emits markdown with format md
type: cli.run
argv:
- --format
- md
exit_code: 0
harness:
  entrypoint: spec_runner.spec_lang_commands:spec_lang_stdlib_report_main
contract:
- id: assert_1
  class: MUST
  target: stdout
  asserts:
  - std.string.contains:
    - var: subject
    - '# Spec-Lang Stdlib Profile Report'
  - std.string.contains:
    - var: subject
    - '- profile symbols:'
```
