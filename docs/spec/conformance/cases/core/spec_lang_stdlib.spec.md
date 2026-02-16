# Conformance Cases

## SRCONF-STDLIB-001

```yaml spec-test
id: SRCONF-STDLIB-001
title: core numeric and set operators evaluate deterministically
purpose: Validates representative numeric operators in the stdlib profile.
type: text.file
path: /docs/spec/conformance/cases/core/spec_lang_stdlib.spec.md
expect:
  portable:
    status: pass
assert:
- target: text
  must:
  - evaluate:
    - std.logic.eq:
      - std.math.add:
        - 2
        - 3
      - 5
    - std.logic.eq:
      - std.math.sub:
        - 9
        - 4
      - 5
    - std.logic.eq:
      - std.math.add:
        - 1
        - 1
      - 2
    - std.logic.eq:
      - std.math.sub:
        - 3
        - 3
      - 0
```

## SRCONF-STDLIB-002

```yaml spec-test
id: SRCONF-STDLIB-002
title: core collection and object operators evaluate deterministically
purpose: Validates representative object and json operators in the stdlib profile.
type: text.file
path: /docs/spec/conformance/cases/core/spec_lang_stdlib.spec.md
expect:
  portable:
    status: pass
assert:
- target: text
  must:
  - evaluate:
    - std.logic.eq:
      - std.type.json_type:
        - std.json.parse:
          - '{"a":1,"b":2}'
        - dict
      - true
    - std.logic.eq:
      - std.object.has_key:
        - std.json.parse:
          - '{"a":{"b":1}}'
        - a
      - true
    - std.logic.eq:
      - std.type.json_type:
        - std.object.get:
          - std.json.parse:
            - '{"a":{"b":1}}'
          - a
        - dict
      - true
```
