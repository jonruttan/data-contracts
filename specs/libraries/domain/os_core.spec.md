# Spec-Lang OS Domain Library

## LIB-DOMAIN-OS-001

```yaml contract-spec
id: LIB-DOMAIN-OS-001-001-DOMAIN-OS-EXEC-OK
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__domain.os.exec_ok
    assert:
      std.logic.eq:
      - ops.os.exec:
        - {var: command}
        - {var: timeout_ms}
      - 0
harness:
  exports:
  - as: domain.os.exec_ok
    from: assert.function
    path: /__export__domain.os.exec_ok
    params:
    - command
    - timeout_ms
    required: true
```

```yaml contract-spec
id: LIB-DOMAIN-OS-001-002-DOMAIN-OS-EXEC-CAPTURE-CODE
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__domain.os.exec_capture_code
    assert:
      std.logic.eq:
      - std.object.get:
        - ops.os.exec_capture:
          - {var: command}
          - {var: timeout_ms}
        - code
      - {var: expected_code}
harness:
  exports:
  - as: domain.os.exec_capture_code
    from: assert.function
    path: /__export__domain.os.exec_capture_code
    params:
    - command
    - timeout_ms
    - expected_code
    required: true
```

```yaml contract-spec
id: LIB-DOMAIN-OS-001-003-DOMAIN-OS-ENV-HAS
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__domain.os.env_has
    assert:
      ops.os.env_has:
      - {var: key}
harness:
  exports:
  - as: domain.os.env_has
    from: assert.function
    path: /__export__domain.os.env_has
    params:
    - key
    required: true
```
