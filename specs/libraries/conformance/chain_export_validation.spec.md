# Chain Export Validation Fixtures

This file is intentionally non-executable as a standalone conformance surface.
It provides producer cases referenced by conformance negative tests.

## BAD-EXPORT-PATH

```yaml contract-spec
id: BAD-EXPORT-PATH
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: valid_step
    assert:
      std.logic.eq:
      - {var: subject}
      - {var: subject}
harness:
  exports:
  - as: bad.path.symbol
    from: assert.function
    path: /missing_step
    params:
    - subject
    required: true
    doc:
      summary: Contract export for `bad.path.symbol`.
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
  id: conformance.chain.export.validation
  module: conformance
  stability: alpha
  owner: data-contracts
  tags:
  - conformance
doc:
  summary: Case `BAD-EXPORT-PATH` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

## BAD-EXPORT-CLASS

```yaml contract-spec
id: BAD-EXPORT-CLASS
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: non_must_step
    class: MAY
    assert:
      std.logic.eq:
      - {var: subject}
      - {var: subject}
harness:
  exports:
  - as: bad.class.symbol
    from: assert.function
    path: /non_must_step
    params:
    - subject
    required: true
    doc:
      summary: Contract export for `bad.class.symbol`.
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
  id: conformance.chain.export.validation
  module: conformance
  stability: alpha
  owner: data-contracts
  tags:
  - conformance
doc:
  summary: Case `BAD-EXPORT-CLASS` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```
