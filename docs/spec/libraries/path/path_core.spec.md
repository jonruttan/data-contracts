# Spec-Lang Path Core Library

## LIB-PATH-001

```yaml spec-test
id: LIB-PATH-001-001-PATH-NORMALIZE-SLASHES
title: 'path-core reusable pure path logic helpers: path.normalize_slashes'
type: spec.export
assert:
- id: __export__path.normalize_slashes
  class: must
  checks:
  - std.string.replace:
    - var: path
    - \
    - /
- id: __export__path.trim_dot
  class: must
  checks:
  - std.string.replace:
    - var: path
    - ./
    - ''
- id: __export__path.dirname
  class: must
  checks:
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
  class: must
  checks:
  - std.logic.eq:
    - call:
      - var: path.extension
      - var: path
    - var: ext
- id: __export__path.is_under
  class: must
  checks:
  - std.string.starts_with:
    - call:
      - var: path.normalize_slashes
      - var: path
    - call:
      - var: path.normalize_slashes
      - var: prefix
- id: __export__path.matches
  class: must
  checks:
  - std.string.regex_match:
    - call:
      - var: path.normalize_slashes
      - var: path
    - var: pattern
harness:
  chain:
    exports:
    - as: path.normalize_slashes
      from: assert.function
      path: /__export__path.normalize_slashes
      params:
      - path
      required: true
    - as: path.trim_dot
      from: assert.function
      path: /__export__path.trim_dot
      params:
      - path
      required: true
    - as: path.dirname
      from: assert.function
      path: /__export__path.dirname
      params:
      - path
      required: true
    - as: path.has_extension
      from: assert.function
      path: /__export__path.has_extension
      params:
      - path
      - ext
      required: true
    - as: path.is_under
      from: assert.function
      path: /__export__path.is_under
      params:
      - path
      - prefix
      required: true
    - as: path.matches
      from: assert.function
      path: /__export__path.matches
      params:
      - path
      - pattern
      required: true
```

```yaml spec-test
id: LIB-PATH-001-002-PATH-SEGMENTS
title: 'path-core reusable pure path logic helpers: path.segments'
type: spec.export
assert:
- id: __export__path.segments
  class: must
  checks:
  - std.string.split:
    - call:
      - var: path.normalize_slashes
      - var: path
    - /
- id: __export__path.trim_dot
  class: must
  checks:
  - std.string.replace:
    - var: path
    - ./
    - ''
- id: __export__path.dirname
  class: must
  checks:
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
  class: must
  checks:
  - std.logic.eq:
    - call:
      - var: path.extension
      - var: path
    - var: ext
- id: __export__path.is_under
  class: must
  checks:
  - std.string.starts_with:
    - call:
      - var: path.normalize_slashes
      - var: path
    - call:
      - var: path.normalize_slashes
      - var: prefix
- id: __export__path.matches
  class: must
  checks:
  - std.string.regex_match:
    - call:
      - var: path.normalize_slashes
      - var: path
    - var: pattern
harness:
  chain:
    exports:
    - as: path.segments
      from: assert.function
      path: /__export__path.segments
      params:
      - path
      required: true
    - as: path.trim_dot
      from: assert.function
      path: /__export__path.trim_dot
      params:
      - path
      required: true
    - as: path.dirname
      from: assert.function
      path: /__export__path.dirname
      params:
      - path
      required: true
    - as: path.has_extension
      from: assert.function
      path: /__export__path.has_extension
      params:
      - path
      - ext
      required: true
    - as: path.is_under
      from: assert.function
      path: /__export__path.is_under
      params:
      - path
      - prefix
      required: true
    - as: path.matches
      from: assert.function
      path: /__export__path.matches
      params:
      - path
      - pattern
      required: true
```

```yaml spec-test
id: LIB-PATH-001-003-PATH-BASENAME
title: 'path-core reusable pure path logic helpers: path.basename'
type: spec.export
assert:
- id: __export__path.basename
  class: must
  checks:
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
  class: must
  checks:
  - std.string.replace:
    - var: path
    - ./
    - ''
- id: __export__path.dirname
  class: must
  checks:
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
  class: must
  checks:
  - std.logic.eq:
    - call:
      - var: path.extension
      - var: path
    - var: ext
- id: __export__path.is_under
  class: must
  checks:
  - std.string.starts_with:
    - call:
      - var: path.normalize_slashes
      - var: path
    - call:
      - var: path.normalize_slashes
      - var: prefix
- id: __export__path.matches
  class: must
  checks:
  - std.string.regex_match:
    - call:
      - var: path.normalize_slashes
      - var: path
    - var: pattern
harness:
  chain:
    exports:
    - as: path.basename
      from: assert.function
      path: /__export__path.basename
      params:
      - path
      required: true
    - as: path.trim_dot
      from: assert.function
      path: /__export__path.trim_dot
      params:
      - path
      required: true
    - as: path.dirname
      from: assert.function
      path: /__export__path.dirname
      params:
      - path
      required: true
    - as: path.has_extension
      from: assert.function
      path: /__export__path.has_extension
      params:
      - path
      - ext
      required: true
    - as: path.is_under
      from: assert.function
      path: /__export__path.is_under
      params:
      - path
      - prefix
      required: true
    - as: path.matches
      from: assert.function
      path: /__export__path.matches
      params:
      - path
      - pattern
      required: true
```

```yaml spec-test
id: LIB-PATH-001-004-PATH-EXTENSION
title: 'path-core reusable pure path logic helpers: path.extension'
type: spec.export
assert:
- id: __export__path.extension
  class: must
  checks:
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
  class: must
  checks:
  - std.string.replace:
    - var: path
    - ./
    - ''
- id: __export__path.dirname
  class: must
  checks:
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
  class: must
  checks:
  - std.logic.eq:
    - call:
      - var: path.extension
      - var: path
    - var: ext
- id: __export__path.is_under
  class: must
  checks:
  - std.string.starts_with:
    - call:
      - var: path.normalize_slashes
      - var: path
    - call:
      - var: path.normalize_slashes
      - var: prefix
- id: __export__path.matches
  class: must
  checks:
  - std.string.regex_match:
    - call:
      - var: path.normalize_slashes
      - var: path
    - var: pattern
harness:
  chain:
    exports:
    - as: path.extension
      from: assert.function
      path: /__export__path.extension
      params:
      - path
      required: true
    - as: path.trim_dot
      from: assert.function
      path: /__export__path.trim_dot
      params:
      - path
      required: true
    - as: path.dirname
      from: assert.function
      path: /__export__path.dirname
      params:
      - path
      required: true
    - as: path.has_extension
      from: assert.function
      path: /__export__path.has_extension
      params:
      - path
      - ext
      required: true
    - as: path.is_under
      from: assert.function
      path: /__export__path.is_under
      params:
      - path
      - prefix
      required: true
    - as: path.matches
      from: assert.function
      path: /__export__path.matches
      params:
      - path
      - pattern
      required: true
```

```yaml spec-test
id: LIB-PATH-001-900-PATH-SMOKE
title: path core helpers execute as colocated executable checks
type: text.file
harness:
  chain:
    steps:
    - id: lib_path_normalize
      class: must
      ref: '#LIB-PATH-001-001-PATH-NORMALIZE-SLASHES'
    imports:
    - from: lib_path_normalize
      names:
      - path.normalize_slashes
assert:
- id: assert_1
  class: must
  checks:
  - std.logic.eq:
    - call:
      - var: path.normalize_slashes
      - a\\b\\c.txt
    - a/b/c.txt
  target: text
```
