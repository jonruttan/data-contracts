# Schema Registry Contract Conformance Cases

## SRCONF-SCHEMA-REG-001

```yaml contract-spec
id: SRCONF-SCHEMA-REG-001
title: schema docs include generated registry snapshot markers
purpose: Ensures generated schema registry snapshot markers and section header are present
  in schema_v1 documentation.
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
        MUST:
        - std.string.contains:
          - {var: subject}
          - 'BEGIN GENERATED: SCHEMA_REGISTRY_V1'
        - std.string.contains:
          - {var: subject}
          - 'END GENERATED: SCHEMA_REGISTRY_V1'
        - std.string.contains:
          - {var: subject}
          - Generated Registry Snapshot
  target: text
harness:
  check:
    profile: text.file
    config:
      path: /docs/spec/schema/schema_v1.md
```
