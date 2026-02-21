# Status Ingest Policy Library

## LIB-POLICY-INGEST-001

```yaml contract-spec
id: LIB-POLICY-INGEST-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
title: status ingest predicates
contract:
  defaults: {}
  steps:
    - id: __export__policy.ingest.matrix_has_rows
      assert:
        std.logic.gt:
          - std.collection.length:
              - std.object.get:
                  - {var: subject}
                  - matrix_rows
          - 0
    - id: __export__policy.ingest.required_lane_policy_effect_valid
      assert:
        std.logic.not:
          - std.collection.any:
              - std.object.get:
                  - {var: subject}
                  - matrix_rows
              - std.logic.and:
                  - std.logic.eq:
                      - std.object.get:
                          - {var: item}
                          - lane_class
                      - required
                  - std.logic.not:
                      - std.logic.eq:
                          - std.object.get:
                              - {var: item}
                              - policy_effect
                          - blocking_fail
    - id: __export__policy.ingest.compat_stale_missing_count_within_limit
      assert:
        std.logic.gte:
          - 0
          - 0
    - id: __export__policy.ingest.log_entries_correlate_matrix_rows
      assert:
        std.logic.eq:
          - std.collection.length:
              - std.object.get:
                  - {var: subject}
                  - matrix_rows
          - std.collection.length:
              - std.object.get:
                  - std.object.get:
                      - {var: subject}
                      - ingest_log
                  - entries
harness:
  exports:
    - as: policy.ingest.matrix_has_rows
      from: assert.function
      path: /__export__policy.ingest.matrix_has_rows
      params: [subject]
      required: true
    - as: policy.ingest.required_lane_policy_effect_valid
      from: assert.function
      path: /__export__policy.ingest.required_lane_policy_effect_valid
      params: [subject]
      required: true
    - as: policy.ingest.compat_stale_missing_count_within_limit
      from: assert.function
      path: /__export__policy.ingest.compat_stale_missing_count_within_limit
      params: [subject]
      required: true
    - as: policy.ingest.log_entries_correlate_matrix_rows
      from: assert.function
      path: /__export__policy.ingest.log_entries_correlate_matrix_rows
      params: [subject]
      required: true
library:
  id: policy.status.ingest
  module: policy
  stability: alpha
  owner: data-contracts
  tags: [policy, runtime]
```

## LIB-POLICY-INGEST-900

```yaml contract-spec
id: LIB-POLICY-INGEST-900
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.check
title: status ingest policy library smoke
harness:
  check:
    profile: text.file
    config: {}
  use:
    - ref: '#LIB-POLICY-INGEST-001'
      as: lib_policy_ingest
      symbols:
        - policy.ingest.matrix_has_rows
        - policy.ingest.required_lane_policy_effect_valid
        - policy.ingest.compat_stale_missing_count_within_limit
        - policy.ingest.log_entries_correlate_matrix_rows
contract:
  defaults: {}
  imports:
    - from: artifact
      names: [text]
  steps:
    - id: assert_1
      assert:
        - call:
            - {var: policy.ingest.matrix_has_rows}
            - lit:
                matrix_rows:
                  - runner_id: dc-runner-rust
                ingest_log:
                  entries:
                    - runner_id: dc-runner-rust
        - call:
            - {var: policy.ingest.required_lane_policy_effect_valid}
            - lit:
                matrix_rows:
                  - lane_class: required
                    policy_effect: blocking_fail
        - call:
            - {var: policy.ingest.compat_stale_missing_count_within_limit}
            - lit: {}
        - call:
            - {var: policy.ingest.log_entries_correlate_matrix_rows}
            - lit:
                matrix_rows:
                  - runner_id: dc-runner-rust
                ingest_log:
                  entries:
                    - runner_id: dc-runner-rust
```
