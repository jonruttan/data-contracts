# Spec-Lang Metadata Domain Library

## LIB-DOMAIN-META-001

```yaml contract-spec
id: LIB-DOMAIN-META-001-001-DOMAIN-META-CASE-ID-EQ
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__domain.meta.case_id_eq
    assert:
      std.logic.eq:
      - std.object.get:
        - std.object.get:
          - {var: meta}
          - case
        - id
      - {var: case_id}
harness:
  exports:
  - as: domain.meta.case_id_eq
    from: assert.function
    path: /__export__domain.meta.case_id_eq
    params:
    - meta
    - case_id
    required: true
    doc:
      summary: Contract export for `domain.meta.case_id_eq`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: meta
        type: any
        required: true
        description: Input parameter `meta`.
      - name: case_id
        type: any
        required: true
        description: Input parameter `case_id`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          meta: <meta>
          case_id: <case_id>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.meta.core
  module: domain
  stability: alpha
  owner: spec_runner
  tags:
  - domain
```

```yaml contract-spec
id: LIB-DOMAIN-META-001-002-DOMAIN-META-HAS-ARTIFACT-TARGET
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__domain.meta.has_artifact_target
    assert:
      std.collection.includes:
      - std.object.get:
        - std.object.get:
          - {var: meta}
          - artifacts
        - target_keys
      - {var: target_name}
harness:
  exports:
  - as: domain.meta.has_artifact_target
    from: assert.function
    path: /__export__domain.meta.has_artifact_target
    params:
    - meta
    - target_name
    required: true
    doc:
      summary: Contract export for `domain.meta.has_artifact_target`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: meta
        type: any
        required: true
        description: Input parameter `meta`.
      - name: target_name
        type: any
        required: true
        description: Input parameter `target_name`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          meta: <meta>
          target_name: <target_name>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.meta.core
  module: domain
  stability: alpha
  owner: spec_runner
  tags:
  - domain
```
