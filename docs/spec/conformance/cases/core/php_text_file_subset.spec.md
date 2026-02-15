# PHP Text File Subset Conformance Cases

## SRCONF-PHP-TEXT-001

```yaml spec-test
id: SRCONF-PHP-TEXT-001
title: text.file contain assertion passes in php bootstrap
purpose: Baseline positive contain check for the php text.file subset.
type: text.file
expect:
  portable:
    status: pass
    category: null
assert:
- target: text
  must:
  - evaluate:
    - contains:
      - {var: subject}
      - 'version: 1'
```

## SRCONF-PHP-TEXT-002

```yaml spec-test
id: SRCONF-PHP-TEXT-002
title: text.file regex assertion can fail in php bootstrap
purpose: Baseline failing regex check for the php text.file subset.
type: text.file
expect:
  portable:
    status: fail
    category: assertion
assert:
- target: text
  must:
  - evaluate:
    - regex_match:
      - {var: subject}
      - \A\Z
```

## SRCONF-PHP-TEXT-003

```yaml spec-test
id: SRCONF-PHP-TEXT-003
title: nested must group with inherited target passes
purpose: Verifies nested must groups inherit target from parent nodes.
type: text.file
expect:
  portable:
    status: pass
    category: null
assert:
- target: text
  must:
  - must:
    - evaluate:
      - contains:
        - {var: subject}
        - 'version: 1'
```

## SRCONF-PHP-TEXT-004

```yaml spec-test
id: SRCONF-PHP-TEXT-004
title: can passes when at least one branch passes
purpose: Verifies can succeeds when at least one branch succeeds.
type: text.file
expect:
  portable:
    status: pass
    category: null
assert:
- target: text
  can:
  - evaluate:
    - regex_match:
      - {var: subject}
      - (?!)
  - evaluate:
    - contains:
      - {var: subject}
      - 'version: 1'
```

## SRCONF-PHP-TEXT-005

```yaml spec-test
id: SRCONF-PHP-TEXT-005
title: can fails when all branches fail
purpose: Verifies can fails when every branch assertion fails.
type: text.file
expect:
  portable:
    status: fail
    category: assertion
assert:
- target: text
  can:
  - evaluate:
    - regex_match:
      - {var: subject}
      - \A\Z
  - evaluate:
    - regex_match:
      - {var: subject}
      - (?!)
```

## SRCONF-PHP-TEXT-006

```yaml spec-test
id: SRCONF-PHP-TEXT-006
title: cannot passes when all branches fail
purpose: Verifies cannot succeeds when every branch assertion fails.
type: text.file
expect:
  portable:
    status: pass
    category: null
assert:
- target: text
  cannot:
  - evaluate:
    - regex_match:
      - {var: subject}
      - \A\Z
  - evaluate:
    - regex_match:
      - {var: subject}
      - (?!)
```

## SRCONF-PHP-TEXT-007

```yaml spec-test
id: SRCONF-PHP-TEXT-007
title: cannot fails when any branch passes
purpose: Verifies cannot fails when at least one branch succeeds.
type: text.file
expect:
  portable:
    status: fail
    category: assertion
assert:
- target: text
  cannot:
  - evaluate:
    - contains:
      - {var: subject}
      - 'version: 1'
  - evaluate:
    - regex_match:
      - {var: subject}
      - (?!)
```

## SRCONF-PHP-TEXT-008

```yaml spec-test
id: SRCONF-PHP-TEXT-008
title: nested mixed groups with inherited target passes
purpose: Covers mixed nested must/can/cannot evaluation with inherited targets.
type: text.file
expect:
  portable:
    status: pass
    category: null
assert:
- target: text
  must:
  - can:
    - evaluate:
      - regex_match:
        - {var: subject}
        - \A\Z
    - evaluate:
      - contains:
        - {var: subject}
        - 'version: 1'
  - cannot:
    - evaluate:
      - regex_match:
        - {var: subject}
        - \A\Z
```

## SRCONF-PHP-TEXT-009

```yaml spec-test
id: SRCONF-PHP-TEXT-009
title: evaluate regex remains pass under assert_health error mode
purpose: Confirms evaluate regex assertions bypass sugar diagnostics and can pass under error
  mode.
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
    - regex_match:
      - {var: subject}
      - '(?<=version: )1'
```

## SRCONF-PHP-TEXT-010

```yaml spec-test
id: SRCONF-PHP-TEXT-010
title: evaluate empty contains remains pass under assert_health error mode
purpose: Confirms evaluate contains with empty string does not trigger sugar diagnostic failures
  in error mode.
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
    - contains:
      - {var: subject}
      - ''
```

## SRCONF-PHP-TEXT-011

```yaml spec-test
id: SRCONF-PHP-TEXT-011
title: evaluate always-true regex remains pass under assert_health error mode
purpose: Confirms evaluate regex assertions are evaluated directly without sugar-level AH002
  failures.
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
    - regex_match:
      - {var: subject}
      - .*
```

## SRCONF-PHP-TEXT-012

```yaml spec-test
id: SRCONF-PHP-TEXT-012
title: evaluate duplicate contains remain pass under assert_health error mode
purpose: Confirms evaluate duplicate contains expressions do not trigger sugar-level AH003
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
    - contains:
      - {var: subject}
      - 'version: 1'
    - contains:
      - {var: subject}
      - 'version: 1'
```

## SRCONF-PHP-TEXT-013

```yaml spec-test
id: SRCONF-PHP-TEXT-013
title: evaluate sibling branches remain pass under assert_health error mode
purpose: Confirms evaluate-only non-redundant sibling branches in can groups remain valid
  in error mode.
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
    - contains:
      - {var: subject}
      - 'version: 1'
  - evaluate:
    - contains:
      - {var: subject}
      - 'version: 2'
```

## SRCONF-PHP-TEXT-014

```yaml spec-test
id: SRCONF-PHP-TEXT-014
title: warn mode emits diagnostics without failing the case
purpose: Checks warn mode emits diagnostics without converting the case to failure.
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
    - contains:
      - {var: subject}
      - ''
```
