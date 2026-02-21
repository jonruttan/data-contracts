```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
title: schema case validation suite
imports:
- id: schema_ref_doc
  ref: '{{schema_ref}}'
  type: application/yaml
  inputs: {}
  outputs: {}
  options: {}
  doc:
    summary: schema reference import
exports:
- id: schema_ref_export
  ref: '{{schema_ref}}'
  type: application/json
  inputs: {}
  outputs: {}
  options: {}
  doc:
    summary: schema reference export
defaults:
  type: contract.check
contracts:
  - id: DCCONF-SCHEMA-CASE-001
    title: valid core shape compiles and runs
    purpose: Ensures standard top-level keys accepted by registry validation continue to execute
      successfully.
    expect:
      portable:
        status: pass
        category: null
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - text
      predicates:
      - id: assert_1
        assert:
          std.string.contains:
          - {var: text}
          - Spec-Test Schema (v2)
    harness:
      check:
        profile: text.file
        config: {}
  - id: DCCONF-SCHEMA-CASE-002
    title: unknown evaluate symbol is rejected as schema
    purpose: Ensures unknown spec-lang symbols fail as schema in both runtimes.
    expect:
      portable:
        status: fail
        category: schema
    clauses:
      defaults: {}
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
    harness:
      check:
        profile: text.file
        config: {}
  - id: DCCONF-SCHEMA-CASE-003
    title: contract export without top-level imports remains valid
    type: contract.export
    expect:
      portable:
        status: pass
        category: null
    clauses:
      defaults: {}
      predicates:
      - id: __export__schema.validation.ok
        assert:
          lit: true
    harness:
      exports:
      - as: schema.validation.ok
        from: assert.function
        path: /__export__schema.validation.ok
        params: []
        required: true
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
      tags: [contract.export]
      see_also: []
  - id: DCCONF-SCHEMA-CASE-004
    title: contract export top-level imports are rejected as schema
    type: contract.export
    expect:
      portable:
        status: fail
        category: schema
    imports:
    - /specs/libraries/domain/path_core.spec.md
    clauses:
      defaults: {}
      predicates:
      - id: __export__schema.validation.forbidden
        assert:
          lit: true
    harness:
      exports:
      - as: schema.validation.forbidden
        from: assert.function
        path: /__export__schema.validation.forbidden
        params: []
        required: true
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
      tags: [contract.export]
      see_also: []
```
