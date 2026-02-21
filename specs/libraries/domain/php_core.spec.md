```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.export
contracts:
- id: LIB-DOMAIN-PHP-001
  title: php projection helper functions
  clauses:
    predicates:
    - id: __export__php.is_assoc_projection
      assert:
        std.logic.eq:
        - std.object.get:
          - std.object.get:
            - var: subject
            - meta
          - php_array_kind
        - assoc
  harness:
    exports:
    - as: php.is_assoc_projection
      from: assert.function
      path: "/__export__php.is_assoc_projection"
      params:
      - subject
      required: true
      docs:
      - id: php.is_assoc_projection.doc.1
        summary: Contract export for `php.is_assoc_projection`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.php.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-PHP-001.doc.1
    summary: Case `LIB-DOMAIN-PHP-001` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
```
