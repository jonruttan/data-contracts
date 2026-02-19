# Spec-Lang Impl Assertion Helpers

## LIB-IMPL-ASSERT-001

```yaml contract-spec
id: LIB-IMPL-ASSERT-001-001-IMPL-ASSERT-CONTAINS
title: 'reusable impl assertion helper functions: impl.assert.contains'
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__impl.assert.contains
    assert:
      std.string.contains:
      - {var: subject}
      - {var: token}
harness:
  exports:
  - as: impl.assert.contains
    from: assert.function
    path: /__export__impl.assert.contains
    params:
    - subject
    - token
    required: true
    doc:
      summary: Contract export for `impl.assert.contains`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      - name: token
        type: any
        required: true
        description: Input parameter `token`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          subject: <subject>
          token: <token>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: impl.assertion.core
  module: impl
  stability: alpha
  owner: spec_runner
  tags:
  - impl
doc:
  summary: Case `LIB-IMPL-ASSERT-001-001-IMPL-ASSERT-CONTAINS` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-IMPL-ASSERT-001-002-IMPL-ASSERT-REGEX
title: 'reusable impl assertion helper functions: impl.assert.regex'
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__impl.assert.regex
    assert:
      std.string.regex_match:
      - {var: subject}
      - {var: pattern}
harness:
  exports:
  - as: impl.assert.regex
    from: assert.function
    path: /__export__impl.assert.regex
    params:
    - subject
    - pattern
    required: true
    doc:
      summary: Contract export for `impl.assert.regex`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      - name: pattern
        type: any
        required: true
        description: Input parameter `pattern`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          subject: <subject>
          pattern: <pattern>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: impl.assertion.core
  module: impl
  stability: alpha
  owner: spec_runner
  tags:
  - impl
doc:
  summary: Case `LIB-IMPL-ASSERT-001-002-IMPL-ASSERT-REGEX` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-IMPL-ASSERT-001-003-IMPL-ASSERT-JSON-TYPE
title: 'reusable impl assertion helper functions: impl.assert.json_type'
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__impl.assert.json_type
    assert:
      std.type.json_type:
      - {var: subject}
      - {var: type_name}
harness:
  exports:
  - as: impl.assert.json_type
    from: assert.function
    path: /__export__impl.assert.json_type
    params:
    - subject
    - type_name
    required: true
    doc:
      summary: Contract export for `impl.assert.json_type`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      - name: type_name
        type: any
        required: true
        description: Input parameter `type_name`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          subject: <subject>
          type_name: <type_name>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: impl.assertion.core
  module: impl
  stability: alpha
  owner: spec_runner
  tags:
  - impl
doc:
  summary: Case `LIB-IMPL-ASSERT-001-003-IMPL-ASSERT-JSON-TYPE` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```
