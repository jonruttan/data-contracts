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
    - {eq: [{add: [2, 3]}, 5]}
    - {eq: [{sub: [9, 4]}, 5]}
    - {eq: [{add: [1, 1]}, 2]}
    - {eq: [{sub: [3, 3]}, 0]}
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
    - eq:
      - {json_type: [{json_parse: ['{"a":1,"b":2}']}, dict]}
      - true
    - eq:
      - {has_key: [{json_parse: ['{"a":{"b":1}}']}, a]}
      - true
    - eq:
      - json_type:
        - {get: [{json_parse: ['{"a":{"b":1}}']}, a]}
        - dict
      - true
```
