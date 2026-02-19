# Spec-Lang Process Domain Library

## LIB-DOMAIN-PROCESS-001

```yaml contract-spec
id: LIB-DOMAIN-PROCESS-001-001-DOMAIN-PROCESS-EXEC-CAPTURE-EX-CODE
type: contract.export
harness:
  spec_lang:
    capabilities:
    - ops.os
  exports:
  - as: domain.process.exec_capture_ex_code
    from: assert.function
    path: /__export__domain.process.exec_capture_ex_code
    params:
    - command
    - options
    required: true
    doc:
      summary: Contract export for `domain.process.exec_capture_ex_code`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: command
        type: any
        required: true
        description: Input parameter `command`.
      - name: options
        type: any
        required: true
        description: Input parameter `options`.
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
          command: <command>
          options: <options>
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
  defaults:
    class: MUST
  steps:
  - id: __export__domain.process.exec_capture_ex_code
    assert:
      std.object.get:
      - ops.os.exec_capture_ex:
        - {var: command}
        - {var: options}
      - code
library:
  id: domain.process.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-PROCESS-001-001-DOMAIN-PROCESS-EXEC-CAPTURE-EX-CODE` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```
