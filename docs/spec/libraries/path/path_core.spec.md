# Spec-Lang Path Core Library

## LIB-PATH-001

```yaml spec-test
id: LIB-PATH-001-001-PATH-NORMALIZE-SLASHES
title: 'path-core reusable pure path logic helpers: path.normalize_slashes'
type: spec_lang.export
defines:
  public:
    path.normalize_slashes:
      fn:
      - [path]
      - std.string.replace:
        - {var: path}
        - \
        - /
  private:
    path.trim_dot:
      fn:
      - [path]
      - std.string.replace:
        - {var: path}
        - ./
        - ''
    path.dirname:
      fn:
      - [path]
      - let:
        - lit:
          - - segs
            - call:
              - {var: path.segments}
              - {var: path}
        - if:
          - std.logic.lte:
            - std.collection.len:
              - {var: segs}
            - 1
          - ''
          - std.string.join:
            - std.collection.slice:
              - 0
              - std.math.sub:
                - std.collection.len:
                  - {var: segs}
                - 1
              - {var: segs}
            - /
    path.has_extension:
      fn:
      - [path, ext]
      - std.logic.eq:
        - call:
          - {var: path.extension}
          - {var: path}
        - {var: ext}
    path.is_under:
      fn:
      - [path, prefix]
      - std.string.starts_with:
        - call:
          - {var: path.normalize_slashes}
          - {var: path}
        - call:
          - {var: path.normalize_slashes}
          - {var: prefix}
    path.matches:
      fn:
      - [path, pattern]
      - std.string.regex_match:
        - call:
          - {var: path.normalize_slashes}
          - {var: path}
        - {var: pattern}
```

```yaml spec-test
id: LIB-PATH-001-002-PATH-SEGMENTS
title: 'path-core reusable pure path logic helpers: path.segments'
type: spec_lang.export
defines:
  public:
    path.segments:
      fn:
      - [path]
      - std.string.split:
        - call:
          - {var: path.normalize_slashes}
          - {var: path}
        - /
  private:
    path.trim_dot:
      fn:
      - [path]
      - std.string.replace:
        - {var: path}
        - ./
        - ''
    path.dirname:
      fn:
      - [path]
      - let:
        - lit:
          - - segs
            - call:
              - {var: path.segments}
              - {var: path}
        - if:
          - std.logic.lte:
            - std.collection.len:
              - {var: segs}
            - 1
          - ''
          - std.string.join:
            - std.collection.slice:
              - 0
              - std.math.sub:
                - std.collection.len:
                  - {var: segs}
                - 1
              - {var: segs}
            - /
    path.has_extension:
      fn:
      - [path, ext]
      - std.logic.eq:
        - call:
          - {var: path.extension}
          - {var: path}
        - {var: ext}
    path.is_under:
      fn:
      - [path, prefix]
      - std.string.starts_with:
        - call:
          - {var: path.normalize_slashes}
          - {var: path}
        - call:
          - {var: path.normalize_slashes}
          - {var: prefix}
    path.matches:
      fn:
      - [path, pattern]
      - std.string.regex_match:
        - call:
          - {var: path.normalize_slashes}
          - {var: path}
        - {var: pattern}
```

```yaml spec-test
id: LIB-PATH-001-003-PATH-BASENAME
title: 'path-core reusable pure path logic helpers: path.basename'
type: spec_lang.export
defines:
  public:
    path.basename:
      fn:
      - [path]
      - let:
        - lit:
          - - segs
            - call:
              - {var: path.segments}
              - {var: path}
        - if:
          - std.collection.is_empty:
            - {var: segs}
          - ''
          - std.object.get:
            - {var: segs}
            - std.math.sub:
              - std.collection.len:
                - {var: segs}
              - 1
  private:
    path.trim_dot:
      fn:
      - [path]
      - std.string.replace:
        - {var: path}
        - ./
        - ''
    path.dirname:
      fn:
      - [path]
      - let:
        - lit:
          - - segs
            - call:
              - {var: path.segments}
              - {var: path}
        - if:
          - std.logic.lte:
            - std.collection.len:
              - {var: segs}
            - 1
          - ''
          - std.string.join:
            - std.collection.slice:
              - 0
              - std.math.sub:
                - std.collection.len:
                  - {var: segs}
                - 1
              - {var: segs}
            - /
    path.has_extension:
      fn:
      - [path, ext]
      - std.logic.eq:
        - call:
          - {var: path.extension}
          - {var: path}
        - {var: ext}
    path.is_under:
      fn:
      - [path, prefix]
      - std.string.starts_with:
        - call:
          - {var: path.normalize_slashes}
          - {var: path}
        - call:
          - {var: path.normalize_slashes}
          - {var: prefix}
    path.matches:
      fn:
      - [path, pattern]
      - std.string.regex_match:
        - call:
          - {var: path.normalize_slashes}
          - {var: path}
        - {var: pattern}
```

```yaml spec-test
id: LIB-PATH-001-004-PATH-EXTENSION
title: 'path-core reusable pure path logic helpers: path.extension'
type: spec_lang.export
defines:
  public:
    path.extension:
      fn:
      - [path]
      - let:
        - lit:
          - - base
            - call:
              - {var: path.basename}
              - {var: path}
        - let:
          - lit:
            - - parts
              - split:
                - {var: base}
                - .
          - if:
            - std.logic.lte:
              - std.collection.len:
                - {var: parts}
              - 1
            - ''
            - std.object.get:
              - {var: parts}
              - std.math.sub:
                - std.collection.len:
                  - {var: parts}
                - 1
  private:
    path.trim_dot:
      fn:
      - [path]
      - std.string.replace:
        - {var: path}
        - ./
        - ''
    path.dirname:
      fn:
      - [path]
      - let:
        - lit:
          - - segs
            - call:
              - {var: path.segments}
              - {var: path}
        - if:
          - std.logic.lte:
            - std.collection.len:
              - {var: segs}
            - 1
          - ''
          - std.string.join:
            - std.collection.slice:
              - 0
              - std.math.sub:
                - std.collection.len:
                  - {var: segs}
                - 1
              - {var: segs}
            - /
    path.has_extension:
      fn:
      - [path, ext]
      - std.logic.eq:
        - call:
          - {var: path.extension}
          - {var: path}
        - {var: ext}
    path.is_under:
      fn:
      - [path, prefix]
      - std.string.starts_with:
        - call:
          - {var: path.normalize_slashes}
          - {var: path}
        - call:
          - {var: path.normalize_slashes}
          - {var: prefix}
    path.matches:
      fn:
      - [path, pattern]
      - std.string.regex_match:
        - call:
          - {var: path.normalize_slashes}
          - {var: path}
        - {var: pattern}
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
