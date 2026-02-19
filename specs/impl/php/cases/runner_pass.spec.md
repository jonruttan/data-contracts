# PHP Spec Runner Pass Cases

## SRPHP-RUN-001

```yaml contract-spec
id: SRPHP-RUN-001
title: text.file default target uses containing spec file
purpose: Verifies text.file reads the containing spec document when path is omitted.
type: contract.check
expect:
  portable:
    status: pass
    category: null
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - text
    as:
      text: subject
  steps:
  - id: assert_1
    assert:
      std.string.contains:
      - {var: subject}
      - '# PHP Spec Runner Pass Cases'
harness:
  check:
    profile: text.file
    config: {}
```

## SRPHP-RUN-002

```yaml contract-spec
id: SRPHP-RUN-002
title: text.file supports relative path
purpose: Verifies text.file can read a relative path under the same repository root.
type: contract.check
expect:
  portable:
    status: pass
    category: null
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - text
    as:
      text: subject
  steps:
  - id: assert_1
    assert:
      std.string.contains:
      - {var: subject}
      - fixture-content
harness:
  check:
    profile: text.file
    config:
      path: /fixtures/sample.txt
```

## SRPHP-RUN-003

```yaml contract-spec
id: SRPHP-RUN-003
title: text.file can group succeeds with one passing branch
purpose: Ensures can group semantics pass when at least one branch evaluates true.
type: contract.check
expect:
  portable:
    status: pass
    category: null
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - text
    as:
      text: subject
  steps:
  - id: assert_1
    class: MAY
    assert:
    - std.string.contains:
      - {var: subject}
      - no-match-token
    - std.string.contains:
      - {var: subject}
      - fixture-content
harness:
  check:
    profile: text.file
    config:
      path: /fixtures/sample.txt
```

## SRPHP-RUN-004

```yaml contract-spec
id: SRPHP-RUN-004
title: cli.run explicit entrypoint executes argv
purpose: Verifies cli.run executes explicit harness entrypoint with argv arguments.
type: contract.check
harness:
  entrypoint: /bin/echo
  check:
    profile: cli.run
    config:
      argv:
      - hello-runner
      exit_code: 0
expect:
  portable:
    status: pass
    category: null
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - stdout
    as:
      stdout: subject
  steps:
  - id: assert_1
    assert:
      std.string.contains:
      - {var: subject}
      - hello-runner
```

## SRPHP-RUN-005

```yaml contract-spec
id: SRPHP-RUN-005
title: cli.run applies harness env mapping
purpose: Verifies cli.run applies harness env values to the subprocess environment.
type: contract.check
harness:
  entrypoint: /bin/sh -c
  env:
    X_PHP_SPEC: 'on'
  check:
    profile: cli.run
    config:
      argv:
      - echo $X_PHP_SPEC
      exit_code: 0
expect:
  portable:
    status: pass
    category: null
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - stdout
    as:
      stdout: subject
  steps:
  - id: assert_1
    assert:
      std.string.contains:
      - {var: subject}
      - 'on'
```

## SRPHP-RUN-006

```yaml contract-spec
id: SRPHP-RUN-006
title: cli.run requires explicit harness entrypoint
purpose: Verifies cli.run executes when harness entrypoint is explicitly provided.
type: contract.check
harness:
  entrypoint: /bin/echo
  check:
    profile: cli.run
    config:
      argv:
      - fallback-ok
      exit_code: 0
expect:
  portable:
    status: pass
    category: null
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - stdout
    as:
      stdout: subject
  steps:
  - id: assert_1
    assert:
      std.string.contains:
      - {var: subject}
      - fallback-ok
```

## SRPHP-RUN-007

```yaml contract-spec
id: SRPHP-RUN-007
title: cli.run json_type list assertion passes
purpose: Verifies json parsing and type checks can be expressed via std.* mapping-AST.
type: contract.check
harness:
  entrypoint: /bin/echo
  check:
    profile: cli.run
    config:
      argv:
      - '[]'
      exit_code: 0
expect:
  portable:
    status: pass
    category: null
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - stdout
    as:
      stdout: subject
  steps:
  - id: assert_1
    assert:
      std.type.json_type:
      - std.json.parse:
        - {var: subject}
      - list
```

## SRPHP-RUN-008

```yaml contract-spec
id: SRPHP-RUN-008
title: cli.run can assert stderr output
purpose: Verifies stderr target assertions using a command that writes to stderr.
type: contract.check
harness:
  entrypoint: /bin/sh -c
  check:
    profile: cli.run
    config:
      argv:
      - echo runner-err 1>&2
      exit_code: 0
expect:
  portable:
    status: pass
    category: null
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - stderr
    as:
      stderr: subject
  steps:
  - id: assert_1
    assert:
      std.string.contains:
      - {var: subject}
      - runner-err
```

## SRPHP-RUN-009

```yaml contract-spec
id: SRPHP-RUN-009
title: cli.run supports stdout_path and stdout_path_text targets
purpose: Verifies path-based assertions for stdout_path existence and stdout_path_text content.
type: contract.check
harness:
  entrypoint: /bin/echo
  check:
    profile: cli.run
    config:
      argv:
      - specs/impl/php/cases/fixtures/path_target.txt
      exit_code: 0
expect:
  portable:
    status: pass
    category: null
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - stdout_path
    as:
      stdout_path: subject
  steps:
  - id: assert_1
    assert:
      std.string.contains:
      - {var: subject}
      - path_target.txt
  - id: assert_2
    assert:
      std.string.contains:
      - {var: subject}
      - path target file content
    imports:
    - from: artifact
      names:
      - stdout_path_text
      as:
        stdout_path_text: subject
```
