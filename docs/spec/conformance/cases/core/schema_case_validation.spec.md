# Schema Case Validation Conformance Cases

## SRCONF-SCHEMA-CASE-001

```yaml spec-test
id: SRCONF-SCHEMA-CASE-001
title: valid core shape compiles and runs
purpose: Ensures standard top-level keys accepted by registry validation continue to execute successfully.
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
      - var: subject
      - Spec-Test Schema (v1)
```

## SRCONF-SCHEMA-CASE-002

```yaml spec-test
id: SRCONF-SCHEMA-CASE-002
title: unknown top-level key is rejected as schema
purpose: Ensures registry-driven validation hard-fails unknown top-level case keys.
type: text.file
bogus_extra: true
expect:
  portable:
    status: fail
    category: schema
assert:
- target: text
  must:
  - evaluate:
    - contains:
      - var: subject
      - Spec-Test Schema (v1)
```
