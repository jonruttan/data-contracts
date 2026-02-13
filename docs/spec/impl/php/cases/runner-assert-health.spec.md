# PHP Spec Runner Assertion Health Cases

## SRPHP-AH-001

```yaml spec-test
id: SRPHP-AH-001
title: cli.run warn mode emits diagnostics without failing
purpose: Verifies assert_health warn mode on cli.run preserves pass outcome while emitting warnings.
type: cli.run
argv: ["ok"]
exit_code: 0
harness:
  entrypoint: /bin/echo
expect:
  portable:
    status: pass
    category: null
assert_health:
  mode: warn
assert:
  - target: stdout
    must:
      - contain: [""]
```

## SRPHP-AH-002

```yaml spec-test
id: SRPHP-AH-002
title: cli.run error mode fails on assertion-health diagnostics
purpose: Verifies assert_health error mode on cli.run converts assertion-health findings into assertion failures.
type: cli.run
argv: ["ok"]
exit_code: 0
harness:
  entrypoint: /bin/echo
expect:
  portable:
    status: fail
    category: assertion
    message_tokens: ["AH001"]
assert_health:
  mode: error
assert:
  - target: stdout
    must:
      - contain: [""]
```

## SRPHP-AH-003

```yaml spec-test
id: SRPHP-AH-003
title: invalid assert_health mode is schema failure
purpose: Verifies invalid assert_health mode values are rejected as schema errors.
type: cli.run
argv: ["ok"]
exit_code: 0
harness:
  entrypoint: /bin/echo
expect:
  portable:
    status: fail
    category: schema
    message_tokens: ["assert_health.mode must be one of"]
assert_health:
  mode: nope
assert:
  - target: stdout
    must:
      - contain: ["ok"]
```
