# PHP Spec Runner Expected Failure Cases

## SRPHP-RUN-F001

```yaml spec-test
id: SRPHP-RUN-F001
title: text.file virtual absolute path missing file fails runtime
purpose: Verifies virtual-root absolute paths resolve under contract root and fail at runtime
  when the file is missing.
type: text.file
path: /tmp/not-allowed.txt
expect:
  portable:
    status: fail
    category: runtime
    message_tokens:
    - cannot read fixture file
assert:
- target: text
  must:
  - evaluate:
    - contains:
      - {var: subject}
      - x
```

## SRPHP-RUN-F002

```yaml spec-test
id: SRPHP-RUN-F002
title: text.file path escape is rejected
purpose: Verifies text.file rejects relative paths that escape the contract root boundary.
type: text.file
path: ../../../../../../outside.txt
expect:
  portable:
    status: fail
    category: schema
    message_tokens:
    - text.file path escapes contract root
assert:
- target: text
  must:
  - evaluate:
    - contains:
      - {var: subject}
      - outside
```

## SRPHP-RUN-F003

```yaml spec-test
id: SRPHP-RUN-F003
title: cli.run without entrypoint fails
purpose: Verifies cli.run reports runtime failure when no entrypoint source is available.
type: cli.run
argv:
- x
exit_code: 0
harness: {}
expect:
  portable:
    status: fail
    category: runtime
    message_tokens:
    - requires explicit harness.entrypoint
assert:
- target: stdout
  must:
  - evaluate:
    - contains:
      - {var: subject}
      - x
```

## SRPHP-RUN-F004

```yaml spec-test
id: SRPHP-RUN-F004
title: cli.run rejects unsupported json_type values
purpose: Verifies cli.run treats unsupported json_type values as schema violations.
type: cli.run
argv:
- '{}'
exit_code: 0
harness:
  entrypoint: /bin/echo
expect:
  portable:
    status: fail
    category: schema
    message_tokens:
    - unsupported json_type
assert:
- target: stdout
  must:
  - json_type:
    - nope
```

## SRPHP-RUN-F005

```yaml spec-test
id: SRPHP-RUN-F005
title: cli.run exit_code mismatch is assertion failure
purpose: Verifies cli.run reports assertion failure when observed exit code differs from expected.
type: cli.run
argv:
- exit 2
exit_code: 0
harness:
  entrypoint: /bin/sh -c
expect:
  portable:
    status: fail
    category: assertion
    message_tokens:
    - exit_code expected=0 actual=2
assert: []
```

## SRPHP-RUN-F006

```yaml spec-test
id: SRPHP-RUN-F006
title: unknown type reports runtime failure
purpose: Verifies unknown spec-test types are reported as runtime failures.
type: nope.type
expect:
  portable:
    status: fail
    category: runtime
    message_tokens:
    - unknown spec-test type
assert: []
```

## SRPHP-RUN-F007

```yaml spec-test
id: SRPHP-RUN-F007
title: cli.run rejects unsupported harness keys
purpose: Verifies cli.run validates supported harness keys and rejects unknown ones.
type: cli.run
argv:
- x
exit_code: 0
harness:
  entrypoint: /bin/echo
  stdin_text: nope
expect:
  portable:
    status: fail
    category: schema
    message_tokens:
    - unsupported harness key(s)
assert: []
```

## SRPHP-RUN-F008

```yaml spec-test
id: SRPHP-RUN-F008
title: leaf target key is rejected
purpose: Verifies leaf assertions including target key are rejected as schema violations.
type: text.file
path: /fixtures/sample.txt
expect:
  portable:
    status: fail
    category: schema
    message_tokens:
    - 'leaf assertion must not include key: target'
assert:
- target: text
  must:
  - target: text
    contain:
    - fixture-content
```
