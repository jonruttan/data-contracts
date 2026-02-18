# Spec-Lang Conformance Assertion Helpers

## LIB-CONF-ASSERT-001

```yaml contract-spec
id: LIB-CONF-ASSERT-001
title: reusable conformance assertion helper functions
type: contract.export
contract:
- id: __export__conf.pass_when_text_contains
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          std.string.contains:
          - {var: subject}
          - {var: token}
- id: __export__conf.pass_when_text_regex
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          std.string.regex_match:
          - {var: subject}
          - {var: pattern}
- id: __export__conf.eq
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          std.logic.eq:
          - {var: subject}
          - {var: value}
- id: __export__conf.has_error_category
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          std.string.contains:
          - {var: subject}
          - {var: category}
- id: __export__conf.json_type_is
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          std.type.json_type:
          - {var: subject}
          - {var: type_name}
harness:
  exports:
  - as: conf.pass_when_text_contains
    from: assert.function
    path: /__export__conf.pass_when_text_contains
    params:
    - subject
    - token
    required: true
  - as: conf.pass_when_text_regex
    from: assert.function
    path: /__export__conf.pass_when_text_regex
    params:
    - subject
    - pattern
    required: true
  - as: conf.eq
    from: assert.function
    path: /__export__conf.eq
    params:
    - subject
    - value
    required: true
  - as: conf.has_error_category
    from: assert.function
    path: /__export__conf.has_error_category
    params:
    - subject
    - category
    required: true
  - as: conf.json_type_is
    from: assert.function
    path: /__export__conf.json_type_is
    params:
    - subject
    - type_name
    required: true
```
