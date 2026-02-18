# Spec-Lang Path Core Library

## LIB-PATH-001

```yaml contract-spec
id: LIB-PATH-001-001-PATH-NORMALIZE-SLASHES
type: spec.export
contract:
- id: __export__path.normalize_slashes
  class: MUST
  asserts:
  - std.string.replace:
    - var: path
    - \
    - /
- id: __export__path.trim_dot
  class: MUST
  asserts:
  - std.string.replace:
    - var: path
    - ./
    - ''
- id: __export__path.dirname
  class: MUST
  asserts:
  - let:
    - lit:
      - - segs
        - call:
          - var: path.segments
          - var: path
    - if:
      - std.logic.lte:
        - std.collection.len:
          - var: segs
        - 1
      - ''
      - std.string.join:
        - std.collection.slice:
          - 0
          - std.math.sub:
            - std.collection.len:
              - var: segs
            - 1
          - var: segs
        - /
- id: __export__path.has_extension
  class: MUST
  asserts:
  - std.logic.eq:
    - call:
      - var: path.extension
      - var: path
    - var: ext
- id: __export__path.is_under
  class: MUST
  asserts:
  - std.string.starts_with:
    - call:
      - var: path.normalize_slashes
      - var: path
    - call:
      - var: path.normalize_slashes
      - var: prefix
- id: __export__path.matches
  class: MUST
  asserts:
  - std.string.regex_match:
    - call:
      - var: path.normalize_slashes
      - var: path
    - var: pattern
harness:
  exports:
  - as: path.normalize_slashes
    from: assert.function
    path: /__export__path.normalize_slashes
    params:
    - path
  - as: path.trim_dot
    from: assert.function
    path: /__export__path.trim_dot
    params:
    - path
  - as: path.dirname
    from: assert.function
    path: /__export__path.dirname
    params:
    - path
  - as: path.has_extension
    from: assert.function
    path: /__export__path.has_extension
    params:
    - path
    - ext
  - as: path.is_under
    from: assert.function
    path: /__export__path.is_under
    params:
    - path
    - prefix
  - as: path.matches
    from: assert.function
    path: /__export__path.matches
    params:
    - path
    - pattern
```

```yaml contract-spec
id: LIB-PATH-001-002-PATH-SEGMENTS
type: spec.export
contract:
- id: __export__path.segments
  class: MUST
  asserts:
  - std.string.split:
    - call:
      - var: path.normalize_slashes
      - var: path
    - /
- id: __export__path.trim_dot
  class: MUST
  asserts:
  - std.string.replace:
    - var: path
    - ./
    - ''
- id: __export__path.dirname
  class: MUST
  asserts:
  - let:
    - lit:
      - - segs
        - call:
          - var: path.segments
          - var: path
    - if:
      - std.logic.lte:
        - std.collection.len:
          - var: segs
        - 1
      - ''
      - std.string.join:
        - std.collection.slice:
          - 0
          - std.math.sub:
            - std.collection.len:
              - var: segs
            - 1
          - var: segs
        - /
- id: __export__path.has_extension
  class: MUST
  asserts:
  - std.logic.eq:
    - call:
      - var: path.extension
      - var: path
    - var: ext
- id: __export__path.is_under
  class: MUST
  asserts:
  - std.string.starts_with:
    - call:
      - var: path.normalize_slashes
      - var: path
    - call:
      - var: path.normalize_slashes
      - var: prefix
- id: __export__path.matches
  class: MUST
  asserts:
  - std.string.regex_match:
    - call:
      - var: path.normalize_slashes
      - var: path
    - var: pattern
harness:
  exports:
  - as: path.segments
    from: assert.function
    path: /__export__path.segments
    params:
    - path
  - as: path.trim_dot
    from: assert.function
    path: /__export__path.trim_dot
    params:
    - path
  - as: path.dirname
    from: assert.function
    path: /__export__path.dirname
    params:
    - path
  - as: path.has_extension
    from: assert.function
    path: /__export__path.has_extension
    params:
    - path
    - ext
  - as: path.is_under
    from: assert.function
    path: /__export__path.is_under
    params:
    - path
    - prefix
  - as: path.matches
    from: assert.function
    path: /__export__path.matches
    params:
    - path
    - pattern
```

```yaml contract-spec
id: LIB-PATH-001-003-PATH-BASENAME
type: spec.export
contract:
- id: __export__path.basename
  class: MUST
  asserts:
  - let:
    - lit:
      - - segs
        - call:
          - var: path.segments
          - var: path
    - if:
      - std.collection.is_empty:
        - var: segs
      - ''
      - std.object.get:
        - var: segs
        - std.math.sub:
          - std.collection.len:
            - var: segs
          - 1
- id: __export__path.trim_dot
  class: MUST
  asserts:
  - std.string.replace:
    - var: path
    - ./
    - ''
- id: __export__path.dirname
  class: MUST
  asserts:
  - let:
    - lit:
      - - segs
        - call:
          - var: path.segments
          - var: path
    - if:
      - std.logic.lte:
        - std.collection.len:
          - var: segs
        - 1
      - ''
      - std.string.join:
        - std.collection.slice:
          - 0
          - std.math.sub:
            - std.collection.len:
              - var: segs
            - 1
          - var: segs
        - /
- id: __export__path.has_extension
  class: MUST
  asserts:
  - std.logic.eq:
    - call:
      - var: path.extension
      - var: path
    - var: ext
- id: __export__path.is_under
  class: MUST
  asserts:
  - std.string.starts_with:
    - call:
      - var: path.normalize_slashes
      - var: path
    - call:
      - var: path.normalize_slashes
      - var: prefix
- id: __export__path.matches
  class: MUST
  asserts:
  - std.string.regex_match:
    - call:
      - var: path.normalize_slashes
      - var: path
    - var: pattern
harness:
  exports:
  - as: path.basename
    from: assert.function
    path: /__export__path.basename
    params:
    - path
  - as: path.trim_dot
    from: assert.function
    path: /__export__path.trim_dot
    params:
    - path
  - as: path.dirname
    from: assert.function
    path: /__export__path.dirname
    params:
    - path
  - as: path.has_extension
    from: assert.function
    path: /__export__path.has_extension
    params:
    - path
    - ext
  - as: path.is_under
    from: assert.function
    path: /__export__path.is_under
    params:
    - path
    - prefix
  - as: path.matches
    from: assert.function
    path: /__export__path.matches
    params:
    - path
    - pattern
```

```yaml contract-spec
id: LIB-PATH-001-004-PATH-EXTENSION
type: spec.export
contract:
- id: __export__path.extension
  class: MUST
  asserts:
  - let:
    - lit:
      - - base
        - call:
          - var: path.basename
          - var: path
    - let:
      - lit:
        - - parts
          - split:
            - var: base
            - .
      - if:
        - std.logic.lte:
          - std.collection.len:
            - var: parts
          - 1
        - ''
        - std.object.get:
          - var: parts
          - std.math.sub:
            - std.collection.len:
              - var: parts
            - 1
- id: __export__path.trim_dot
  class: MUST
  asserts:
  - std.string.replace:
    - var: path
    - ./
    - ''
- id: __export__path.dirname
  class: MUST
  asserts:
  - let:
    - lit:
      - - segs
        - call:
          - var: path.segments
          - var: path
    - if:
      - std.logic.lte:
        - std.collection.len:
          - var: segs
        - 1
      - ''
      - std.string.join:
        - std.collection.slice:
          - 0
          - std.math.sub:
            - std.collection.len:
              - var: segs
            - 1
          - var: segs
        - /
- id: __export__path.has_extension
  class: MUST
  asserts:
  - std.logic.eq:
    - call:
      - var: path.extension
      - var: path
    - var: ext
- id: __export__path.is_under
  class: MUST
  asserts:
  - std.string.starts_with:
    - call:
      - var: path.normalize_slashes
      - var: path
    - call:
      - var: path.normalize_slashes
      - var: prefix
- id: __export__path.matches
  class: MUST
  asserts:
  - std.string.regex_match:
    - call:
      - var: path.normalize_slashes
      - var: path
    - var: pattern
harness:
  exports:
  - as: path.extension
    from: assert.function
    path: /__export__path.extension
    params:
    - path
  - as: path.trim_dot
    from: assert.function
    path: /__export__path.trim_dot
    params:
    - path
  - as: path.dirname
    from: assert.function
    path: /__export__path.dirname
    params:
    - path
  - as: path.has_extension
    from: assert.function
    path: /__export__path.has_extension
    params:
    - path
    - ext
  - as: path.is_under
    from: assert.function
    path: /__export__path.is_under
    params:
    - path
    - prefix
  - as: path.matches
    from: assert.function
    path: /__export__path.matches
    params:
    - path
    - pattern
```

```yaml contract-spec
id: LIB-PATH-001-900-PATH-SMOKE
type: text.file
harness:
  chain:
    steps:
    - id: lib_path_normalize
      class: MUST
      ref: '#LIB-PATH-001-001-PATH-NORMALIZE-SLASHES'
    imports:
    - from: lib_path_normalize
      names:
      - path.normalize_slashes
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - call:
      - var: path.normalize_slashes
      - a\\b\\c.txt
    - a/b/c.txt
  target: text
```
