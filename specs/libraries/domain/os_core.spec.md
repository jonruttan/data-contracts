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
    doc:
      summary: Contract export for `domain.os.exec_ok`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: command
        type: any
        required: true
        description: Input parameter `command`.
      - name: timeout_ms
        type: any
        required: true
        description: Input parameter `timeout_ms`.
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
          timeout_ms: <timeout_ms>
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
  id: domain.os.core
  module: domain
  stability: alpha
  owner: spec_runner
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-OS-001-001-DOMAIN-OS-EXEC-OK` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
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
    doc:
      summary: Contract export for `domain.os.exec_capture_code`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: command
        type: any
        required: true
        description: Input parameter `command`.
      - name: timeout_ms
        type: any
        required: true
        description: Input parameter `timeout_ms`.
      - name: expected_code
        type: any
        required: true
        description: Input parameter `expected_code`.
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
          timeout_ms: <timeout_ms>
          expected_code: <expected_code>
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
  id: domain.os.core
  module: domain
  stability: alpha
  owner: spec_runner
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-OS-001-002-DOMAIN-OS-EXEC-CAPTURE-CODE` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
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
    doc:
      summary: Contract export for `domain.os.env_has`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: key
        type: any
        required: true
        description: Input parameter `key`.
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
          key: <key>
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
  id: domain.os.core
  module: domain
  stability: alpha
  owner: spec_runner
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-OS-001-003-DOMAIN-OS-ENV-HAS` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```
