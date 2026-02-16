# Schema Case Validation Conformance Cases

## SRCONF-SCHEMA-CASE-001

```yaml spec-test
id: SRCONF-SCHEMA-CASE-001
title: valid core shape compiles and runs
purpose: Ensures standard top-level keys accepted by registry validation continue
  to execute successfully.
type: text.file
expect:
  portable:
    status: pass
    category: null
assert:
- id: assert_1
  class: must
  checks:
  - std.string.contains:
    - var: subject
    - Spec-Test Schema (v1)
  target: text
```

## SRCONF-SCHEMA-CASE-002

```yaml spec-test
id: SRCONF-SCHEMA-CASE-002
title: unknown evaluate symbol is rejected as schema
purpose: Ensures unknown spec-lang symbols fail as schema in both runtimes.
type: text.file
expect:
  portable:
    status: fail
    category: schema
assert:
- id: assert_1
  class: must
  checks:
  - unknown_symbol_for_schema_case:
    - var: subject
  target: text
```
