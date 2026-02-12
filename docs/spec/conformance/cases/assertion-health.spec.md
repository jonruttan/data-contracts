# Assertion Health Conformance Cases

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
      - contain: [""]
```

## SRCONF-AH-002

```yaml spec-test
id: SRCONF-AH-002
title: assert_health error fails the case
purpose: Confirms error mode promotes assertion-health findings into assertion failures.
type: text.file
expect:
  portable:
    status: fail
    category: assertion
assert_health:
  mode: error
assert:
  - target: text
    must:
      - contain: [""]
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
      - contain: ["spec-test"]
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
      - contain: [""]
```

## SRCONF-AH-005

```yaml spec-test
id: SRCONF-AH-005
title: redundant sibling branches fail when assert_health mode is error
purpose: Guards against redundant can branches by requiring AH004 in error mode.
type: text.file
expect:
  portable:
    status: fail
    category: assertion
    message_tokens:
      - AH004
assert_health:
  mode: error
assert:
  - target: text
    can:
      - contain: ["version: 1"]
      - contain: ["version: 1"]
```

## SRCONF-AH-006

```yaml spec-test
id: SRCONF-AH-006
title: non-portable regex fails when assert_health mode is error
purpose: Checks non-portable regex constructs trigger AH005 in error mode.
type: text.file
expect:
  portable:
    status: fail
    category: assertion
    message_tokens:
      - AH005
assert_health:
  mode: error
assert:
  - target: text
    must:
      - regex: ["(?<=version: )1"]
```
