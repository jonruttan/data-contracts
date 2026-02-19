# PHP Spec Runner Portability Cases

## DCIMPL-PHP-PORT-001

```yaml contract-spec
id: DCIMPL-PHP-PORT-001
title: shell command via sh -c works when shell exists
purpose: Captures a shell-based cli.run case to detect environments where sh is unavailable.
type: contract.check
harness:
  entrypoint: /bin/sh -c
  check:
    profile: cli.run
    config:
      argv:
      - echo port-shell-ok
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
  steps:
  - id: assert_1
    assert:
      std.string.contains:
      - {var: stdout}
      - port-shell-ok
```

## DCIMPL-PHP-PORT-002

```yaml contract-spec
id: DCIMPL-PHP-PORT-002
title: process env passthrough remains stringly typed
purpose: Verifies env values passed through cli.run are observed as strings by child processes.
type: contract.check
harness:
  entrypoint: /bin/sh -c
  env:
    X_PORT_BOOL: 'true'
    X_PORT_NUM: '7'
  check:
    profile: cli.run
    config:
      argv:
      - echo x:$X_PORT_BOOL y:$X_PORT_NUM
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
  steps:
  - id: assert_1
    assert:
      std.string.contains:
      - {var: stdout}
      - x:true y:7
```

## DCIMPL-PHP-PORT-003

```yaml contract-spec
id: DCIMPL-PHP-PORT-003
title: relative stdout path resolves from runner cwd
purpose: Detects portability differences in cwd/path handling for stdout_path assertions.
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
  steps:
  - id: assert_1
    assert:
      std.string.contains:
      - {var: stdout_path}
      - path_target.txt
```
