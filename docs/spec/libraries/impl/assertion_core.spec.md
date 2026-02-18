# Spec-Lang Impl Assertion Helpers

## LIB-IMPL-ASSERT-001

```yaml contract-spec
id: LIB-IMPL-ASSERT-001-001-IMPL-ASSERT-CONTAINS
title: 'reusable impl assertion helper functions: impl.assert.contains'
type: spec.export
contract:
- id: __export__impl.assert.contains
  class: MUST
  asserts:
  - std.string.contains:
    - var: subject
    - var: token
harness:
  exports:
  - as: impl.assert.contains
    from: assert.function
    path: /__export__impl.assert.contains
    params:
    - subject
    - token
    required: true
```

```yaml contract-spec
id: LIB-IMPL-ASSERT-001-002-IMPL-ASSERT-REGEX
title: 'reusable impl assertion helper functions: impl.assert.regex'
type: spec.export
contract:
- id: __export__impl.assert.regex
  class: MUST
  asserts:
  - std.string.regex_match:
    - var: subject
    - var: pattern
harness:
  exports:
  - as: impl.assert.regex
    from: assert.function
    path: /__export__impl.assert.regex
    params:
    - subject
    - pattern
    required: true
```

```yaml contract-spec
id: LIB-IMPL-ASSERT-001-003-IMPL-ASSERT-JSON-TYPE
title: 'reusable impl assertion helper functions: impl.assert.json_type'
type: spec.export
contract:
- id: __export__impl.assert.json_type
  class: MUST
  asserts:
  - std.type.json_type:
    - var: subject
    - var: type_name
harness:
  exports:
  - as: impl.assert.json_type
    from: assert.function
    path: /__export__impl.assert.json_type
    params:
    - subject
    - type_name
    required: true
```
