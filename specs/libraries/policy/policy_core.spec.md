# Spec-Lang Policy Core Library

## LIB-POLICY-001

```yaml contract-spec
id: LIB-POLICY-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: policy-core reusable governance predicates
type: contract.export
contract:
  defaults: {}
  steps:
  - id: __export__policy.pass_when_no_violations
    assert:
      std.collection.is_empty:
      - std.object.get:
        - {var: subject}
        - violations
  - id: __export__policy.fail_when_has_violations
    assert:
      std.logic.not:
      - call:
        - {var: policy.pass_when_no_violations}
        - {var: subject}
  - id: __export__policy.check_id_is
    assert:
      std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - {var: expected}
  - id: __export__policy.violation_count_is
    assert:
      std.logic.eq:
      - std.object.get:
        - {var: subject}
        - violation_count
      - {var: expected}
harness:
  exports:
  - as: policy.pass_when_no_violations
    from: assert.function
    path: /__export__policy.pass_when_no_violations
    params:
    - subject
    required: true
    doc:
      summary: Contract export for `policy.pass_when_no_violations`.
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
  - as: policy.fail_when_has_violations
    from: assert.function
    path: /__export__policy.fail_when_has_violations
    params:
    - subject
    required: true
    doc:
      summary: Contract export for `policy.fail_when_has_violations`.
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
  - as: policy.check_id_is
    from: assert.function
    path: /__export__policy.check_id_is
    params:
    - subject
    - expected
    required: true
    doc:
      summary: Contract export for `policy.check_id_is`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      - name: expected
        type: any
        required: true
        description: Input parameter `expected`.
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
          expected: <expected>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
  - as: policy.violation_count_is
    from: assert.function
    path: /__export__policy.violation_count_is
    params:
    - subject
    - expected
    required: true
    doc:
      summary: Contract export for `policy.violation_count_is`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      - name: expected
        type: any
        required: true
        description: Input parameter `expected`.
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
          expected: <expected>
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
  id: policy.policy.core
  module: policy
  stability: alpha
  owner: data-contracts
  tags:
  - policy
doc:
  summary: Case `LIB-POLICY-001` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```
