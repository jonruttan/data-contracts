# Spec-Lang YAML Domain Library

## LIB-DOMAIN-YAML-001

```yaml contract-spec
id: LIB-DOMAIN-YAML-001-001-DOMAIN-YAML-PARSE-GET-OR
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__domain.yaml.parse_get_or
    assert:
      ops.fs.yaml.get_or:
      - ops.fs.yaml.parse:
        - {var: yaml_text}
      - {var: path_segments}
      - {var: fallback}
harness:
  exports:
  - as: domain.yaml.parse_get_or
    from: assert.function
    path: /__export__domain.yaml.parse_get_or
    params:
    - yaml_text
    - path_segments
    - fallback
    required: true
    doc:
      summary: Contract export for `domain.yaml.parse_get_or`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: yaml_text
        type: any
        required: true
        description: Input parameter `yaml_text`.
      - name: path_segments
        type: any
        required: true
        description: Input parameter `path_segments`.
      - name: fallback
        type: any
        required: true
        description: Input parameter `fallback`.
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
          yaml_text: <yaml_text>
          path_segments: <path_segments>
          fallback: <fallback>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.yaml.core
  module: domain
  stability: alpha
  owner: spec_runner
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-YAML-001-001-DOMAIN-YAML-PARSE-GET-OR` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-YAML-001-002-DOMAIN-YAML-STRINGIFY
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__domain.yaml.stringify
    assert:
      ops.fs.yaml.stringify:
      - {var: value}
harness:
  exports:
  - as: domain.yaml.stringify
    from: assert.function
    path: /__export__domain.yaml.stringify
    params:
    - value
    required: true
    doc:
      summary: Contract export for `domain.yaml.stringify`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
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
library:
  id: domain.yaml.core
  module: domain
  stability: alpha
  owner: spec_runner
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-YAML-001-002-DOMAIN-YAML-STRINGIFY` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```
