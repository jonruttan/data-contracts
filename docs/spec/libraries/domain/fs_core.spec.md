# Spec-Lang Filesystem Utility Domain Library

## LIB-DOMAIN-FS-001

```yaml contract-spec
id: LIB-DOMAIN-FS-001-001-DOMAIN-FS-IS-DOCS-SPEC-FILE
type: spec.export
contract:
- id: __export__domain.fs.is_docs_spec_file
  class: must
  asserts:
  - std.logic.and:
    - ops.fs.path.within:
      - /docs
      - ops.fs.path.normalize:
        - var: path
    - std.string.ends_with:
      - ops.fs.path.normalize:
        - var: path
      - .spec.md
harness:
  chain:
    exports:
    - as: domain.fs.is_docs_spec_file
      from: assert.function
      path: /__export__domain.fs.is_docs_spec_file
      params:
      - path
      required: true
```

```yaml contract-spec
id: LIB-DOMAIN-FS-001-002-DOMAIN-FS-SORT-SPEC-FILES
type: spec.export
contract:
- id: __export__domain.fs.sort_spec_files
  class: must
  asserts:
  - ops.fs.path.sort:
    - ops.fs.glob.filter:
      - var: paths
      - '*.spec.md'
harness:
  chain:
    exports:
    - as: domain.fs.sort_spec_files
      from: assert.function
      path: /__export__domain.fs.sort_spec_files
      params:
      - paths
      required: true
```

```yaml contract-spec
id: LIB-DOMAIN-FS-001-003-DOMAIN-FS-JSON-GET-OR-TEXT
type: spec.export
contract:
- id: __export__domain.fs.json_get_or_text
  class: must
  asserts:
  - ops.fs.json.get_or:
    - ops.fs.json.parse:
      - var: json_text
    - var: path_segments
    - var: fallback
harness:
  chain:
    exports:
    - as: domain.fs.json_get_or_text
      from: assert.function
      path: /__export__domain.fs.json_get_or_text
      params:
      - json_text
      - path_segments
      - fallback
      required: true
```

```yaml contract-spec
id: LIB-DOMAIN-FS-001-004-DOMAIN-FS-JSON-HAS-PATH-TEXT
type: spec.export
contract:
- id: __export__domain.fs.json_has_path_text
  class: must
  asserts:
  - ops.fs.json.has_path:
    - ops.fs.json.parse:
      - var: json_text
    - var: path_segments
harness:
  chain:
    exports:
    - as: domain.fs.json_has_path_text
      from: assert.function
      path: /__export__domain.fs.json_has_path_text
      params:
      - json_text
      - path_segments
      required: true
```

```yaml contract-spec
id: LIB-DOMAIN-FS-001-005-DOMAIN-FS-GLOB-ANY-SPEC-FILES
type: spec.export
contract:
- id: __export__domain.fs.glob_any_spec_files
  class: must
  asserts:
  - ops.fs.glob.any:
    - var: paths
    - '*.spec.md'
harness:
  chain:
    exports:
    - as: domain.fs.glob_any_spec_files
      from: assert.function
      path: /__export__domain.fs.glob_any_spec_files
      params:
      - paths
      required: true
```

```yaml contract-spec
id: LIB-DOMAIN-FS-001-006-DOMAIN-FS-FILE-EXT-EQ
type: spec.export
contract:
- id: __export__domain.fs.file_ext_eq
  class: must
  asserts:
  - ops.fs.path.has_ext:
    - ops.fs.file.path:
      - var: meta
    - var: ext
harness:
  chain:
    exports:
    - as: domain.fs.file_ext_eq
      from: assert.function
      path: /__export__domain.fs.file_ext_eq
      params:
      - meta
      - ext
      required: true
```

```yaml contract-spec
id: LIB-DOMAIN-FS-001-007-DOMAIN-FS-JSON-GET-TEXT
type: spec.export
contract:
- id: __export__domain.fs.json_get_text
  class: must
  asserts:
  - ops.fs.json.get:
    - ops.fs.json.parse:
      - var: json_text
    - var: path_segments
harness:
  chain:
    exports:
    - as: domain.fs.json_get_text
      from: assert.function
      path: /__export__domain.fs.json_get_text
      params:
      - json_text
      - path_segments
      required: true
```

```yaml contract-spec
id: LIB-DOMAIN-FS-001-008-DOMAIN-FS-JSON-PATH-EQ-TEXT
type: spec.export
contract:
- id: __export__domain.fs.json_path_eq_text
  class: must
  asserts:
  - std.logic.eq:
    - call:
      - var: domain.fs.json_get_or_text
      - var: json_text
      - var: path_segments
      - null
    - var: expected
harness:
  chain:
    exports:
    - as: domain.fs.json_path_eq_text
      from: assert.function
      path: /__export__domain.fs.json_path_eq_text
      params:
      - json_text
      - path_segments
      - expected
      required: true
```

```yaml contract-spec
id: LIB-DOMAIN-FS-001-009-DOMAIN-FS-GLOB-FILTER
type: spec.export
contract:
- id: __export__domain.fs.glob_filter
  class: must
  asserts:
  - ops.fs.glob.filter:
    - var: paths
    - var: pattern
harness:
  chain:
    exports:
    - as: domain.fs.glob_filter
      from: assert.function
      path: /__export__domain.fs.glob_filter
      params:
      - paths
      - pattern
      required: true
```

```yaml contract-spec
id: LIB-DOMAIN-FS-001-010-DOMAIN-FS-GLOB-ALL
type: spec.export
contract:
- id: __export__domain.fs.glob_all
  class: must
  asserts:
  - ops.fs.glob.all:
    - var: paths
    - var: pattern
harness:
  chain:
    exports:
    - as: domain.fs.glob_all
      from: assert.function
      path: /__export__domain.fs.glob_all
      params:
      - paths
      - pattern
      required: true
```
