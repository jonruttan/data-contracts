# CLI Entry Point Conformance Cases

These fixtures pin down entrypoint resolution behavior for `type: cli.run`.

Coverage focus:

- explicit `harness.entrypoint` behavior
- precedence over env fallback values
- capability-gated skip behavior for runtimes without `cli.run`

## SRCONF-CLI-001

```yaml spec-test
id: SRCONF-CLI-001
title: conformance fixture sets explicit cli.run harness.entrypoint
purpose: Defines portable behavior for explicit cli.run entrypoint when capability is present.
type: cli.run
requires:
  capabilities: ["cli.run"]
  when_missing: skip
expect:
  portable:
    status: pass
    category: null
  impl:
    php:
      status: skip
      category: null
argv: ["--help"]
exit_code: 0
harness:
  entrypoint: spec_runner.conformance_fixtures:main
assert: []
```

## SRCONF-CLI-002

```yaml spec-test
id: SRCONF-CLI-002
title: explicit entrypoint is used even if env fallback var is set
purpose: Prevents env fallback from overriding an explicitly declared harness entrypoint.
type: cli.run
requires:
  capabilities: [cli.run]
  when_missing: skip
expect:
  portable: {status: pass, category: null}
  impl:
    php: {status: skip, category: null}
argv: [--json]
exit_code: 0
harness:
  entrypoint: spec_runner.conformance_fixtures:main
  env: {SPEC_RUNNER_ENTRYPOINT: 'does.not.exist:main'}
assert:
  - target: stdout
    must:
      - evaluate:
          - ["contains", ["subject"], "\"ok\": true"]
```
