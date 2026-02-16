# CLI Entry Point Conformance Cases

These fixtures pin down entrypoint resolution behavior for `type: cli.run`.

Coverage focus:

- explicit `harness.entrypoint` behavior
- capability-gated skip behavior for runtimes without `cli.run`

## SRCONF-CLI-001

```yaml spec-test
id: SRCONF-CLI-001
title: conformance fixture sets explicit cli.run harness.entrypoint
purpose: Defines portable behavior for explicit cli.run entrypoint when capability
  is present.
type: cli.run
requires:
  capabilities:
  - cli.run
  - cli.run.entrypoint_conformance
  when_missing: skip
expect:
  portable:
    status: skip
    category: null
  impl:
    php:
      status: skip
      category: null
argv:
- --help
exit_code: 0
harness:
  entrypoint: spec_runner.conformance_fixtures:main
assert: []
```

## SRCONF-CLI-002

```yaml spec-test
id: SRCONF-CLI-002
title: explicit entrypoint drives cli.run behavior deterministically
purpose: Pins deterministic behavior for explicit harness entrypoint execution.
type: cli.run
requires:
  capabilities:
  - cli.run
  - cli.run.entrypoint_conformance
  when_missing: skip
expect:
  portable:
    status: skip
    category: null
  impl:
    php:
      status: skip
      category: null
argv:
- --json
exit_code: 0
harness:
  entrypoint: spec_runner.conformance_fixtures:main
assert:
- id: assert_1
  class: must
  checks:
  - std.string.contains:
    - var: subject
    - '"ok": true'
  target: stdout
```
