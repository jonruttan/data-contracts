```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
contracts:
- id: LIB-POLICY-002-001-POLICY-METRIC-NON-DECREASE
  title: 'policy-metrics reusable non-regression predicates: policy.metric_non_decrease'
  type: contract.export
  clauses:
    predicates:
    - id: __export__policy.metric_non_decrease
      assert:
        std.logic.gte:
        - std.math.add:
          - std.object.get:
            - var: subject
            - var: field
          - var: epsilon
        - std.object.get:
          - var: subject
          - var: baseline_field
  harness:
    exports:
    - as: policy.metric_non_decrease
      from: assert.function
      path: "/__export__policy.metric_non_decrease"
      params:
      - subject
      - field
      - baseline_field
      - epsilon
      required: true
      docs:
      - id: policy.metric_non_decrease.doc.1
        summary: Contract export for `policy.metric_non_decrease`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\n  field: \"<field>\"\n  baseline_field: \"<baseline_field>\"\n  epsilon: \"<epsilon>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- name: field\n  type: any\n  required: true\n  description: Input parameter `field`.\n- name: baseline_field\n  type: any\n  required: true\n  description: Input parameter `baseline_field`.\n- name: epsilon\n  type: any\n  required: true\n  description: Input parameter `epsilon`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: policy.policy.metrics
    module: policy
    stability: alpha
    owner: data-contracts
    tags:
    - policy
  docs:
  - id: LIB-POLICY-002-001-POLICY-METRIC-NON-DECREASE.doc.1
    summary: Case `LIB-POLICY-002-001-POLICY-METRIC-NON-DECREASE` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-POLICY-002-002-POLICY-METRIC-NON-INCREASE
  title: 'policy-metrics reusable non-regression predicates: policy.metric_non_increase'
  type: contract.export
  clauses:
    predicates:
    - id: __export__policy.metric_non_increase
      assert:
        std.logic.lte:
        - std.math.sub:
          - std.object.get:
            - var: subject
            - var: field
          - var: epsilon
        - std.object.get:
          - var: subject
          - var: baseline_field
  harness:
    exports:
    - as: policy.metric_non_increase
      from: assert.function
      path: "/__export__policy.metric_non_increase"
      params:
      - subject
      - field
      - baseline_field
      - epsilon
      required: true
      docs:
      - id: policy.metric_non_increase.doc.1
        summary: Contract export for `policy.metric_non_increase`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\n  field: \"<field>\"\n  baseline_field: \"<baseline_field>\"\n  epsilon: \"<epsilon>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- name: field\n  type: any\n  required: true\n  description: Input parameter `field`.\n- name: baseline_field\n  type: any\n  required: true\n  description: Input parameter `baseline_field`.\n- name: epsilon\n  type: any\n  required: true\n  description: Input parameter `epsilon`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: policy.policy.metrics
    module: policy
    stability: alpha
    owner: data-contracts
    tags:
    - policy
  docs:
  - id: LIB-POLICY-002-002-POLICY-METRIC-NON-INCREASE.doc.1
    summary: Case `LIB-POLICY-002-002-POLICY-METRIC-NON-INCREASE` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-POLICY-002-900-POLICY-METRIC-SMOKE
  title: policy metric helpers execute as colocated executable checks
  type: contract.check
  harness:
    check:
      profile: text.file
      config: {}
    use:
    - ref: "#LIB-POLICY-002-001-POLICY-METRIC-NON-DECREASE"
      as: lib_non_decrease
      symbols:
      - policy.metric_non_decrease
    - ref: "#LIB-POLICY-002-002-POLICY-METRIC-NON-INCREASE"
      as: lib_non_increase
      symbols:
      - policy.metric_non_increase
  clauses:
    imports:
    - from: artifact
      names:
      - text
    predicates:
    - id: assert_1
      assert:
      - call:
        - var: policy.metric_non_decrease
        - lit:
            current: 10
            baseline: 9
        - current
        - baseline
        - 0
      - call:
        - var: policy.metric_non_increase
        - lit:
            current: 8
            baseline: 9
        - current
        - baseline
        - 0
```


