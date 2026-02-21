```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.export
contracts:
- id: LIB-DOMAIN-REPO-001-001-DOMAIN-REPO-WALK-MATCHING
  harness:
    exports:
    - as: domain.repo.walk_matching
      from: assert.function
      path: "/__export__domain.repo.walk_matching"
      params:
      - root
      - pattern
      required: true
      docs:
      - id: domain.repo.walk_matching.doc.1
        summary: Contract export for `domain.repo.walk_matching`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  root: \"<root>\"\n  pattern: \"<pattern>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: root\n  type: any\n  required: true\n  description: Input parameter `root`.\n- name: pattern\n  type: any\n  required: true\n  description: Input parameter `pattern`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  clauses:
    predicates:
    - id: __export__domain.repo.walk_matching
      assert:
        ops.fs.walk:
        - var: root
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
  docs:
  - id: LIB-DOMAIN-REPO-001-001-DOMAIN-REPO-WALK-MATCHING.doc.1
    summary: Case `LIB-DOMAIN-REPO-001-001-DOMAIN-REPO-WALK-MATCHING` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
```
