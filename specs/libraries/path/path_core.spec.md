# Spec-Lang Path Core Library

## LIB-PATH-001

```yaml contract-spec
id: LIB-PATH-001-001-PATH-NORMALIZE-SLASHES
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__path.normalize_slashes
    assert:
      std.string.replace:
      - {var: path}
      - \
      - /
  - id: __export__path.trim_dot
    assert:
      std.string.replace:
      - {var: path}
      - ./
      - ''
  - id: __export__path.dirname
    assert:
      lit:
        let:
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
    assert:
      std.logic.eq:
      - call:
        - {var: path.extension}
        - {var: path}
      - {var: ext}
  - id: __export__path.is_under
    assert:
      std.string.starts_with:
      - call:
        - {var: path.normalize_slashes}
        - {var: path}
      - call:
        - {var: path.normalize_slashes}
        - {var: prefix}
  - id: __export__path.matches
    assert:
      std.string.regex_match:
      - call:
        - {var: path.normalize_slashes}
        - {var: path}
      - {var: pattern}
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
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__path.segments
    assert:
      std.string.split:
      - call:
        - {var: path.normalize_slashes}
        - {var: path}
      - /
  - id: __export__path.trim_dot
    assert:
      std.string.replace:
      - {var: path}
      - ./
      - ''
  - id: __export__path.dirname
    assert:
      lit:
        let:
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
    assert:
      std.logic.eq:
      - call:
        - {var: path.extension}
        - {var: path}
      - {var: ext}
  - id: __export__path.is_under
    assert:
      std.string.starts_with:
      - call:
        - {var: path.normalize_slashes}
        - {var: path}
      - call:
        - {var: path.normalize_slashes}
        - {var: prefix}
  - id: __export__path.matches
    assert:
      std.string.regex_match:
      - call:
        - {var: path.normalize_slashes}
        - {var: path}
      - {var: pattern}
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
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__path.basename
    assert:
      lit:
        let:
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
    assert:
      std.string.replace:
      - {var: path}
      - ./
      - ''
  - id: __export__path.dirname
    assert:
      lit:
        let:
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
    assert:
      std.logic.eq:
      - call:
        - {var: path.extension}
        - {var: path}
      - {var: ext}
  - id: __export__path.is_under
    assert:
      std.string.starts_with:
      - call:
        - {var: path.normalize_slashes}
        - {var: path}
      - call:
        - {var: path.normalize_slashes}
        - {var: prefix}
  - id: __export__path.matches
    assert:
      std.string.regex_match:
      - call:
        - {var: path.normalize_slashes}
        - {var: path}
      - {var: pattern}
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
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__path.extension
    assert:
      lit:
        let:
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
    assert:
      std.string.replace:
      - {var: path}
      - ./
      - ''
  - id: __export__path.dirname
    assert:
      lit:
        let:
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
    assert:
      std.logic.eq:
      - call:
        - {var: path.extension}
        - {var: path}
      - {var: ext}
  - id: __export__path.is_under
    assert:
      std.string.starts_with:
      - call:
        - {var: path.normalize_slashes}
        - {var: path}
      - call:
        - {var: path.normalize_slashes}
        - {var: prefix}
  - id: __export__path.matches
    assert:
      std.string.regex_match:
      - call:
        - {var: path.normalize_slashes}
        - {var: path}
      - {var: pattern}
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
type: contract.check
harness:
  check:
    profile: text.file
    config: {}
  use:
  - ref: '#LIB-PATH-001-001-PATH-NORMALIZE-SLASHES'
    as: lib_path_normalize
    symbols:
    - path.normalize_slashes
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    'on': text
    assert:
      std.logic.eq:
      - call:
        - {var: path.normalize_slashes}
        - a\\b\\c.txt
      - a/b/c.txt
```
