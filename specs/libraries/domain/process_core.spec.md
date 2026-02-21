```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.export
contracts:
- id: LIB-DOMAIN-PROCESS-001-001-DOMAIN-PROCESS-EXEC-CAPTURE-EX-CODE
  harness:
    spec_lang:
      capabilities:
      - ops.os
    exports:
    - as: domain.process.exec_capture_ex_code
      from: assert.function
      path: "/__export__domain.process.exec_capture_ex_code"
      params:
      - command
      - options
      required: true
      docs:
      - id: domain.process.exec_capture_ex_code.doc.1
        summary: Contract export for `domain.process.exec_capture_ex_code`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  command: \"<command>\"\n  options: \"<options>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: command\n  type: any\n  required: true\n  description: Input parameter `command`.\n- name: options\n  type: any\n  required: true\n  description: Input parameter `options`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  clauses:
    predicates:
    - id: __export__domain.process.exec_capture_ex_code
      assert:
        std.object.get:
        - ops.os.exec_capture_ex:
          - var: command
          - var: options
        - code
  library:
    id: domain.process.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-PROCESS-001-001-DOMAIN-PROCESS-EXEC-CAPTURE-EX-CODE.doc.1
    summary: Case `LIB-DOMAIN-PROCESS-001-001-DOMAIN-PROCESS-EXEC-CAPTURE-EX-CODE` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
```
