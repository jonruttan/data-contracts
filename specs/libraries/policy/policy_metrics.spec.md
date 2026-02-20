# Spec-Lang Policy Metrics Library

## LIB-POLICY-002

```yaml contract-spec
id: LIB-POLICY-002-001-POLICY-METRIC-NON-DECREASE
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: 'policy-metrics reusable non-regression predicates: policy.metric_non_decrease'
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__policy.metric_non_decrease
    assert:
      std.logic.gte:
      - std.math.add:
        - std.object.get:
          - {var: subject}
          - {var: field}
        - {var: epsilon}
      - std.object.get:
        - {var: subject}
        - {var: baseline_field}
harness:
  exports:
  - as: policy.metric_non_decrease
    from: assert.function
    path: /__export__policy.metric_non_decrease
    params:
    - subject
    - field
    - baseline_field
    - epsilon
    required: true
    doc:
      summary: Contract export for `policy.metric_non_decrease`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      - name: field
        type: any
        required: true
        description: Input parameter `field`.
      - name: baseline_field
        type: any
        required: true
        description: Input parameter `baseline_field`.
      - name: epsilon
        type: any
        required: true
        description: Input parameter `epsilon`.
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
          subject: <subject>
          field: <field>
          baseline_field: <baseline_field>
          epsilon: <epsilon>
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
  id: policy.policy.metrics
  module: policy
  stability: alpha
  owner: data-contracts
  tags:
  - policy
doc:
  summary: Case `LIB-POLICY-002-001-POLICY-METRIC-NON-DECREASE` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-POLICY-002-002-POLICY-METRIC-NON-INCREASE
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: 'policy-metrics reusable non-regression predicates: policy.metric_non_increase'
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__policy.metric_non_increase
    assert:
      std.logic.lte:
      - std.math.sub:
        - std.object.get:
          - {var: subject}
          - {var: field}
        - {var: epsilon}
      - std.object.get:
        - {var: subject}
        - {var: baseline_field}
harness:
  exports:
  - as: policy.metric_non_increase
    from: assert.function
    path: /__export__policy.metric_non_increase
    params:
    - subject
    - field
    - baseline_field
    - epsilon
    required: true
    doc:
      summary: Contract export for `policy.metric_non_increase`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      - name: field
        type: any
        required: true
        description: Input parameter `field`.
      - name: baseline_field
        type: any
        required: true
        description: Input parameter `baseline_field`.
      - name: epsilon
        type: any
        required: true
        description: Input parameter `epsilon`.
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
          subject: <subject>
          field: <field>
          baseline_field: <baseline_field>
          epsilon: <epsilon>
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
  id: policy.policy.metrics
  module: policy
  stability: alpha
  owner: data-contracts
  tags:
  - policy
doc:
  summary: Case `LIB-POLICY-002-002-POLICY-METRIC-NON-INCREASE` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-POLICY-002-900-POLICY-METRIC-SMOKE
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: policy metric helpers execute as colocated executable checks
type: contract.check
harness:
  check:
    profile: text.file
    config: {}
  use:
  - ref: '#LIB-POLICY-002-001-POLICY-METRIC-NON-DECREASE'
    as: lib_non_decrease
    symbols:
    - policy.metric_non_decrease
  - ref: '#LIB-POLICY-002-002-POLICY-METRIC-NON-INCREASE'
    as: lib_non_increase
    symbols:
    - policy.metric_non_increase
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - text
  steps:
  - id: assert_1
    assert:
    - call:
      - {var: policy.metric_non_decrease}
      - lit:
          current: 10
          baseline: 9
      - current
      - baseline
      - 0
    - call:
      - {var: policy.metric_non_increase}
      - lit:
          current: 8
          baseline: 9
      - current
      - baseline
      - 0
```
