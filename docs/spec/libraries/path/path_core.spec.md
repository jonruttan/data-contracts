# Spec-Lang Path Core Library

## LIB-PATH-001

```yaml spec-test
id: LIB-PATH-001
title: path-core reusable pure path logic helpers
type: spec_lang.library
definitions:
  public:
    path.normalize_slashes:
      fn:
      - [path]
      - std.string.replace:
        - {var: path}
        - \
        - /
    path.segments:
      fn:
      - [path]
      - std.string.split:
        - call:
          - {var: path.normalize_slashes}
          - {var: path}
        - /
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
