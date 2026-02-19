# Spec-Lang Python Domain Library

## LIB-DOMAIN-PY-001

```yaml contract-spec
id: LIB-DOMAIN-PY-001
title: python projection helper functions
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__py.is_tuple_projection
    assert:
      std.logic.eq:
      - std.object.get:
        - std.object.get:
          - {var: subject}
          - meta
        - native_kind
      - python.tuple
harness:
  exports:
  - as: py.is_tuple_projection
    from: assert.function
    path: /__export__py.is_tuple_projection
    params:
    - subject
    required: true
    doc:
      summary: Contract export for `py.is_tuple_projection`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
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
  id: domain.python.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-PY-001` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```
