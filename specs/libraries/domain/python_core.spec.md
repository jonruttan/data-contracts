```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.export
contracts:
- id: LIB-DOMAIN-PY-001
  title: python projection helper functions
  clauses:
    predicates:
    - id: __export__py.is_tuple_projection
      assert:
        std.logic.eq:
        - std.object.get:
          - std.object.get:
            - var: subject
            - meta
          - native_kind
        - python.tuple
  harness:
    exports:
    - as: py.is_tuple_projection
      from: assert.function
      path: "/__export__py.is_tuple_projection"
      params:
      - subject
      required: true
      docs:
      - id: py.is_tuple_projection.doc.1
        summary: Contract export for `py.is_tuple_projection`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.python.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-PY-001.doc.1
    summary: Case `LIB-DOMAIN-PY-001` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
```
