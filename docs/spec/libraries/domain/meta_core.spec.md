# Spec-Lang Metadata Domain Library

## LIB-DOMAIN-META-001

```yaml spec-test
id: LIB-DOMAIN-META-001-001-DOMAIN-META-CASE-ID-EQ
type: spec.export
assert:
- id: __export__domain.meta.case_id_eq
  class: must
  checks:
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

```yaml spec-test
id: LIB-DOMAIN-META-001-002-DOMAIN-META-HAS-ARTIFACT-TARGET
type: spec.export
assert:
- id: __export__domain.meta.has_artifact_target
  class: must
  checks:
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
