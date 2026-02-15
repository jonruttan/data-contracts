# PHP Spec Runner Pass Cases

## SRPHP-RUN-001

```yaml spec-test
id: SRPHP-RUN-001
title: text.file default target uses containing spec file
purpose: Verifies text.file reads the containing spec document when path is omitted.
type: text.file
expect:
  portable:
    status: pass
    category: null
assert:
- target: text
  must:
  - contain:
    - '# PHP Spec Runner Pass Cases'
```

## SRPHP-RUN-002

```yaml spec-test
id: SRPHP-RUN-002
title: text.file supports relative path
purpose: Verifies text.file can read a relative path under the same repository root.
type: text.file
path: /fixtures/sample.txt
expect:
  portable:
    status: pass
    category: null
assert:
- target: text
  must:
  - contain:
    - fixture-content
```

## SRPHP-RUN-003

```yaml spec-test
id: SRPHP-RUN-003
title: text.file can group succeeds with one passing branch
purpose: Ensures can group semantics pass when at least one branch evaluates true.
type: text.file
path: /fixtures/sample.txt
expect:
  portable:
    status: pass
    category: null
assert:
- target: text
  can:
  - contain:
    - no-match-token
  - contain:
    - fixture-content
```

## SRPHP-RUN-004

```yaml spec-test
id: SRPHP-RUN-004
title: cli.run explicit entrypoint executes argv
purpose: Verifies cli.run executes explicit harness entrypoint with argv arguments.
type: cli.run
argv:
- hello-runner
exit_code: 0
harness:
  entrypoint: /bin/echo
expect:
  portable:
    status: pass
    category: null
assert:
- target: stdout
  must:
  - contain:
    - hello-runner
```

## SRPHP-RUN-005

```yaml spec-test
id: SRPHP-RUN-005
title: cli.run applies harness env mapping
purpose: Verifies cli.run applies harness env values to the subprocess environment.
type: cli.run
argv:
- echo $X_PHP_SPEC
exit_code: 0
harness:
  entrypoint: /bin/sh -c
  env:
    X_PHP_SPEC: 'on'
expect:
  portable:
    status: pass
    category: null
assert:
- target: stdout
  must:
  - contain:
    - 'on'
```

## SRPHP-RUN-006

```yaml spec-test
id: SRPHP-RUN-006
title: cli.run requires explicit harness entrypoint
purpose: Verifies cli.run executes when harness entrypoint is explicitly provided.
type: cli.run
argv:
- fallback-ok
exit_code: 0
harness:
  entrypoint: /bin/echo
expect:
  portable:
    status: pass
    category: null
assert:
- target: stdout
  must:
  - contain:
    - fallback-ok
```

## SRPHP-RUN-007

```yaml spec-test
id: SRPHP-RUN-007
title: cli.run json_type list assertion passes
purpose: Verifies json_type list assertions are supported for stdout target in cli.run.
type: cli.run
argv:
- '[]'
exit_code: 0
harness:
  entrypoint: /bin/echo
expect:
  portable:
    status: pass
    category: null
assert:
- target: stdout
  must:
  - json_type:
    - list
```

## SRPHP-RUN-008

```yaml spec-test
id: SRPHP-RUN-008
title: cli.run can assert stderr output
purpose: Verifies stderr target assertions using a command that writes to stderr.
type: cli.run
argv:
- echo runner-err 1>&2
exit_code: 0
harness:
  entrypoint: /bin/sh -c
expect:
  portable:
    status: pass
    category: null
assert:
- target: stderr
  must:
  - contain:
    - runner-err
```

## SRPHP-RUN-009

```yaml spec-test
id: SRPHP-RUN-009
title: cli.run supports stdout_path and stdout_path_text targets
purpose: Verifies path-based assertions for stdout_path existence and stdout_path_text content.
type: cli.run
argv:
- docs/spec/impl/php/cases/fixtures/path_target.txt
exit_code: 0
harness:
  entrypoint: /bin/echo
expect:
  portable:
    status: pass
    category: null
assert:
- target: stdout_path
  must:
  - exists:
    - true
  - contain:
    - path_target.txt
  - evaluate:
    - contains:
      - {var: subject}
      - path_target.txt
- target: stdout_path_text
  must:
  - contain:
    - path target file content
  - evaluate:
    - contains:
      - {var: subject}
      - path target file content
```
