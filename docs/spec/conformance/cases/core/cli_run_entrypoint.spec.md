# CLI Entry Point Conformance Cases

These fixtures pin down entrypoint resolution behavior for `type: cli.run`.

Coverage focus:

- explicit `harness.entrypoint` behavior
- capability-gated skip behavior for runtimes without `cli.run`

## SRCONF-CLI-001

```yaml contract-spec
id: SRCONF-CLI-001
title: conformance fixture sets explicit cli.run harness.entrypoint
purpose: Defines portable behavior for explicit cli.run entrypoint when capability
  is present.
type: contract.check
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
harness:
  entrypoint: spec_runner.conformance_fixtures:main
  check:
    profile: cli.run
    config:
      argv:
      - --help
      exit_code: 0
contract: []
```

## SRCONF-CLI-002

```yaml contract-spec
id: SRCONF-CLI-002
title: explicit entrypoint drives cli.run behavior deterministically
purpose: Pins deterministic behavior for explicit harness entrypoint execution.
type: contract.check
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
harness:
  entrypoint: spec_runner.conformance_fixtures:main
  check:
    profile: cli.run
    config:
      argv:
      - --json
      exit_code: 0
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        lit:
          lit:
            std.string.contains:
            - {var: subject}
            - '"ok": true'
  target: stdout
```
