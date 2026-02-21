```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
title: schema case validation suite
artifact:
  imports:
  - id: schema_ref_doc
    ref: "{{schema_ref}}"
    type: application/yaml
    inputs: {}
    options: {}
    doc:
      summary: schema reference import
  exports:
  - id: schema_ref_export
    ref: "{{schema_ref}}"
    type: application/json
    options: {}
    doc:
      summary: schema reference export
exports:
- as: schema.validation.ok
  from: assert.function
  path: "/__export__schema.validation.ok"
  params: []
  required: true
- as: schema.validation.forbidden
  from: assert.function
  path: "/__export__schema.validation.forbidden"
  params: []
  required: true
contracts:
- id: DCCONF-SCHEMA-CASE-001
  title: valid core shape compiles and runs
  purpose: Ensures standard top-level keys accepted by registry validation continue to execute successfully.
  expect:
    portable:
      status: pass
      category:
  clauses:
    imports:
    - from: artifact
      names:
      - text
    predicates:
    - id: assert_1
      assert:
        std.string.contains:
        - var: text
        - Spec-Test Schema (v2)
    profile: text.file
    config: {}
  harness: check
- id: DCCONF-SCHEMA-CASE-002
  title: unknown evaluate symbol is rejected as schema
  purpose: Ensures unknown spec-lang symbols fail as schema in both runtimes.
  expect:
    portable:
      status: fail
      category: schema
  clauses:
    imports:
    - from: artifact
      names:
      - text
    predicates:
    - id: assert_1
      assert:
        lit:
          unknown_symbol_for_schema_case:
          - var: text
    profile: text.file
    config: {}
  harness: check
- id: DCCONF-SCHEMA-CASE-003
  title: contract export without top-level imports remains valid
  expect:
    portable:
      status: pass
      category:
  clauses:
    predicates:
    - id: __export__schema.validation.ok
      assert:
        lit: true
  harness: export
  library:
    id: schema.validation.core
    module: schema
    stability: alpha
    owner: data-contracts
  doc:
    summary: schema export validation case
    description: Valid contract.export shape without deprecated top-level imports.
    audience: spec-authors
    since: v2
    tags:
    - contract.export
    see_also: []
- id: DCCONF-SCHEMA-CASE-004
  title: contract export top-level imports are rejected as schema
  expect:
    portable:
      status: fail
      category: schema
  imports:
  - "/specs/libraries/domain/path_core.spec.md"
  clauses:
    predicates:
    - id: __export__schema.validation.forbidden
      assert:
        lit: true
  harness: export
  library:
    id: schema.validation.forbidden
    module: schema
    stability: alpha
    owner: data-contracts
  doc:
    summary: schema export invalid imports case
    description: Deprecated contract.export top-level imports must hard-fail in v2.
    audience: spec-authors
    since: v2
    tags:
    - contract.export
    see_also: []
- id: DCCONF-SCHEMA-CASE-005
  title: missing harness is rejected as schema
  expect:
    portable:
      status: fail
      category: schema
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
- id: DCCONF-SCHEMA-CASE-006
  title: unknown harness is rejected as schema
  expect:
    portable:
      status: fail
      category: schema
  harness: unknown_harness
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
- id: DCCONF-SCHEMA-CASE-007
  title: legacy type field is rejected as schema
  expect:
    portable:
      status: fail
      category: schema
  type: contract.check
  harness: check
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
- id: DCCONF-SCHEMA-CASE-008
  title: root imports surface is rejected as schema
  expect:
    portable:
      status: fail
      category: schema
  imports:
  - id: legacy_import
    ref: "/specs/schema/schema_v2.md"
  harness: check
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
- id: DCCONF-SCHEMA-CASE-009
  title: root exports mode key is rejected as schema
  expect:
    portable:
      status: fail
      category: schema
  exports:
  - as: schema.validation.invalid_mode
    mode: function
    from: assert.function
    path: "/__export__schema.validation.ok"
  harness: check
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
- id: DCCONF-SCHEMA-CASE-010
  title: root exports id key is rejected as schema
  expect:
    portable:
      status: fail
      category: schema
  exports:
  - id: schema.validation.invalid_id
    as: schema.validation.invalid_id
    from: assert.function
    path: "/__export__schema.validation.ok"
  harness: check
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
- id: DCCONF-SCHEMA-CASE-011
  title: root exports ref key is rejected as schema
  expect:
    portable:
      status: fail
      category: schema
  exports:
  - as: schema.validation.invalid_ref
    from: assert.function
    path: "/__export__schema.validation.ok"
    ref: "/specs/schema/schema_v2.md"
  harness: check
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
- id: DCCONF-SCHEMA-CASE-012
  title: root exports from must be assert function
  expect:
    portable:
      status: fail
      category: schema
  exports:
  - as: schema.validation.invalid_from
    from: custom.function
    path: "/__export__schema.validation.ok"
  harness: check
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
- id: DCCONF-SCHEMA-CASE-013
  title: artifact import missing ref is rejected as schema
  expect:
    portable:
      status: fail
      category: schema
  artifact:
    imports:
    - id: missing_ref
  harness: check
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
- id: DCCONF-SCHEMA-CASE-014
  title: artifact export forbids inputs and outputs keys
  expect:
    portable:
      status: fail
      category: schema
  artifact:
    exports:
    - id: invalid_artifact_export
      ref: "/specs/schema/schema_v2.md"
      inputs: {}
      outputs: {}
  harness: check
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
- id: DCCONF-SCHEMA-CASE-015
  title: artifact export missing id is rejected as schema
  expect:
    portable:
      status: fail
      category: schema
  artifact:
    exports:
    - ref: "/specs/schema/schema_v2.md"
  harness: check
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
- id: DCCONF-SCHEMA-CASE-016
  title: unresolved artifact template reference fails
  expect:
    portable:
      status: fail
      category: schema
  artifact:
    imports:
    - id: unresolved_template
      ref: "{{unknown_suite_var}}"
  harness: check
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
```
