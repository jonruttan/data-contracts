```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.export
contracts:
- id: LIB-DOMAIN-OS-001-001-DOMAIN-OS-EXEC-OK
  clauses:
    predicates:
    - id: __export__domain.os.exec_ok
      assert:
        std.logic.eq:
        - ops.os.exec:
          - var: command
          - var: timeout_ms
        - 0
  harness:
    exports:
    - as: domain.os.exec_ok
      from: assert.function
      path: "/__export__domain.os.exec_ok"
      params:
      - command
      - timeout_ms
      required: true
      docs:
      - id: domain.os.exec_ok.doc.1
        summary: Contract export for `domain.os.exec_ok`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  command: \"<command>\"\n  timeout_ms: \"<timeout_ms>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: command\n  type: any\n  required: true\n  description: Input parameter `command`.\n- name: timeout_ms\n  type: any\n  required: true\n  description: Input parameter `timeout_ms`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.os.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-OS-001-001-DOMAIN-OS-EXEC-OK.doc.1
    summary: Case `LIB-DOMAIN-OS-001-001-DOMAIN-OS-EXEC-OK` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-OS-001-002-DOMAIN-OS-EXEC-CAPTURE-CODE
  clauses:
    predicates:
    - id: __export__domain.os.exec_capture_code
      assert:
        std.logic.eq:
        - std.object.get:
          - ops.os.exec_capture:
            - var: command
            - var: timeout_ms
          - code
        - var: expected_code
  harness:
    exports:
    - as: domain.os.exec_capture_code
      from: assert.function
      path: "/__export__domain.os.exec_capture_code"
      params:
      - command
      - timeout_ms
      - expected_code
      required: true
      docs:
      - id: domain.os.exec_capture_code.doc.1
        summary: Contract export for `domain.os.exec_capture_code`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  command: \"<command>\"\n  timeout_ms: \"<timeout_ms>\"\n  expected_code: \"<expected_code>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: command\n  type: any\n  required: true\n  description: Input parameter `command`.\n- name: timeout_ms\n  type: any\n  required: true\n  description: Input parameter `timeout_ms`.\n- name: expected_code\n  type: any\n  required: true\n  description: Input parameter `expected_code`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.os.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-OS-001-002-DOMAIN-OS-EXEC-CAPTURE-CODE.doc.1
    summary: Case `LIB-DOMAIN-OS-001-002-DOMAIN-OS-EXEC-CAPTURE-CODE` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-OS-001-003-DOMAIN-OS-ENV-HAS
  clauses:
    predicates:
    - id: __export__domain.os.env_has
      assert:
        ops.os.env_has:
        - var: key
  harness:
    exports:
    - as: domain.os.env_has
      from: assert.function
      path: "/__export__domain.os.env_has"
      params:
      - key
      required: true
      docs:
      - id: domain.os.env_has.doc.1
        summary: Contract export for `domain.os.env_has`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  key: \"<key>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: key\n  type: any\n  required: true\n  description: Input parameter `key`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.os.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-OS-001-003-DOMAIN-OS-ENV-HAS.doc.1
    summary: Case `LIB-DOMAIN-OS-001-003-DOMAIN-OS-ENV-HAS` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
```


