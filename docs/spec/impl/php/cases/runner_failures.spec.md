# PHP Spec Runner Expected Failure Cases

## SRPHP-RUN-F001

```yaml contract-spec
id: SRPHP-RUN-F001
title: text.file virtual absolute path missing file fails runtime
purpose: Verifies virtual-root absolute paths resolve under contract root and fail at runtime
  when the file is missing.
type: contract.check
expect:
  portable:
    status: fail
    category: runtime
    message_tokens:
    - cannot read fixture file
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          std.string.contains:
          - {var: subject}
          - x
  target: text
harness:
  check:
    profile: text.file
    config:
      path: /tmp/not-allowed.txt
```

## SRPHP-RUN-F002

```yaml contract-spec
id: SRPHP-RUN-F002
title: text.file path escape is rejected
purpose: Verifies text.file rejects relative paths that escape the contract root boundary.
type: contract.check
expect:
  portable:
    status: fail
    category: schema
    message_tokens:
    - text.file path escapes contract root
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          std.string.contains:
          - {var: subject}
          - outside
  target: text
harness:
  check:
    profile: text.file
    config:
      path: ../../../../../../outside.txt
```

## SRPHP-RUN-F003

```yaml contract-spec
id: SRPHP-RUN-F003
title: cli.run without entrypoint fails
purpose: Verifies cli.run reports runtime failure when no entrypoint source is available.
type: contract.check
harness:
  check:
    profile: cli.run
    config:
      argv:
      - x
      exit_code: 0
expect:
  portable:
    status: fail
    category: runtime
    message_tokens:
    - requires explicit harness.entrypoint
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          std.string.contains:
          - {var: subject}
          - x
  target: stdout
```

## SRPHP-RUN-F004

```yaml contract-spec
id: SRPHP-RUN-F004
title: cli.run rejects unknown spec-lang symbol usage
purpose: Verifies unknown expression symbols are rejected as schema failures.
type: contract.check
harness:
  entrypoint: /bin/echo
  check:
    profile: cli.run
    config:
      argv:
      - '{}'
      exit_code: 0
expect:
  portable:
    status: fail
    category: schema
    message_tokens:
    - unsupported spec_lang symbol
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          not.a.real.symbol:
          - {var: subject}
  target: stdout
```

## SRPHP-RUN-F005

```yaml contract-spec
id: SRPHP-RUN-F005
title: cli.run exit_code mismatch is assertion failure
purpose: Verifies cli.run reports assertion failure when observed exit code differs
  from expected.
type: contract.check
harness:
  entrypoint: /bin/sh -c
  check:
    profile: cli.run
    config:
      argv:
      - exit 2
      exit_code: 0
expect:
  portable:
    status: fail
    category: assertion
    message_tokens:
    - exit_code expected=0 actual=2
contract: []
```

## SRPHP-RUN-F006

```yaml contract-spec
id: SRPHP-RUN-F006
title: unknown type reports runtime failure
purpose: Verifies unknown contract-spec types are reported as runtime failures.
type: nope.type
expect:
  portable:
    status: fail
    category: runtime
    message_tokens:
    - unknown contract-spec type
contract: []
```

## SRPHP-RUN-F007

```yaml contract-spec
id: SRPHP-RUN-F007
title: cli.run rejects unsupported harness keys
purpose: Verifies cli.run validates supported harness keys and rejects unknown ones.
type: contract.check
harness:
  entrypoint: /bin/echo
  stdin_text: nope
  check:
    profile: cli.run
    config:
      argv:
      - x
      exit_code: 0
expect:
  portable:
    status: fail
    category: schema
    message_tokens:
    - unsupported harness key(s)
contract: []
```

## SRPHP-RUN-F008

```yaml contract-spec
id: SRPHP-RUN-F008
title: leaf target key is rejected
purpose: Verifies leaf assertions including target key are rejected as schema violations.
type: contract.check
expect:
  portable:
    status: fail
    category: schema
    message_tokens:
    - 'leaf assertion must not include key: target'
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          target: text
          contain:
          - fixture-content
  target: text
harness:
  check:
    profile: text.file
    config:
      path: /fixtures/sample.txt
```
