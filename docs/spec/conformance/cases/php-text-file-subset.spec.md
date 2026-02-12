# PHP Text File Subset Conformance Cases

## SRCONF-PHP-TEXT-001

```yaml spec-test
id: SRCONF-PHP-TEXT-001
title: text.file contain assertion passes in php bootstrap
type: text.file
expect:
  portable:
    status: pass
    category: null
assert:
  - target: text
    must:
      - contain: ["version: 1"]
```

## SRCONF-PHP-TEXT-002

```yaml spec-test
id: SRCONF-PHP-TEXT-002
title: text.file regex assertion can fail in php bootstrap
type: text.file
expect:
  portable:
    status: fail
    category: assertion
assert:
  - target: text
    must:
      - regex: ["\\A\\Z"]
```

## SRCONF-PHP-TEXT-003

```yaml spec-test
id: SRCONF-PHP-TEXT-003
title: nested must group with inherited target passes
type: text.file
expect:
  portable:
    status: pass
    category: null
assert:
  - target: text
    must:
      - must:
          - contain: ["version: 1"]
```

## SRCONF-PHP-TEXT-004

```yaml spec-test
id: SRCONF-PHP-TEXT-004
title: can passes when at least one branch passes
type: text.file
expect:
  portable:
    status: pass
    category: null
assert:
  - target: text
    can:
      - regex: ["(?!)"]
      - contain: ["version: 1"]
```

## SRCONF-PHP-TEXT-005

```yaml spec-test
id: SRCONF-PHP-TEXT-005
title: can fails when all branches fail
type: text.file
expect:
  portable:
    status: fail
    category: assertion
assert:
  - target: text
    can:
      - regex: ["\\A\\Z"]
      - regex: ["(?!)"]
```

## SRCONF-PHP-TEXT-006

```yaml spec-test
id: SRCONF-PHP-TEXT-006
title: cannot passes when all branches fail
type: text.file
expect:
  portable:
    status: pass
    category: null
assert:
  - target: text
    cannot:
      - regex: ["\\A\\Z"]
      - regex: ["(?!)"]
```

## SRCONF-PHP-TEXT-007

```yaml spec-test
id: SRCONF-PHP-TEXT-007
title: cannot fails when any branch passes
type: text.file
expect:
  portable:
    status: fail
    category: assertion
assert:
  - target: text
    cannot:
      - contain: ["version: 1"]
      - regex: ["(?!)"]
```

## SRCONF-PHP-TEXT-008

```yaml spec-test
id: SRCONF-PHP-TEXT-008
title: nested mixed groups with inherited target passes
type: text.file
expect:
  portable:
    status: pass
    category: null
assert:
  - target: text
    must:
      - can:
          - regex: ["\\A\\Z"]
          - contain: ["version: 1"]
      - cannot:
          - regex: ["\\A\\Z"]
```

## SRCONF-PHP-TEXT-009

```yaml spec-test
id: SRCONF-PHP-TEXT-009
title: non-portable regex fails under assert_health error mode
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

## SRCONF-PHP-TEXT-010

```yaml spec-test
id: SRCONF-PHP-TEXT-010
title: AH001 empty contain fails under assert_health error mode
type: text.file
expect:
  portable:
    status: fail
    category: assertion
    message_tokens:
      - AH001
assert_health:
  mode: error
assert:
  - target: text
    must:
      - contain: [""]
```

## SRCONF-PHP-TEXT-011

```yaml spec-test
id: SRCONF-PHP-TEXT-011
title: AH002 always-true regex fails under assert_health error mode
type: text.file
expect:
  portable:
    status: fail
    category: assertion
    message_tokens:
      - AH002
assert_health:
  mode: error
assert:
  - target: text
    must:
      - regex: [".*"]
```

## SRCONF-PHP-TEXT-012

```yaml spec-test
id: SRCONF-PHP-TEXT-012
title: AH003 duplicate contain values fail under assert_health error mode
type: text.file
expect:
  portable:
    status: fail
    category: assertion
    message_tokens:
      - AH003
assert_health:
  mode: error
assert:
  - target: text
    must:
      - contain: ["version: 1", "version: 1"]
```

## SRCONF-PHP-TEXT-013

```yaml spec-test
id: SRCONF-PHP-TEXT-013
title: AH004 redundant branch fails under assert_health error mode
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

## SRCONF-PHP-TEXT-014

```yaml spec-test
id: SRCONF-PHP-TEXT-014
title: warn mode emits diagnostics without failing the case
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
