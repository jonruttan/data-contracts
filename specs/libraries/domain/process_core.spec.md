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
contract:
- id: __export__domain.process.exec_capture_ex_code
  class: MUST
  asserts:
  - std.object.get:
    - ops.os.exec_capture_ex:
      - {var: command}
      - {var: options}
    - code
```
