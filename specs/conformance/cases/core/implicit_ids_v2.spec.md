```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
services:
  entries:
  - id: svc.default.1
contracts:
- id: DCCONF-IMPLICIT-ID-001
  title: missing predicate id normalizes to assert index
  expect:
    portable:
      status: pass
      category:
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
  entries:
  - id: svc.default.2
docs:
- summary: root docs id omitted
  audience: spec-authors
  status: active
contracts:
- id: DCCONF-IMPLICIT-ID-002
  title: missing docs id normalizes to doc index
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
  entries:
  - id: svc.default.3
contracts:
- id: DCCONF-IMPLICIT-ID-003
  title: missing docs owner id normalizes to owner index
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
  entries:
  - id: svc.default.4
docs:
- summary: first docs entry id omitted
  audience: spec-authors
  status: active
- id: doc_1
  summary: colliding explicit doc id
  audience: spec-authors
  status: active
contracts:
- id: DCCONF-IMPLICIT-ID-004
  title: explicit docs id collides with generated docs id
  expect:
    portable:
      status: fail
      category: schema
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
  - summary: owner collision fixture
    audience: spec-authors
    status: active
    owners:
    - role: owner
    - id: owner_1
      role: reviewer
services:
  entries:
  - id: svc.default.5
contracts:
- id: DCCONF-IMPLICIT-ID-005
  title: explicit owner id collides with generated owner id
  expect:
    portable:
      status: fail
      category: schema
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
  entries:
  - id: svc.default.6
contracts:
- title: contracts id remains required
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
  entries:
  - profile: text.file
contracts:
- id: DCCONF-IMPLICIT-ID-007
  title: services entries id remains required
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
  entries:
  - id: svc.default.8
artifact:
  imports:
  - ref: artifact://implicit/missing-import-id
  exports:
  - id: export_a
    ref: artifact://implicit/export-a
contracts:
- id: DCCONF-IMPLICIT-ID-008
  title: artifact import id remains required
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
  entries:
  - id: svc.default.9
artifact:
  imports:
  - id: import_a
    ref: artifact://implicit/import-a
  exports:
  - ref: artifact://implicit/missing-export-id
contracts:
- id: DCCONF-IMPLICIT-ID-009
  title: artifact export id remains required
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
  entries:
  - id: svc.default.10
bindings:
- contract: DCCONF-IMPLICIT-ID-010
  service: svc.default.10
  import: pipe_identity
contracts:
- id: DCCONF-IMPLICIT-ID-010
  title: bindings id remains required
  expect:
    portable:
      status: fail
      category: schema
  clauses:
    predicates:
    - assert:
        lit: true
```
