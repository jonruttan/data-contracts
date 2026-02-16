# Assertion Health Conformance Cases

These fixtures validate assertion-health behavior independent of a specific
runtime implementation.

Coverage focus:

- per-case `assert_health.mode` behavior (`warn`, `error`, `ignore`)
- canonical diagnostic codes (`AH001`-`AH005`)
- expected outcome category (`pass` vs assertion/schema failure)

## SRCONF-AH-001

```yaml spec-test
id: SRCONF-AH-001
title: assert_health warn emits diagnostics but case still passes
purpose: Covers warn mode behavior where diagnostics are emitted but verdict remains pass.
type: text.file
expect:
  portable:
    status: pass
    category: null
assert_health:
  mode: warn
assert:
- target: text
  must:
  - evaluate:
    - std.string.contains:
      - {var: subject}
      - ''
```

## SRCONF-AH-002

```yaml spec-test
id: SRCONF-AH-002
title: assert_health error mode can pass for evaluate-only assertions
purpose: Confirms error mode does not fail evaluate-only assertions when no assertion-health
  diagnostics are emitted.
type: text.file
expect:
  portable:
    status: pass
    category: null
assert_health:
  mode: error
assert:
- target: text
  must:
  - evaluate:
    - std.string.contains:
      - {var: subject}
      - ''
```

## SRCONF-AH-003

```yaml spec-test
id: SRCONF-AH-003
title: invalid assert_health.mode is a schema error
purpose: Ensures unsupported assert_health modes are rejected as schema violations.
type: text.file
expect:
  portable:
    status: fail
    category: schema
assert_health:
  mode: nope
assert:
- target: text
  must:
  - evaluate:
    - std.string.contains:
      - {var: subject}
      - spec-test
```

## SRCONF-AH-004

```yaml spec-test
id: SRCONF-AH-004
title: per-case ignore override can neutralize global strict mode
purpose: Verifies local mode override can disable stricter global assertion-health settings.
type: text.file
expect:
  portable:
    status: pass
    category: null
assert_health:
  mode: ignore
assert:
- target: text
  must:
  - evaluate:
    - std.string.contains:
      - {var: subject}
      - ''
```

## SRCONF-AH-005

```yaml spec-test
id: SRCONF-AH-005
title: evaluate-only sibling branches remain valid under assert_health error
purpose: Confirms evaluate-only non-redundant sibling branches do not trigger AH004 under
  assert_health error mode.
type: text.file
expect:
  portable:
    status: pass
    category: null
assert_health:
  mode: error
assert:
- target: text
  can:
  - evaluate:
    - std.string.contains:
      - {var: subject}
      - 'version: 1'
  - evaluate:
    - std.string.contains:
      - {var: subject}
      - 'version: 2'
```

## SRCONF-AH-006

```yaml spec-test
id: SRCONF-AH-006
title: evaluate regex portability is handled without sugar diagnostics
purpose: Confirms evaluate regex assertions are evaluated directly without sugar-level portability
  diagnostics.
type: text.file
expect:
  portable:
    status: pass
    category: null
assert_health:
  mode: error
assert:
- target: text
  must:
  - evaluate:
    - std.string.regex_match:
      - {var: subject}
      - '(?<=version: )1'
```
