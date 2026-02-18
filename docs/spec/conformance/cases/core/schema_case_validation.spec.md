# Schema Case Validation Conformance Cases

## SRCONF-SCHEMA-CASE-001

```yaml contract-spec
id: SRCONF-SCHEMA-CASE-001
title: valid core shape compiles and runs
purpose: Ensures standard top-level keys accepted by registry validation continue to execute
  successfully.
type: contract.check
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
        lit:
          lit:
            std.string.contains:
            - {var: subject}
            - Spec-Test Schema (v1)
  target: text
harness:
  check:
    profile: text.file
    config: {}
```

## SRCONF-SCHEMA-CASE-002

```yaml contract-spec
id: SRCONF-SCHEMA-CASE-002
title: unknown evaluate symbol is rejected as schema
purpose: Ensures unknown spec-lang symbols fail as schema in both runtimes.
type: contract.check
expect:
  portable:
    status: fail
    category: schema
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        lit:
          lit:
            unknown_symbol_for_schema_case:
            - {var: subject}
  target: text
harness:
  check:
    profile: text.file
    config: {}
```
