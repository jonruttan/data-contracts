# PHP Spec Runner Portability Cases

## SRPHP-PORT-001

```yaml spec-test
id: SRPHP-PORT-001
title: shell command via sh -c works when shell exists
purpose: Captures a shell-based cli.run case to detect environments where sh is unavailable.
type: cli.run
argv:
- echo port-shell-ok
exit_code: 0
harness:
  entrypoint: /bin/sh -c
expect:
  portable:
    status: pass
    category: null
assert:
- target: stdout
  must:
  - evaluate:
    - std.string.contains:
      - {var: subject}
      - port-shell-ok
```

## SRPHP-PORT-002

```yaml spec-test
id: SRPHP-PORT-002
title: process env passthrough remains stringly typed
purpose: Verifies env values passed through cli.run are observed as strings by child processes.
type: cli.run
argv:
- echo x:$X_PORT_BOOL y:$X_PORT_NUM
exit_code: 0
harness:
  entrypoint: /bin/sh -c
  env:
    X_PORT_BOOL: 'true'
    X_PORT_NUM: '7'
expect:
  portable:
    status: pass
    category: null
assert:
- target: stdout
  must:
  - evaluate:
    - std.string.contains:
      - {var: subject}
      - x:true y:7
```

## SRPHP-PORT-003

```yaml spec-test
id: SRPHP-PORT-003
title: relative stdout path resolves from runner cwd
purpose: Detects portability differences in cwd/path handling for stdout_path assertions.
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
  - evaluate:
    - std.string.contains:
      - {var: subject}
      - path_target.txt
```
