# Python Spec-Lang Stdlib Report Command Cases

## SRPY-STDLIB-REP-001

```yaml spec-test
id: SRPY-STDLIB-REP-001
title: spec_lang_stdlib_report_main emits json by default
type: cli.run
argv: []
exit_code: 0
harness:
  entrypoint: spec_runner.cli:spec_lang_stdlib_report_main
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
```

## SRPY-STDLIB-REP-002

```yaml spec-test
id: SRPY-STDLIB-REP-002
title: spec_lang_stdlib_report_main emits markdown with format md
type: cli.run
argv:
- --format
- md
exit_code: 0
harness:
  entrypoint: spec_runner.cli:spec_lang_stdlib_report_main
assert:
- id: assert_1
  class: must
  target: stdout
  checks:
  - std.string.contains:
    - var: subject
    - '# Spec-Lang Stdlib Profile Report'
  - std.string.contains:
    - var: subject
    - '- profile symbols:'
```
