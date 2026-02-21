```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.export
contracts:
- id: LIB-DOMAIN-YAML-001-001-DOMAIN-YAML-PARSE-GET-OR
  clauses:
    predicates:
    - id: __export__domain.yaml.parse_get_or
      assert:
        ops.fs.yaml.get_or:
        - ops.fs.yaml.parse:
          - var: yaml_text
        - var: path_segments
        - var: fallback
  harness:
    exports:
    - as: domain.yaml.parse_get_or
      from: assert.function
      path: "/__export__domain.yaml.parse_get_or"
      params:
      - yaml_text
      - path_segments
      - fallback
      required: true
      docs:
      - id: domain.yaml.parse_get_or.doc.1
        summary: Contract export for `domain.yaml.parse_get_or`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  yaml_text: \"<yaml_text>\"\n  path_segments: \"<path_segments>\"\n  fallback: \"<fallback>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: yaml_text\n  type: any\n  required: true\n  description: Input parameter `yaml_text`.\n- name: path_segments\n  type: any\n  required: true\n  description: Input parameter `path_segments`.\n- name: fallback\n  type: any\n  required: true\n  description: Input parameter `fallback`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.yaml.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-YAML-001-001-DOMAIN-YAML-PARSE-GET-OR.doc.1
    summary: Case `LIB-DOMAIN-YAML-001-001-DOMAIN-YAML-PARSE-GET-OR` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-YAML-001-002-DOMAIN-YAML-STRINGIFY
  clauses:
    predicates:
    - id: __export__domain.yaml.stringify
      assert:
        ops.fs.yaml.stringify:
        - var: value
  harness:
    exports:
    - as: domain.yaml.stringify
      from: assert.function
      path: "/__export__domain.yaml.stringify"
      params:
      - value
      required: true
      docs:
      - id: domain.yaml.stringify.doc.1
        summary: Contract export for `domain.yaml.stringify`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  value: \"<value>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: value\n  type: any\n  required: true\n  description: Input parameter `value`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.yaml.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-YAML-001-002-DOMAIN-YAML-STRINGIFY.doc.1
    summary: Case `LIB-DOMAIN-YAML-001-002-DOMAIN-YAML-STRINGIFY` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
```

