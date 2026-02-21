# Spec-Lang Repo Domain Library

## LIB-DOMAIN-REPO-001

```yaml contract-spec
id: LIB-DOMAIN-REPO-001-001-DOMAIN-REPO-WALK-MATCHING
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
harness:
  exports:
  - as: domain.repo.walk_matching
    from: assert.function
    path: /__export__domain.repo.walk_matching
    params:
    - root
    - pattern
    required: true
    doc:
      summary: Contract export for `domain.repo.walk_matching`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: root
        type: any
        required: true
        description: Input parameter `root`.
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
          root: <root>
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
contract:
  defaults: {}
  steps:
  - id: __export__domain.repo.walk_matching
    assert:
      ops.fs.walk:
      - {var: root}
      - lit:
          pattern:
            var: pattern
          include_dirs: false
          relative: true
library:
  id: domain.repo.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-REPO-001-001-DOMAIN-REPO-WALK-MATCHING` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```
