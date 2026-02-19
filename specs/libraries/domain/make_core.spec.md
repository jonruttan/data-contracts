# Spec-Lang Makefile Domain Library

## LIB-DOMAIN-MAKE-001

```yaml contract-spec
id: LIB-DOMAIN-MAKE-001
title: makefile projection helper functions
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__make.has_target
    assert:
      std.string.contains:
      - std.object.get:
        - {var: subject}
        - value
      - {var: target}
harness:
  exports:
  - as: make.has_target
    from: assert.function
    path: /__export__make.has_target
    params:
    - subject
    - target
    required: true
    doc:
      summary: Contract export for `make.has_target`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      - name: target
        type: any
        required: true
        description: Input parameter `target`.
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
          target: <target>
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
  id: domain.make.core
  module: domain
  stability: alpha
  owner: spec_runner
  tags:
  - domain
```
