# Assertion Health Conformance Cases

## SRCONF-AH-001

```yaml spec-test
id: SRCONF-AH-001
title: assert_health warn emits diagnostics but case still passes
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
