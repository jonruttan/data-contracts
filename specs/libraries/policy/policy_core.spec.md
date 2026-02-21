```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.export
contracts:
- id: LIB-POLICY-001
  title: policy-core reusable governance predicates
  clauses:
    predicates:
    - id: __export__policy.pass_when_no_violations
      assert:
        std.collection.is_empty:
        - std.object.get:
          - var: subject
          - violations
    - id: __export__policy.fail_when_has_violations
      assert:
        std.logic.not:
        - call:
          - var: policy.pass_when_no_violations
          - var: subject
    - id: __export__policy.check_id_is
      assert:
        std.logic.eq:
        - std.object.get:
          - var: subject
          - check_id
        - var: expected
    - id: __export__policy.violation_count_is
      assert:
        std.logic.eq:
        - std.object.get:
          - var: subject
          - violation_count
        - var: expected
  harness:
    exports:
    - as: policy.pass_when_no_violations
      from: assert.function
      path: "/__export__policy.pass_when_no_violations"
      params:
      - subject
      required: true
      docs:
      - id: policy.pass_when_no_violations.doc.1
        summary: Contract export for `policy.pass_when_no_violations`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: policy.fail_when_has_violations
      from: assert.function
      path: "/__export__policy.fail_when_has_violations"
      params:
      - subject
      required: true
      docs:
      - id: policy.fail_when_has_violations.doc.1
        summary: Contract export for `policy.fail_when_has_violations`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: policy.check_id_is
      from: assert.function
      path: "/__export__policy.check_id_is"
      params:
      - subject
      - expected
      required: true
      docs:
      - id: policy.check_id_is.doc.1
        summary: Contract export for `policy.check_id_is`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\n  expected: \"<expected>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- name: expected\n  type: any\n  required: true\n  description: Input parameter `expected`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: policy.violation_count_is
      from: assert.function
      path: "/__export__policy.violation_count_is"
      params:
      - subject
      - expected
      required: true
      docs:
      - id: policy.violation_count_is.doc.1
        summary: Contract export for `policy.violation_count_is`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\n  expected: \"<expected>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- name: expected\n  type: any\n  required: true\n  description: Input parameter `expected`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: policy.policy.core
    module: policy
    stability: alpha
    owner: data-contracts
    tags:
    - policy
  docs:
  - id: LIB-POLICY-001.doc.1
    summary: Case `LIB-POLICY-001` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
```
