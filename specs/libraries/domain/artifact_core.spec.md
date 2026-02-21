# Spec-Lang Artifact Domain Library

## LIB-DOMAIN-ARTIFACT-001

```yaml contract-spec
id: LIB-DOMAIN-ARTIFACT-001-001-DOMAIN-ARTIFACT-WRITE-YAML
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
harness:
  exports:
  - as: domain.artifact.write_yaml
    from: assert.function
    path: /__export__domain.artifact.write_yaml
    params:
    - path
    - value
    required: true
    doc:
      summary: Contract export for `domain.artifact.write_yaml`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: path
        type: any
        required: true
        description: Input parameter `path`.
      - name: value
        type: any
        required: true
        description: Input parameter `value`.
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
          path: <path>
          value: <value>
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
  - id: __export__domain.artifact.write_yaml
    assert:
      ops.fs.file.set:
      - {var: path}
      - ops.fs.yaml.stringify:
        - {var: value}
library:
  id: domain.artifact.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-ARTIFACT-001-001-DOMAIN-ARTIFACT-WRITE-YAML` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-ARTIFACT-001-002-DOMAIN-ARTIFACT-APPEND-TEXT
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
harness:
  exports:
  - as: domain.artifact.append_text
    from: assert.function
    path: /__export__domain.artifact.append_text
    params:
    - path
    - content
    required: true
    doc:
      summary: Contract export for `domain.artifact.append_text`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: path
        type: any
        required: true
        description: Input parameter `path`.
      - name: content
        type: any
        required: true
        description: Input parameter `content`.
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
          path: <path>
          content: <content>
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
  - id: __export__domain.artifact.append_text
    assert:
      ops.fs.file.append:
      - {var: path}
      - {var: content}
library:
  id: domain.artifact.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-ARTIFACT-001-002-DOMAIN-ARTIFACT-APPEND-TEXT` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```
