# Spec-Lang Artifact Domain Library

## LIB-DOMAIN-ARTIFACT-001

```yaml contract-spec
id: LIB-DOMAIN-ARTIFACT-001-001-DOMAIN-ARTIFACT-WRITE-YAML
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
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__domain.artifact.write_yaml
    assert:
      ops.fs.file.set:
      - {var: path}
      - ops.fs.yaml.stringify:
        - {var: value}
```

```yaml contract-spec
id: LIB-DOMAIN-ARTIFACT-001-002-DOMAIN-ARTIFACT-APPEND-TEXT
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
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__domain.artifact.append_text
    assert:
      ops.fs.file.append:
      - {var: path}
      - {var: content}
```
