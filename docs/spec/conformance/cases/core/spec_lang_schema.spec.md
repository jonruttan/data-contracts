# Conformance Cases

## SRCONF-STDLIB-003

```yaml spec-test
id: SRCONF-STDLIB-003
title: json parsing and type predicates stay deterministic
purpose: Ensures parsed JSON shapes can be validated with deterministic type predicates.
type: text.file
path: /docs/spec/conformance/cases/core/spec_lang_schema.spec.md
expect:
  portable:
    status: pass
assert:
- target: text
  must:
  - evaluate:
    - eq:
      - {json_type: [{json_parse: ['{"id":1,"tags":["alpha","beta"]}']}, dict]}
      - true
    - eq:
      - json_type:
        - {get: [{json_parse: ['{"id":1,"tags":["alpha","beta"]}']}, tags]}
        - list
      - true
```

## SRCONF-STDLIB-004

```yaml spec-test
id: SRCONF-STDLIB-004
title: parsed payload predicates support deterministic error-shape checks
purpose: Ensures JSON payload predicate composition remains deterministic for invalid-value checks.
type: text.file
path: /docs/spec/conformance/cases/core/spec_lang_schema.spec.md
expect:
  portable:
    status: pass
assert:
- target: text
  must:
  - evaluate:
    - and:
      - eq:
        - json_type:
          - {get: [{json_parse: ['{"id":"x"}']}, id]}
          - string
        - true
      - not:
        - eq:
          - {get: [{json_parse: ['{"id":"x"}']}, id]}
          - 1
```
