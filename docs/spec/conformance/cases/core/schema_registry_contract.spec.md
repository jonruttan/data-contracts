# Schema Registry Contract Conformance Cases

## SRCONF-SCHEMA-REG-001

```yaml spec-test
id: SRCONF-SCHEMA-REG-001
title: schema docs include generated registry snapshot markers
purpose: Ensures generated schema registry snapshot markers and section header are present in schema_v1 documentation.
type: text.file
path: /docs/spec/schema/schema_v1.md
expect:
  portable:
    status: pass
    category: null
assert:
- target: text
  must:
  - evaluate:
    - {contains: [{var: subject}, 'BEGIN GENERATED: SCHEMA_REGISTRY_V1']}
    - {contains: [{var: subject}, 'END GENERATED: SCHEMA_REGISTRY_V1']}
    - {contains: [{var: subject}, Generated Registry Snapshot]}
```
