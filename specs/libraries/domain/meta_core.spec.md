```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.export
contracts:
- id: LIB-DOMAIN-META-001-001-DOMAIN-META-CASE-ID-EQ
  clauses:
    predicates:
    - id: __export__domain.meta.case_id_eq
      assert:
        std.logic.eq:
        - std.object.get:
          - std.object.get:
            - var: meta
            - case
          - id
        - var: case_id
  harness:
    exports:
    - as: domain.meta.case_id_eq
      from: assert.function
      path: "/__export__domain.meta.case_id_eq"
      params:
      - meta
      - case_id
      required: true
      docs:
      - id: domain.meta.case_id_eq.doc.1
        summary: Contract export for `domain.meta.case_id_eq`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  meta: \"<meta>\"\n  case_id: \"<case_id>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: meta\n  type: any\n  required: true\n  description: Input parameter `meta`.\n- name: case_id\n  type: any\n  required: true\n  description: Input parameter `case_id`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.meta.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-META-001-001-DOMAIN-META-CASE-ID-EQ.doc.1
    summary: Case `LIB-DOMAIN-META-001-001-DOMAIN-META-CASE-ID-EQ` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-META-001-002-DOMAIN-META-HAS-ARTIFACT-TARGET
  clauses:
    predicates:
    - id: __export__domain.meta.has_artifact_target
      assert:
        std.collection.includes:
        - std.object.get:
          - std.object.get:
            - var: meta
            - artifacts
          - target_keys
        - var: target_name
  harness:
    exports:
    - as: domain.meta.has_artifact_target
      from: assert.function
      path: "/__export__domain.meta.has_artifact_target"
      params:
      - meta
      - target_name
      required: true
      docs:
      - id: domain.meta.has_artifact_target.doc.1
        summary: Contract export for `domain.meta.has_artifact_target`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  meta: \"<meta>\"\n  target_name: \"<target_name>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: meta\n  type: any\n  required: true\n  description: Input parameter `meta`.\n- name: target_name\n  type: any\n  required: true\n  description: Input parameter `target_name`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.meta.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-META-001-002-DOMAIN-META-HAS-ARTIFACT-TARGET.doc.1
    summary: Case `LIB-DOMAIN-META-001-002-DOMAIN-META-HAS-ARTIFACT-TARGET` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
```

