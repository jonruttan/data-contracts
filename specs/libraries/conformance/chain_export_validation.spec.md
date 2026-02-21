This file is intentionally non-executable as a standalone conformance surface.
It provides producer cases referenced by conformance negative tests.


```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.export
contracts:
- id: BAD-EXPORT-PATH
  clauses:
    predicates:
    - id: valid_step
      assert:
        std.logic.eq:
        - var: subject
        - var: subject
  harness:
    exports:
    - as: bad.path.symbol
      from: assert.function
      path: "/missing_step"
      params:
      - subject
      required: true
      docs:
      - id: bad.path.symbol.doc.1
        summary: Contract export for `bad.path.symbol`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: conformance.chain.export.validation
    module: conformance
    stability: alpha
    owner: data-contracts
    tags:
    - conformance
  docs:
  - id: BAD-EXPORT-PATH.doc.1
    summary: Case `BAD-EXPORT-PATH` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: BAD-EXPORT-CLASS
  clauses:
    predicates:
    - id: non_must_step
      required: false
      assert:
        std.logic.eq:
        - var: subject
        - var: subject
  harness:
    exports:
    - as: bad.class.symbol
      from: assert.function
      path: "/non_must_step"
      params:
      - subject
      required: true
      docs:
      - id: bad.class.symbol.doc.1
        summary: Contract export for `bad.class.symbol`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: conformance.chain.export.validation
    module: conformance
    stability: alpha
    owner: data-contracts
    tags:
    - conformance
  docs:
  - id: BAD-EXPORT-CLASS.doc.1
    summary: Case `BAD-EXPORT-CLASS` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
```


