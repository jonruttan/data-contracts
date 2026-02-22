```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
title: schema alias registry harmonization
harness:
  type: unit.test
  profile: check
services:
  actions:
  - id: svc.alias.harmonize.1
    type: io.fs
    io: input
    profile: read.text
    imports:
    - pipe_identity
    - assert_truth
contracts:
- id: DCCONF-SCHEMA-ALIAS-001
  title: services imports compact aliases remain valid via alias registry
  expect:
    portable:
      status: pass
      category:
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
- id: DCCONF-SCHEMA-ALIAS-002
  title: clause imports support canonical and compact aliases together
  expect:
    portable:
      status: pass
      category:
  bindings:
    defaults:
      service: svc.alias.harmonize.1
      import: pipe_identity
      mode: merge
  clauses:
    imports:
    - pipe_identity
    - service:
        id: svc.alias.harmonize.1
        names:
        - assert_truth
    - from: service
      service: svc.alias.harmonize.1
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
- id: DCCONF-SCHEMA-ALIAS-003
  title: effective-required binding import missing after merge is rejected
  expect:
    portable:
      status: fail
      category: schema
  bindings:
    defaults:
      service: svc.alias.harmonize.1
      mode: merge
    rows:
    - id: bind_alias_missing_import
      outputs:
      - to: alias_output
        as: subject
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
artifacts:
- id: alias_output
  ref: "/specs/schema/schema_v2.md"
  io: output
```
