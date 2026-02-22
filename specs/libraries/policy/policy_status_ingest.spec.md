```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'check': {'profile': 'text.file', 'config': {}}, 'use': [{'ref': '#LIB-POLICY-INGEST-001',
      'as': 'lib_policy_ingest', 'symbols': ['policy.ingest.matrix_has_rows', 'policy.ingest.required_lane_policy_effect_valid',
      'policy.ingest.compat_stale_missing_count_within_limit', 'policy.ingest.log_entries_correlate_matrix_rows']}]}"
    - "{'exports': [{'as': 'policy.ingest.matrix_has_rows', 'from': 'assert.function',
      'path': '/__export__policy.ingest.matrix_has_rows', 'params': ['subject'], 'required':
      True}, {'as': 'policy.ingest.required_lane_policy_effect_valid', 'from': 'assert.function',
      'path': '/__export__policy.ingest.required_lane_policy_effect_valid', 'params':
      ['subject'], 'required': True}, {'as': 'policy.ingest.compat_stale_missing_count_within_limit',
      'from': 'assert.function', 'path': '/__export__policy.ingest.compat_stale_missing_count_within_limit',
      'params': ['subject'], 'required': True}, {'as': 'policy.ingest.log_entries_correlate_matrix_rows',
      'from': 'assert.function', 'path': '/__export__policy.ingest.log_entries_correlate_matrix_rows',
      'params': ['subject'], 'required': True}]}"
services:
- id: svc.exports_as_policy_ingest_matrix_has_rows_from_assert_function_path_export_policy_ingest_matrix_has_rows_params_subject_required_true_as_policy_ingest_required_lane_policy_effect_valid_from_assert_function_path_export_policy_ingest_required_lane_policy_effect_valid_params_subject_required_true_as_policy_ingest_compat_stale_missing_count_within_limit_from_assert_function_path_export_policy_ingest_compat_stale_missing_count_within_limit_params_subject_required_true_as_policy_ingest_log_entries_correlate_matrix_rows_from_assert_function_path_export_policy_ingest_log_entries_correlate_matrix_rows_params_subject_required_true.default.1
  type: legacy.exports_as_policy_ingest_matrix_has_rows_from_assert_function_path_export_policy_ingest_matrix_has_rows_params_subject_required_true_as_policy_ingest_required_lane_policy_effect_valid_from_assert_function_path_export_policy_ingest_required_lane_policy_effect_valid_params_subject_required_true_as_policy_ingest_compat_stale_missing_count_within_limit_from_assert_function_path_export_policy_ingest_compat_stale_missing_count_within_limit_params_subject_required_true_as_policy_ingest_log_entries_correlate_matrix_rows_from_assert_function_path_export_policy_ingest_log_entries_correlate_matrix_rows_params_subject_required_true
  mode: default
- id: svc.check_profile_text_file_config_use_ref_lib_policy_ingest_001_as_lib_policy_ingest_symbols_policy_ingest_matrix_has_rows_policy_ingest_required_lane_policy_effect_valid_policy_ingest_compat_stale_missing_count_within_limit_policy_ingest_log_entries_correlate_matrix_rows.default.1
  type: legacy.check_profile_text_file_config_use_ref_lib_policy_ingest_001_as_lib_policy_ingest_symbols_policy_ingest_matrix_has_rows_policy_ingest_required_lane_policy_effect_valid_policy_ingest_compat_stale_missing_count_within_limit_policy_ingest_log_entries_correlate_matrix_rows
  mode: default
contracts:
- id: LIB-POLICY-INGEST-001
  title: status ingest predicates
  clauses:
    predicates:
    - id: __export__policy.ingest.matrix_has_rows
      assert:
        std.logic.gt:
        - std.collection.length:
          - std.object.get:
            - var: subject
            - matrix_rows
        - 0
    - id: __export__policy.ingest.required_lane_policy_effect_valid
      assert:
        std.logic.not:
        - std.collection.any:
          - std.object.get:
            - var: subject
            - matrix_rows
          - std.logic.and:
            - std.logic.eq:
              - std.object.get:
                - var: item
                - lane_class
              - required
            - std.logic.not:
              - std.logic.eq:
                - std.object.get:
                  - var: item
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
            - var: subject
            - matrix_rows
        - std.collection.length:
          - std.object.get:
            - std.object.get:
              - var: subject
              - ingest_log
            - entries
  library:
    id: policy.status.ingest
    module: policy
    stability: alpha
    owner: data-contracts
    tags:
    - policy
    - runtime
  type: contract.export
- id: LIB-POLICY-INGEST-900
  title: status ingest policy library smoke
  clauses:
    imports:
    - from: artifact
      names:
      - text
    predicates:
    - id: assert_1
      assert:
      - call:
        - var: policy.ingest.matrix_has_rows
        - lit:
            matrix_rows:
            - runner_id: dc-runner-rust
            ingest_log:
              entries:
              - runner_id: dc-runner-rust
      - call:
        - var: policy.ingest.required_lane_policy_effect_valid
        - lit:
            matrix_rows:
            - lane_class: required
              policy_effect: blocking_fail
      - call:
        - var: policy.ingest.compat_stale_missing_count_within_limit
        - lit: {}
      - call:
        - var: policy.ingest.log_entries_correlate_matrix_rows
        - lit:
            matrix_rows:
            - runner_id: dc-runner-rust
            ingest_log:
              entries:
              - runner_id: dc-runner-rust
  type: contract.check
```


