```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
services:
  actions:
  - id: svc.default.1
contracts:
- id: DCCONF-IMPLICIT-ID-001
  title: omitted docs id remains valid metadata
  docs:
  - summary: contract docs id intentionally omitted
    audience: spec-authors
    status: active
  expect:
    portable:
      status: pass
      category:
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
```

```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  docs:
  - summary: harness docs owner id omitted
    audience: spec-authors
    status: active
    owners:
    - role: owner
services:
  actions:
  - id: svc.default.2
contracts:
- id: DCCONF-IMPLICIT-ID-002
  title: omitted docs owner id remains valid metadata
  expect:
    portable:
      status: pass
      category:
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
```

```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
services:
  actions:
  - id: svc.default.3
contracts:
- id: DCCONF-IMPLICIT-ID-003
  title: missing predicate id is schema failure
  expect:
    portable:
      status: fail
      category: schema
  clauses:
    predicates:
    - assert:
        lit: true
```

```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
services:
  actions:
  - id: svc.default.4
    imports:
    - pipe_identity
contracts:
- id: DCCONF-IMPLICIT-ID-004
  title: synthetic report label is invalid as reference identity
  expect:
    portable:
      status: fail
      category: schema
  bindings:
    defaults:
      service: svc.default.4
      import: pipe_identity
    rows:
    - id: bind.invalid.synthetic
      outputs:
      - to: out_json
  clauses:
    predicates:
    - id: assert_1
      assert:
        lit: true
artifacts:
- id: out_json
  ref: artifact://implicit_ids/out_json
  type: application/json
  io: output
```
