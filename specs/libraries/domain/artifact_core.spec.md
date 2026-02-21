```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.export
contracts:
- id: LIB-DOMAIN-ARTIFACT-001-001-DOMAIN-ARTIFACT-WRITE-YAML
  harness:
    exports:
    - as: domain.artifact.write_yaml
      from: assert.function
      path: "/__export__domain.artifact.write_yaml"
      params:
      - path
      - value
      required: true
      docs:
      - id: domain.artifact.write_yaml.doc.1
        summary: Contract export for `domain.artifact.write_yaml`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\n  value: \"<value>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- name: value\n  type: any\n  required: true\n  description: Input parameter `value`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  clauses:
    predicates:
    - id: __export__domain.artifact.write_yaml
      assert:
        ops.fs.file.set:
        - var: path
        - ops.fs.yaml.stringify:
          - var: value
  library:
    id: domain.artifact.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-ARTIFACT-001-001-DOMAIN-ARTIFACT-WRITE-YAML.doc.1
    summary: Case `LIB-DOMAIN-ARTIFACT-001-001-DOMAIN-ARTIFACT-WRITE-YAML` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-ARTIFACT-001-002-DOMAIN-ARTIFACT-APPEND-TEXT
  harness:
    exports:
    - as: domain.artifact.append_text
      from: assert.function
      path: "/__export__domain.artifact.append_text"
      params:
      - path
      - content
      required: true
      docs:
      - id: domain.artifact.append_text.doc.1
        summary: Contract export for `domain.artifact.append_text`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\n  content: \"<content>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- name: content\n  type: any\n  required: true\n  description: Input parameter `content`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  clauses:
    predicates:
    - id: __export__domain.artifact.append_text
      assert:
        ops.fs.file.append:
        - var: path
        - var: content
  library:
    id: domain.artifact.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-ARTIFACT-001-002-DOMAIN-ARTIFACT-APPEND-TEXT.doc.1
    summary: Case `LIB-DOMAIN-ARTIFACT-001-002-DOMAIN-ARTIFACT-APPEND-TEXT` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
```

