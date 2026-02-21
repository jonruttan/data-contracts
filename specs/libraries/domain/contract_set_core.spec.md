```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.export
contracts:
- id: LIB-DOMAIN-CONTRACT-SET-001
  title: contract-set manifest projection helper functions
  clauses:
    predicates:
    - id: __export__domain.contract_set.id
      assert:
        std.object.get:
        - var: manifest
        - contract_set_id
    - id: __export__domain.contract_set.depends_on
      assert:
        std.object.get:
        - var: manifest
        - depends_on
    - id: __export__domain.contract_set.include_paths
      assert:
        std.object.get:
        - var: manifest
        - include_paths
    - id: __export__domain.contract_set.applies_to_runners
      assert:
        std.object.get:
        - var: manifest
        - applies_to_runners
  harness:
    exports:
    - as: domain.contract_set.id
      from: assert.function
      path: "/__export__domain.contract_set.id"
      params:
      - manifest
      required: true
      docs:
      - id: domain.contract_set.id.doc.1
        summary: Contract export for `domain.contract_set.id`.
        audience: spec-authors
        status: active
        description: "Returns manifest `contract_set_id`.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Read id\ninput:\n  manifest:\n    contract_set_id: python_runner_contract_set\nexpected: python_runner_contract_set\n- params: - name: manifest\n  type: any\n  required: true\n  description: Contract-set manifest object projection.\n- returns: type: string\ndescription: Manifest contract-set identifier.\n- errors: - code: SCHEMA_ERROR\n  when: Manifest does not contain the required field.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Portable stdlib projection."
        since: v1
    - as: domain.contract_set.depends_on
      from: assert.function
      path: "/__export__domain.contract_set.depends_on"
      params:
      - manifest
      required: true
      docs:
      - id: domain.contract_set.depends_on.doc.1
        summary: Contract export for `domain.contract_set.depends_on`.
        audience: spec-authors
        status: active
        description: "Returns declared dependency list from manifest.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Read dependencies\ninput:\n  manifest:\n    depends_on:\n    - shared_makefile_help_contract_set\nexpected:\n- shared_makefile_help_contract_set\n- params: - name: manifest\n  type: any\n  required: true\n  description: Contract-set manifest object projection.\n- returns: type: list\ndescription: Manifest dependency contract set ids.\n- errors: - code: SCHEMA_ERROR\n  when: Manifest does not contain the required field.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Portable stdlib projection."
        since: v1
    - as: domain.contract_set.include_paths
      from: assert.function
      path: "/__export__domain.contract_set.include_paths"
      params:
      - manifest
      required: true
      docs:
      - id: domain.contract_set.include_paths.doc.1
        summary: Contract export for `domain.contract_set.include_paths`.
        audience: spec-authors
        status: active
        description: "Returns include path/glob list from manifest.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Read include paths\ninput:\n  manifest:\n    include_paths:\n    - specs/impl/python/**\nexpected:\n- specs/impl/python/**\n- params: - name: manifest\n  type: any\n  required: true\n  description: Contract-set manifest object projection.\n- returns: type: list\ndescription: Include path/glob list.\n- errors: - code: SCHEMA_ERROR\n  when: Manifest does not contain the required field.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Portable stdlib projection."
        since: v1
    - as: domain.contract_set.applies_to_runners
      from: assert.function
      path: "/__export__domain.contract_set.applies_to_runners"
      params:
      - manifest
      required: true
      docs:
      - id: domain.contract_set.applies_to_runners.doc.1
        summary: Contract export for `domain.contract_set.applies_to_runners`.
        audience: spec-authors
        status: active
        description: "Returns optional runner applicability list.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Read runner filter\ninput:\n  manifest:\n    applies_to_runners:\n    - python\n    - php\nexpected:\n- python\n- php\n- params: - name: manifest\n  type: any\n  required: true\n  description: Contract-set manifest object projection.\n- returns: type: list\ndescription: Runner ids list or null/empty list per manifest authoring.\n- errors: - code: SCHEMA_ERROR\n  when: Manifest does not contain expected structure.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Portable stdlib projection."
        since: v1
  library:
    id: domain.contract_set.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-CONTRACT-SET-001.doc.1
    summary: Case `LIB-DOMAIN-CONTRACT-SET-001` for `contract.export`.
    audience: spec-authors
    status: active
    description: Contract-set manifest projection exports for resolver policy and validation checks.
    since: v1
    tags:
    - contract.export
```
