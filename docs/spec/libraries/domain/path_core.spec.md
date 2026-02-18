# Spec-Lang Path/File Domain Library

## LIB-DOMAIN-PATH-001

```yaml contract-spec
id: LIB-DOMAIN-PATH-001-001-DOMAIN-PATH-NORMALIZE
type: contract.export
contract:
- id: __export__domain.path.normalize
  class: MUST
  asserts:
  - ops.fs.path.normalize:
    - {var: path}
harness:
  exports:
  - as: domain.path.normalize
    from: assert.function
    path: /__export__domain.path.normalize
    params:
    - path
    required: true
```

```yaml contract-spec
id: LIB-DOMAIN-PATH-001-002-DOMAIN-PATH-EQ
type: contract.export
contract:
- id: __export__domain.path.eq
  class: MUST
  asserts:
  - std.logic.eq:
    - ops.fs.path.normalize:
      - {var: left}
    - ops.fs.path.normalize:
      - {var: right}
harness:
  exports:
  - as: domain.path.eq
    from: assert.function
    path: /__export__domain.path.eq
    params:
    - left
    - right
    required: true
```

```yaml contract-spec
id: LIB-DOMAIN-PATH-001-003-DOMAIN-PATH-IS-SPEC-MD
type: contract.export
contract:
- id: __export__domain.path.is_spec_md
  class: MUST
  asserts:
  - std.string.ends_with:
    - ops.fs.path.normalize:
      - {var: path}
    - .spec.md
harness:
  exports:
  - as: domain.path.is_spec_md
    from: assert.function
    path: /__export__domain.path.is_spec_md
    params:
    - path
    required: true
```

```yaml contract-spec
id: LIB-DOMAIN-PATH-001-004-DOMAIN-PATH-IS-IN-DOCS
type: contract.export
contract:
- id: __export__domain.path.is_in_docs
  class: MUST
  asserts:
  - ops.fs.path.within:
    - /docs
    - ops.fs.path.normalize:
      - {var: path}
harness:
  exports:
  - as: domain.path.is_in_docs
    from: assert.function
    path: /__export__domain.path.is_in_docs
    params:
    - path
    required: true
```

```yaml contract-spec
id: LIB-DOMAIN-PATH-001-005-DOMAIN-PATH-SORTED
type: contract.export
contract:
- id: __export__domain.path.sorted
  class: MUST
  asserts:
  - ops.fs.path.sort:
    - {var: paths}
harness:
  exports:
  - as: domain.path.sorted
    from: assert.function
    path: /__export__domain.path.sorted
    params:
    - paths
    required: true
```

```yaml contract-spec
id: LIB-DOMAIN-PATH-001-006-DOMAIN-FILE-IS-EXISTING-FILE
type: contract.export
contract:
- id: __export__domain.file.is_existing_file
  class: MUST
  asserts:
  - std.logic.and:
    - ops.fs.file.exists:
      - {var: meta}
    - ops.fs.file.is_file:
      - {var: meta}
harness:
  exports:
  - as: domain.file.is_existing_file
    from: assert.function
    path: /__export__domain.file.is_existing_file
    params:
    - meta
    required: true
```

```yaml contract-spec
id: LIB-DOMAIN-PATH-001-007-DOMAIN-FILE-IS-EXISTING-DIR
type: contract.export
contract:
- id: __export__domain.file.is_existing_dir
  class: MUST
  asserts:
  - std.logic.and:
    - ops.fs.file.exists:
      - {var: meta}
    - ops.fs.file.is_dir:
      - {var: meta}
harness:
  exports:
  - as: domain.file.is_existing_dir
    from: assert.function
    path: /__export__domain.file.is_existing_dir
    params:
    - meta
    required: true
```

```yaml contract-spec
id: LIB-DOMAIN-PATH-001-008-DOMAIN-FILE-HAS-EXT
type: contract.export
contract:
- id: __export__domain.file.has_ext
  class: MUST
  asserts:
  - ops.fs.path.has_ext:
    - ops.fs.file.path:
      - {var: meta}
    - {var: ext}
harness:
  exports:
  - as: domain.file.has_ext
    from: assert.function
    path: /__export__domain.file.has_ext
    params:
    - meta
    - ext
    required: true
```

```yaml contract-spec
id: LIB-DOMAIN-PATH-001-009-DOMAIN-FILE-NAME
type: contract.export
contract:
- id: __export__domain.file.name
  class: MUST
  asserts:
  - ops.fs.file.name:
    - {var: meta}
harness:
  exports:
  - as: domain.file.name
    from: assert.function
    path: /__export__domain.file.name
    params:
    - meta
    required: true
```
