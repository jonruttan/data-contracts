# Spec-Lang YAML Domain Library

## LIB-DOMAIN-YAML-001

```yaml contract-spec
id: LIB-DOMAIN-YAML-001-001-DOMAIN-YAML-PARSE-GET-OR
type: contract.export
contract:
- id: __export__domain.yaml.parse_get_or
  class: MUST
  asserts:
  - ops.fs.yaml.get_or:
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
```

```yaml contract-spec
id: LIB-DOMAIN-YAML-001-002-DOMAIN-YAML-STRINGIFY
type: contract.export
contract:
- id: __export__domain.yaml.stringify
  class: MUST
  asserts:
  - ops.fs.yaml.stringify:
    - {var: value}
harness:
  exports:
  - as: domain.yaml.stringify
    from: assert.function
    path: /__export__domain.yaml.stringify
    params:
    - value
    required: true
```
