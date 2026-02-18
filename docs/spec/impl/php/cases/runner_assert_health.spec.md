# PHP Spec Runner Assertion Health Cases

## SRPHP-AH-001

```yaml contract-spec
id: SRPHP-AH-001
title: cli.run warn mode emits diagnostics without failing
purpose: Verifies assert_health warn mode on cli.run preserves pass outcome while emitting
  warnings.
type: contract.check
harness:
  entrypoint: /bin/echo
  check:
    profile: cli.run
    config:
      argv:
      - ok
      exit_code: 0
expect:
  portable:
    status: pass
    category: null
assert_health:
  mode: warn
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        MUST:
        - std.string.contains:
          - {var: subject}
          - ok
        - std.string.contains:
          - {var: subject}
          - ok
  target: stdout
```

## SRPHP-AH-002

```yaml contract-spec
id: SRPHP-AH-002
title: cli.run error mode fails on assertion-health diagnostics
purpose: Verifies assert_health error mode on cli.run converts assertion-health findings into
  assertion failures.
type: contract.check
harness:
  entrypoint: /bin/echo
  check:
    profile: cli.run
    config:
      argv:
      - ok
      exit_code: 0
expect:
  portable:
    status: fail
    category: assertion
    message_tokens:
    - AH004
assert_health:
  mode: error
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        MUST:
        - std.string.contains:
          - {var: subject}
          - ok
        - std.string.contains:
          - {var: subject}
          - ok
  target: stdout
```

## SRPHP-AH-003

```yaml contract-spec
id: SRPHP-AH-003
title: invalid assert_health mode is schema failure
purpose: Verifies invalid assert_health mode values are rejected as schema errors.
type: contract.check
harness:
  entrypoint: /bin/echo
  check:
    profile: cli.run
    config:
      argv:
      - ok
      exit_code: 0
expect:
  portable:
    status: fail
    category: schema
    message_tokens:
    - assert_health.mode must be one of
assert_health:
  mode: nope
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        std.string.contains:
        - {var: subject}
        - ok
  target: stdout
```

## SRPHP-AH-004

```yaml contract-spec
id: SRPHP-AH-004
title: global assert health mode applies when case mode is omitted
purpose: Verifies SPEC_RUNNER_ASSERT_HEALTH controls diagnostics when assert_health.mode is
  not set in a case.
type: contract.check
harness:
  entrypoint: /bin/echo
  check:
    profile: cli.run
    config:
      argv:
      - ok
      exit_code: 0
expect:
  portable:
    status: pass
    category: null
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        MUST:
        - std.string.contains:
          - {var: subject}
          - ok
        - std.string.contains:
          - {var: subject}
          - ok
  target: stdout
```

## SRPHP-AH-005

```yaml contract-spec
id: SRPHP-AH-005
title: per-case ignore overrides global warn policy
purpose: Verifies assert_health.mode ignore suppresses diagnostics even when global policy
  is warn.
type: contract.check
harness:
  entrypoint: /bin/echo
  check:
    profile: cli.run
    config:
      argv:
      - ok
      exit_code: 0
expect:
  portable:
    status: pass
    category: null
assert_health:
  mode: ignore
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        MUST:
        - std.string.contains:
          - {var: subject}
          - ok
        - std.string.contains:
          - {var: subject}
          - ok
  target: stdout
```
