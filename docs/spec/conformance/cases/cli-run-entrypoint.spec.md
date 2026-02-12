# CLI Entry Point Conformance Cases

## SRCONF-CLI-001

```yaml spec-test
id: SRCONF-CLI-001
title: conformance fixture sets explicit cli.run harness.entrypoint
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
argv: ["--json"]
exit_code: 0
harness:
  entrypoint: spec_runner.conformance_fixtures:main
  env:
    SPEC_RUNNER_ENTRYPOINT: does.not.exist:main
assert:
  - target: stdout
    must:
      - contain: ['"ok": true']
```
