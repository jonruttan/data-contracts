```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
services:
  actions:
  - id: svc.check.compact.1
    type: io.fs
    io: input
    profile: read.text
    imports:
    - pipe_identity
contracts:
- id: DCCONF-SCHEMA-CASE-027
  title: service imports compact single-name list is accepted
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
  - id: svc.check.compact.6
    type: io.fs
    io: input
    profile: read.text
    imports:
    - pipe_identity
contracts:
- id: DCCONF-SCHEMA-CASE-032
  title: clause imports bare-string short alias is accepted
  expect:
    portable:
      status: pass
      category:
  bindings:
    defaults:
      service: svc.check.compact.6
  clauses:
    imports:
    - pipe_identity
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
  - id: svc.check.compact.7
    type: io.fs
    io: input
    profile: read.text
    imports:
    - pipe_identity
contracts:
- id: DCCONF-SCHEMA-CASE-033
  title: predicate imports bare-string short alias is accepted
  expect:
    portable:
      status: pass
      category:
  bindings:
    defaults:
      service: svc.check.compact.7
  clauses:
    predicates:
    - id: assert_1
      imports:
      - pipe_identity
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
  - id: svc.check.compact.8
    type: io.fs
    io: input
    profile: read.text
    imports:
    - pipe_identity
contracts:
- id: DCCONF-SCHEMA-CASE-034
  title: clause short alias without bindings defaults service is rejected
  expect:
    portable:
      status: fail
      category: schema
  clauses:
    imports:
    - pipe_identity
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
  - id: svc.check.compact.9
    type: io.fs
    io: input
    profile: read.text
    imports:
    - pipe_identity
contracts:
- id: DCCONF-SCHEMA-CASE-035
  title: clause short alias with unknown default service is rejected
  expect:
    portable:
      status: fail
      category: schema
  bindings:
    defaults:
      service: svc.check.missing
  clauses:
    imports:
    - pipe_identity
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
  - id: svc.check.compact.10
    type: io.fs
    io: input
    profile: read.text
    imports:
    - pipe_identity
contracts:
- id: DCCONF-SCHEMA-CASE-036
  title: clause short alias unknown import name is rejected
  expect:
    portable:
      status: fail
      category: schema
  bindings:
    defaults:
      service: svc.check.compact.10
  clauses:
    imports:
    - unknown_import
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
  - id: svc.check.compact.2
    type: io.fs
    io: input
    profile: read.text
    imports:
    - pipe_identity
    - assert_truth
contracts:
- id: DCCONF-SCHEMA-CASE-028
  title: service imports compact multi-name list is accepted
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
  - id: svc.check.compact.3
    type: io.fs
    io: input
    profile: read.text
    imports:
    - pipe_identity
    - names:
      - assert_truth
contracts:
- id: DCCONF-SCHEMA-CASE-029
  title: service imports mixed compact and mapping item kinds are rejected
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
  actions:
  - id: svc.check.compact.4
    type: io.fs
    io: input
    profile: read.text
    imports:
    - pipe_identity
    - pipe_identity
contracts:
- id: DCCONF-SCHEMA-CASE-030
  title: service imports compact duplicate names are rejected
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
  actions:
  - id: svc.check.compact.5
    type: io.fs
    io: input
    profile: read.text
    imports:
    - unknown_import
contracts:
- id: DCCONF-SCHEMA-CASE-031
  title: service imports compact unknown catalog name is rejected
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
