# Conformance Cases

## SRCONF-STDLIB-003

```yaml contract-spec
id: SRCONF-STDLIB-003
title: json parsing and type predicates stay deterministic
purpose: Ensures parsed JSON shapes can be validated with deterministic type predicates.
type: text.file
path: /docs/spec/conformance/cases/core/spec_lang_schema.spec.md
expect:
  portable:
    status: pass
contract:
- id: assert_1
  class: must
  asserts:
  - must:
    - std.logic.eq:
      - std.type.json_type:
        - std.json.parse:
          - '{"id":1,"tags":["alpha","beta"]}'
        - dict
      - true
    - std.logic.eq:
      - std.type.json_type:
        - std.object.get:
          - std.json.parse:
            - '{"id":1,"tags":["alpha","beta"]}'
          - tags
        - list
      - true
  target: text
```

## SRCONF-STDLIB-004

```yaml contract-spec
id: SRCONF-STDLIB-004
title: parsed payload predicates support deterministic error-shape checks
purpose: Ensures JSON payload predicate composition remains deterministic for invalid-value
  checks.
type: text.file
path: /docs/spec/conformance/cases/core/spec_lang_schema.spec.md
expect:
  portable:
    status: pass
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.and:
    - std.logic.eq:
      - std.type.json_type:
        - std.object.get:
          - std.json.parse:
            - '{"id":"x"}'
          - id
        - string
      - true
    - std.logic.not:
      - std.logic.eq:
        - std.object.get:
          - std.json.parse:
            - '{"id":"x"}'
          - id
        - 1
  target: text
```
