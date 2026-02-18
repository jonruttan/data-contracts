# PHP Text File Subset Conformance Cases

## SRCONF-PHP-TEXT-001

```yaml contract-spec
id: SRCONF-PHP-TEXT-001
title: text.file contain assertion passes in php bootstrap
purpose: Baseline positive contain check for the php text.file subset.
type: text.file
expect:
  portable:
    status: pass
    category: null
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.string.contains:
    - var: subject
    - 'version: 1'
  target: text
```

## SRCONF-PHP-TEXT-002

```yaml contract-spec
id: SRCONF-PHP-TEXT-002
title: text.file regex assertion can fail in php bootstrap
purpose: Baseline failing regex check for the php text.file subset.
type: text.file
expect:
  portable:
    status: fail
    category: assertion
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.string.regex_match:
    - var: subject
    - \A\Z
  target: text
```

## SRCONF-PHP-TEXT-003

```yaml contract-spec
id: SRCONF-PHP-TEXT-003
title: nested must group with inherited target passes
purpose: Verifies nested must groups inherit target from parent nodes.
type: text.file
expect:
  portable:
    status: pass
    category: null
contract:
- id: assert_1
  class: MUST
  asserts:
  - MUST:
    - std.string.contains:
      - var: subject
      - 'version: 1'
  target: text
```

## SRCONF-PHP-TEXT-004

```yaml contract-spec
id: SRCONF-PHP-TEXT-004
title: can passes when at least one branch passes
purpose: Verifies can succeeds when at least one branch succeeds.
type: text.file
expect:
  portable:
    status: pass
    category: null
contract:
- id: assert_1
  class: MAY
  asserts:
  - std.string.regex_match:
    - var: subject
    - (?!)
  - std.string.contains:
    - var: subject
    - 'version: 1'
  target: text
```

## SRCONF-PHP-TEXT-005

```yaml contract-spec
id: SRCONF-PHP-TEXT-005
title: can fails when all branches fail
purpose: Verifies can fails when every branch assertion fails.
type: text.file
expect:
  portable:
    status: fail
    category: assertion
contract:
- id: assert_1
  class: MAY
  asserts:
  - std.string.regex_match:
    - var: subject
    - \A\Z
  - std.string.regex_match:
    - var: subject
    - (?!)
  target: text
```

## SRCONF-PHP-TEXT-006

```yaml contract-spec
id: SRCONF-PHP-TEXT-006
title: cannot passes when all branches fail
purpose: Verifies cannot succeeds when every branch assertion fails.
type: text.file
expect:
  portable:
    status: pass
    category: null
contract:
- id: assert_1
  class: MUST_NOT
  asserts:
  - std.string.regex_match:
    - var: subject
    - \A\Z
  - std.string.regex_match:
    - var: subject
    - (?!)
  target: text
```

## SRCONF-PHP-TEXT-007

```yaml contract-spec
id: SRCONF-PHP-TEXT-007
title: cannot fails when any branch passes
purpose: Verifies cannot fails when at least one branch succeeds.
type: text.file
expect:
  portable:
    status: fail
    category: assertion
contract:
- id: assert_1
  class: MUST_NOT
  asserts:
  - std.string.contains:
    - var: subject
    - 'version: 1'
  - std.string.regex_match:
    - var: subject
    - (?!)
  target: text
```

## SRCONF-PHP-TEXT-008

```yaml contract-spec
id: SRCONF-PHP-TEXT-008
title: nested mixed groups with inherited target passes
purpose: Covers mixed nested must/can/cannot evaluation with inherited targets.
type: text.file
expect:
  portable:
    status: pass
    category: null
contract:
- id: assert_1
  class: MUST
  asserts:
  - MAY:
    - std.string.regex_match:
      - var: subject
      - \A\Z
    - std.string.contains:
      - var: subject
      - 'version: 1'
  - MUST_NOT:
    - std.string.regex_match:
      - var: subject
      - \A\Z
  target: text
```

## SRCONF-PHP-TEXT-009

```yaml contract-spec
id: SRCONF-PHP-TEXT-009
title: evaluate regex remains pass under assert_health error mode
purpose: Confirms evaluate regex assertions bypass sugar diagnostics and can pass
  under error mode.
type: text.file
expect:
  portable:
    status: pass
    category: null
assert_health:
  mode: error
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.string.regex_match:
    - var: subject
    - '(?<=version: )1'
  target: text
```

## SRCONF-PHP-TEXT-010

```yaml contract-spec
id: SRCONF-PHP-TEXT-010
title: evaluate empty contains remains pass under assert_health error mode
purpose: Confirms evaluate contains with empty string does not trigger sugar diagnostic
  failures in error mode.
type: text.file
expect:
  portable:
    status: pass
    category: null
assert_health:
  mode: error
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.string.contains:
    - var: subject
    - ''
  target: text
```

## SRCONF-PHP-TEXT-011

```yaml contract-spec
id: SRCONF-PHP-TEXT-011
title: evaluate always-true regex remains pass under assert_health error mode
purpose: Confirms evaluate regex assertions are evaluated directly without sugar-level
  AH002 failures.
type: text.file
expect:
  portable:
    status: pass
    category: null
assert_health:
  mode: error
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.string.regex_match:
    - var: subject
    - .*
  target: text
```

## SRCONF-PHP-TEXT-012

```yaml contract-spec
id: SRCONF-PHP-TEXT-012
title: evaluate duplicate contains remain pass under assert_health error mode
purpose: Confirms evaluate duplicate contains expressions do not trigger sugar-level
  AH003 diagnostics.
type: text.file
expect:
  portable:
    status: fail
    category: assertion
    message_tokens:
    - AH004
    - contract[0].asserts[0].MUST
assert_health:
  mode: error
contract:
- id: assert_1
  class: MUST
  asserts:
  - MUST:
    - std.string.contains:
      - var: subject
      - 'version: 1'
    - std.string.contains:
      - var: subject
      - 'version: 1'
  target: text
```

## SRCONF-PHP-TEXT-013

```yaml contract-spec
id: SRCONF-PHP-TEXT-013
title: evaluate sibling branches remain pass under assert_health error mode
purpose: Confirms evaluate-only non-redundant sibling branches in can groups remain
  valid in error mode.
type: text.file
expect:
  portable:
    status: pass
    category: null
assert_health:
  mode: error
contract:
- id: assert_1
  class: MAY
  asserts:
  - std.string.contains:
    - var: subject
    - 'version: 1'
  - std.string.contains:
    - var: subject
    - 'version: 2'
  target: text
```

## SRCONF-PHP-TEXT-014

```yaml contract-spec
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
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.string.contains:
    - var: subject
    - ''
  target: text
```
