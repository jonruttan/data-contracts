# Spec-Lang Metadata Domain Library

## LIB-DOMAIN-META-001

```yaml contract-spec
id: LIB-DOMAIN-META-001-001-DOMAIN-META-CASE-ID-EQ
type: spec.export
contract:
- id: __export__domain.meta.case_id_eq
  class: must
  asserts:
  - std.logic.eq:
    - std.object.get:
      - std.object.get:
        - var: meta
        - case
      - id
    - var: case_id
harness:
  chain:
    exports:
    - as: domain.meta.case_id_eq
      from: assert.function
      path: /__export__domain.meta.case_id_eq
      params:
      - meta
      - case_id
      required: true
```

```yaml contract-spec
id: LIB-DOMAIN-META-001-002-DOMAIN-META-HAS-ARTIFACT-TARGET
type: spec.export
contract:
- id: __export__domain.meta.has_artifact_target
  class: must
  asserts:
  - std.collection.includes:
    - std.object.get:
      - std.object.get:
        - var: meta
        - artifacts
      - target_keys
    - var: target_name
harness:
  chain:
    exports:
    - as: domain.meta.has_artifact_target
      from: assert.function
      path: /__export__domain.meta.has_artifact_target
      params:
      - meta
      - target_name
      required: true
```
