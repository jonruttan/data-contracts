```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
title: schema case validation suite
harness:
  type: unit.test
  profile: export
  config:
    legacy_contract_harnesses:
    - check
    - export
    - unknown_harness
services:
  actions:
  - id: svc.check.text_file.1
    type: io.fs
    io: input
    profile: read.text
  - id: svc.check.default.1
    type: io.fs
    io: input
    profile: read.text
    imports:
    - pipe_identity
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
    - artifact:
      - text
    predicates:
    - id: assert_1
      assert:
        std.string.contains:
        - var: text
        - Spec-Test Schema (v2)
- id: DCCONF-SCHEMA-CASE-002
  title: unknown evaluate symbol is rejected as schema
  purpose: Ensures unknown spec-lang symbols fail as schema in both runtimes.
  expect:
    portable:
      status: fail
      category: schema
  clauses:
    imports:
    - artifact:
      - text
    predicates:
    - id: assert_1
      assert:
        lit:
          unknown_symbol_for_schema_case:
          - var: text
- id: DCCONF-SCHEMA-CASE-003
  title: contract export without top-level imports remains valid under suite harness/services
  docs:
  - summary: schema export validation case
    audience: spec-authors
    status: active
    description: Valid contract.export shape without deprecated top-level imports.
    since: v2
    tags:
    - contract.export
  expect:
    portable:
      status: pass
      category:
  clauses:
    predicates:
    - id: __export__schema.validation.ok
      assert:
        lit: true
  library:
    id: schema.validation.core
    module: schema
    stability: alpha
    owner: data-contracts
- id: DCCONF-SCHEMA-CASE-004
  title: contract export top-level imports are rejected as schema
  docs:
  - summary: schema export invalid imports case
    audience: spec-authors
    status: active
    description: Deprecated contract.export top-level imports must hard-fail in v2.
    since: v2
    tags:
    - contract.export
  expect:
    portable:
      status: fail
      category: schema
  clauses:
    predicates:
    - id: __export__schema.validation.forbidden
      assert:
        lit: true
  library:
    id: schema.validation.forbidden
    module: schema
    stability: alpha
    owner: data-contracts
  imports:
  - "/specs/libraries/domain/path_core.spec.md"
- id: DCCONF-SCHEMA-CASE-005
  title: contract-level harness is rejected as schema
  expect:
    portable:
      status: fail
      category: schema
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
  harness: check
- id: DCCONF-SCHEMA-CASE-006
  title: contract-level clauses profile is rejected as schema
  expect:
    portable:
      status: fail
      category: schema
  clauses:
    profile: read.text
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
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
  type: contract.check
- id: DCCONF-SCHEMA-CASE-008
  title: root imports surface is rejected as schema
  expect:
    portable:
      status: fail
      category: schema
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
  imports:
  - id: legacy_import
    ref: "/specs/schema/schema_v2.md"
- id: DCCONF-SCHEMA-CASE-009
  title: root exports mode key is rejected as schema
  expect:
    portable:
      status: fail
      category: schema
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
  exports:
  - as: schema.validation.invalid_mode
    mode: function
    from: assert.function
    path: "/__export__schema.validation.ok"
- id: DCCONF-SCHEMA-CASE-010
  title: root exports id key is rejected as schema
  expect:
    portable:
      status: fail
      category: schema
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
  exports:
  - id: schema.validation.invalid_id
    as: schema.validation.invalid_id
    from: assert.function
    path: "/__export__schema.validation.ok"
- id: DCCONF-SCHEMA-CASE-011
  title: root exports ref key is rejected as schema
  expect:
    portable:
      status: fail
      category: schema
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
  exports:
  - as: schema.validation.invalid_ref
    from: assert.function
    path: "/__export__schema.validation.ok"
    ref: "/specs/schema/schema_v2.md"
- id: DCCONF-SCHEMA-CASE-012
  title: root exports from must be assert function
  expect:
    portable:
      status: fail
      category: schema
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
  exports:
  - as: schema.validation.invalid_from
    from: custom.function
    path: "/__export__schema.validation.ok"
- id: DCCONF-SCHEMA-CASE-013
  title: artifacts entry missing ref is rejected as schema
  expect:
    portable:
      status: fail
      category: schema
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
  artifacts:
  - id: missing_ref
    io: input
- id: DCCONF-SCHEMA-CASE-014
  title: artifacts entry missing io is rejected as schema
  expect:
    portable:
      status: fail
      category: schema
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
  artifacts:
  - id: invalid_artifact
    ref: "/specs/schema/schema_v2.md"
- id: DCCONF-SCHEMA-CASE-015
  title: artifacts entry invalid io enum is rejected as schema
  expect:
    portable:
      status: fail
      category: schema
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
  artifacts:
  - id: bad_io
    ref: "/specs/schema/schema_v2.md"
    io: inbound
- id: DCCONF-SCHEMA-CASE-016
  title: unresolved artifact template reference fails
  expect:
    portable:
      status: fail
      category: schema
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
  artifacts:
  - id: unresolved_template
    ref: "{{unknown_suite_var}}"
    io: input
- id: DCCONF-SCHEMA-CASE-017
  title: legacy singular doc is rejected as schema
  expect:
    portable:
      status: fail
      category: schema
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
  doc:
    summary: legacy singular doc
- id: DCCONF-SCHEMA-CASE-018
  title: docs entry missing required status is rejected as schema
  docs:
  - summary: missing status
    audience: spec-authors
  expect:
    portable:
      status: fail
      category: schema
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
- id: DCCONF-SCHEMA-CASE-019
  title: docs entry invalid type enum is rejected as schema
  docs:
  - summary: invalid docs type
    audience: spec-authors
    status: active
    type: narrative
  expect:
    portable:
      status: fail
      category: schema
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
- id: DCCONF-SCHEMA-CASE-020
  title: docs entry duplicate ids are rejected as schema
  docs:
  - summary: docs entry one
    audience: spec-authors
    status: active
  - summary: docs entry two
    audience: spec-authors
    status: active
  expect:
    portable:
      status: fail
      category: schema
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
- id: DCCONF-SCHEMA-CASE-021
  title: docs entry unknown key is rejected as schema
  docs:
  - summary: docs entry with unknown key
    audience: spec-authors
    status: active
    unknown_field: true
  expect:
    portable:
      status: fail
      category: schema
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
- id: DCCONF-SCHEMA-CASE-022
  title: valid contract binding entry is accepted
  expect:
    portable:
      status: pass
      category:
  bindings:
    defaults:
      import: pipe_identity
      mode: merge
    rows:
    - id: bind_schema_case_022
      service: svc.check.default.1
      inputs:
      - from: schema_ref_doc
        as: source_text
      outputs:
      - to: schema_ref_export
        as: piped_text
      predicates:
      - assert_1
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
- id: DCCONF-SCHEMA-CASE-023
  title: service import with declared service is accepted
  expect:
    portable:
      status: pass
      category:
  clauses:
    imports:
    - service:
        id: svc.check.default.1
        names:
        - pipe_identity
        as:
          pipe_identity: subject
    predicates:
    - id: assert_1
      assert:
        std.logic.eq:
        - var: subject
        - pipe_identity
- id: DCCONF-SCHEMA-CASE-024
  title: service import with unknown service id is rejected as schema
  expect:
    portable:
      status: fail
      category: schema
  clauses:
    imports:
    - service:
        id: svc.unknown
        names:
        - pipe_identity
    predicates:
    - id: assert_1
      assert:
        lit: true
- id: DCCONF-SCHEMA-CASE-025
  title: binding service is effective-required after defaults merge
  expect:
    portable:
      status: fail
      category: schema
  bindings:
    defaults:
      import: pipe_identity
      mode: merge
    rows:
    - id: bind_schema_case_025_missing_service
      outputs:
      - to: schema_ref_export
        as: piped_text
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
- id: DCCONF-SCHEMA-CASE-026
  title: undeclared artifact symbol import is rejected as schema
  expect:
    portable:
      status: fail
      category: schema
  clauses:
    imports:
    - artifact:
      - undeclared_symbol
    predicates:
    - id: assert_1
      assert:
        lit: true
- id: DCCONF-SCHEMA-CASE-037
  title: compact binding outputs are accepted
  expect:
    portable:
      status: pass
      category:
  bindings:
    defaults:
      import: pipe_identity
      mode: merge
    rows:
    - id: bind_schema_case_037
      service: svc.check.default.1
      outputs:
      - schema_ref_export
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
- id: DCCONF-SCHEMA-CASE-038
  title: compact binding inputs are accepted
  expect:
    portable:
      status: pass
      category:
  bindings:
    defaults:
      import: pipe_identity
      mode: merge
    rows:
    - id: bind_schema_case_038
      service: svc.check.default.1
      inputs:
      - schema_ref_doc
      outputs:
      - schema_ref_export
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
- id: DCCONF-SCHEMA-CASE-039
  title: mixed compact and mapping binding output rows are rejected
  expect:
    portable:
      status: fail
      category: schema
  bindings:
    defaults:
      import: pipe_identity
      mode: merge
    rows:
    - id: bind_schema_case_039
      service: svc.check.default.1
      outputs:
      - schema_ref_export
      - to: schema_ref_export
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
- id: DCCONF-SCHEMA-CASE-040
  title: empty compact binding output row is rejected
  expect:
    portable:
      status: fail
      category: schema
  bindings:
    defaults:
      import: pipe_identity
      mode: merge
    rows:
    - id: bind_schema_case_040
      service: svc.check.default.1
      outputs:
      - " "
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
- id: DCCONF-SCHEMA-CASE-041
  title: duplicate compact binding output rows are rejected
  expect:
    portable:
      status: fail
      category: schema
  bindings:
    defaults:
      import: pipe_identity
      mode: merge
    rows:
    - id: bind_schema_case_041
      service: svc.check.default.1
      outputs:
      - schema_ref_export
      - schema_ref_export
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
artifacts:
- id: schema_ref_doc
  ref: "{{schema_ref}}"
  type: application/yaml
  docs:
  - summary: schema reference import
    audience: spec-authors
    status: active
  io: input
- id: schema_ref_export
  ref: "{{schema_ref}}"
  type: application/json
  docs:
  - summary: schema reference export
    audience: spec-authors
    status: active
  io: output
- id: text
  ref: "{{schema_ref}}"
  type: text/plain
  docs:
  - summary: schema text export
    audience: spec-authors
    status: active
  io: output
```
