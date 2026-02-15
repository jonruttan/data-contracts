# Spec-Lang Path Core Library

## LIB-PATH-001

```yaml spec-test
id: LIB-PATH-001
title: path-core reusable pure path logic helpers
type: spec_lang.library
functions:
  public:
    path.normalize_slashes:
      fn:
      - [path]
      - {replace: [{var: path}, \, /]}
    path.segments:
      fn:
      - [path]
      - split:
        - {call: [{var: path.normalize_slashes}, {var: path}]}
        - /
    path.basename:
      fn:
      - [path]
      - let:
        - {lit: [[segs, {call: [{var: path.segments}, {var: path}]}]]}
        - if:
          - {is_empty: [{var: segs}]}
          - ''
          - get:
            - {var: segs}
            - sub:
              - {len: [{var: segs}]}
              - 1
    path.extension:
      fn:
      - [path]
      - let:
        - {lit: [[base, {call: [{var: path.basename}, {var: path}]}]]}
        - let:
          - {lit: [[parts, {split: [{var: base}, .]}]]}
          - if:
            - lte:
              - {len: [{var: parts}]}
              - 1
            - ''
            - get:
              - {var: parts}
              - sub:
                - {len: [{var: parts}]}
                - 1
  private:
    path.trim_dot:
      fn:
      - [path]
      - {replace: [{var: path}, ./, '']}
    path.dirname:
      fn:
      - [path]
      - let:
        - {lit: [[segs, {call: [{var: path.segments}, {var: path}]}]]}
        - if:
          - lte:
            - {len: [{var: segs}]}
            - 1
          - ''
          - join:
            - slice:
              - 0
              - sub:
                - {len: [{var: segs}]}
                - 1
              - {var: segs}
            - /
    path.has_extension:
      fn:
      - [path, ext]
      - eq:
        - {call: [{var: path.extension}, {var: path}]}
        - {var: ext}
    path.is_under:
      fn:
      - [path, prefix]
      - starts_with:
        - {call: [{var: path.normalize_slashes}, {var: path}]}
        - {call: [{var: path.normalize_slashes}, {var: prefix}]}
    path.matches:
      fn:
      - [path, pattern]
      - regex_match:
        - {call: [{var: path.normalize_slashes}, {var: path}]}
        - {var: pattern}
```
