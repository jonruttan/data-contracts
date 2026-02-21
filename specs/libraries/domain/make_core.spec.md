```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.export
contracts:
- id: LIB-DOMAIN-MAKE-001
  title: makefile projection helper functions
  clauses:
    predicates:
    - id: __export__make.has_target
      assert:
        std.string.contains:
        - std.object.get:
          - var: subject
          - value
        - var: target
  harness:
    exports:
    - as: make.has_target
      from: assert.function
      path: "/__export__make.has_target"
      params:
      - subject
      - target
      required: true
      docs:
      - id: make.has_target.doc.1
        summary: Contract export for `make.has_target`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\n  target: \"<target>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- name: target\n  type: any\n  required: true\n  description: Input parameter `target`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.make.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-MAKE-001.doc.1
    summary: Case `LIB-DOMAIN-MAKE-001` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
```
