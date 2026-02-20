# Spec-Lang PHP Domain Library

## LIB-DOMAIN-PHP-001

```yaml contract-spec
id: LIB-DOMAIN-PHP-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: php projection helper functions
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__php.is_assoc_projection
    assert:
      std.logic.eq:
      - std.object.get:
        - std.object.get:
          - {var: subject}
          - meta
        - php_array_kind
      - assoc
harness:
  exports:
  - as: php.is_assoc_projection
    from: assert.function
    path: /__export__php.is_assoc_projection
    params:
    - subject
    required: true
    doc:
      summary: Contract export for `php.is_assoc_projection`.
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
  id: domain.php.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-PHP-001` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```
