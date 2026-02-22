```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'spec_lang_builtin_sync': {'required_ops': ['std.math.mul', 'std.math.div', 'std.math.mod', 'std.math.pow', 'std.math.abs', 'std.math.negate', 'std.math.inc', 'std.math.dec', 'std.math.clamp', 'std.math.round', 'std.math.floor', 'std.math.ceil', 'std.logic.compare', 'std.logic.between', 'std.logic.xor', 'std.collection.slice', 'std.collection.reverse', 'std.collection.zip', 'std.collection.zip_with', 'std.math.range', 'std.collection.repeat', 'std.object.keys', 'std.object.values', 'std.object.entries', 'std.object.merge', 'std.object.assoc', 'std.object.dissoc', 'std.object.pick', 'std.object.omit', 'std.object.prop_eq', 'std.object.where', 'std.fn.compose', 'std.fn.pipe', 'std.fn.identity', 'std.fn.always', 'std.string.replace', 'std.string.pad_left', 'std.string.pad_right', 'std.type.is_null', 'std.type.is_bool', 'std.type.is_number', 'std.type.is_string', 'std.type.is_list', 'std.type.is_dict']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'assert.spec_lang_builtin_surface_sync'}}, 'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
contracts:
  clauses:
  - id: DCGOV-ASSERT-SYNC-005
    title: spec-lang builtin surface remains synced across contract and runners
    purpose: Ensures builtin operators documented in the spec-lang contract are implemented in both Python and PHP runner evaluators.
    asserts:
      imports:
      - from: artifact
        names:
        - violation_count
      checks:
      - id: assert_1
        assert:
          call:
          - var: policy.assert.no_violations
          - std.object.assoc:
            - violation_count
            - var: violation_count
            - lit: {}
      - id: assert_2
        assert:
        - call:
          - var: policy.assert.summary_passed
          - std.object.assoc:
            - summary_json
            - var: summary_json
            - lit: {}
        - call:
          - var: policy.assert.summary_check_id
          - std.object.assoc:
            - summary_json
            - var: summary_json
            - lit: {}
          - assert.spec_lang_builtin_surface_sync
        imports:
        - from: artifact
          names:
          - summary_json
adapters:
- type: legacy.root_spec_lang_builtin_sync_required_ops_std_math_mul_std_math_div_std_math_mod_std_math_pow_std_math_abs_std_math_negate_std_math_inc_std_math_dec_std_math_clamp_std_math_round_std_math_floor_std_math_ceil_std_logic_compare_std_logic_between_std_logic_xor_std_collection_slice_std_collection_reverse_std_collection_zip_std_collection_zip_with_std_math_range_std_collection_repeat_std_object_keys_std_object_values_std_object_entries_std_object_merge_std_object_assoc_std_object_dissoc_std_object_pick_std_object_omit_std_object_prop_eq_std_object_where_std_fn_compose_std_fn_pipe_std_fn_identity_std_fn_always_std_string_replace_std_string_pad_left_std_string_pad_right_std_type_is_null_std_type_is_bool_std_type_is_number_std_type_is_string_std_type_is_list_std_type_is_dict_check_profile_governance_scan_config_check_assert_spec_lang_builtin_surface_sync_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  actions:
  - id: svc.root_spec_lang_builtin_sync_required_ops_std_math_mul_std_math_div_std_math_mod_std_math_pow_std_math_abs_std_math_negate_std_math_inc_std_math_dec_std_math_clamp_std_math_round_std_math_floor_std_math_ceil_std_logic_compare_std_logic_between_std_logic_xor_std_collection_slice_std_collection_reverse_std_collection_zip_std_collection_zip_with_std_math_range_std_collection_repeat_std_object_keys_std_object_values_std_object_entries_std_object_merge_std_object_assoc_std_object_dissoc_std_object_pick_std_object_omit_std_object_prop_eq_std_object_where_std_fn_compose_std_fn_pipe_std_fn_identity_std_fn_always_std_string_replace_std_string_pad_left_std_string_pad_right_std_type_is_null_std_type_is_bool_std_type_is_number_std_type_is_string_std_type_is_list_std_type_is_dict_check_profile_governance_scan_config_check_assert_spec_lang_builtin_surface_sync_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    direction: bidirectional
    profile: default
services:
- id: svc.root_spec_lang_builtin_sync_required_ops_std_math_mul_std_math_div_std_math_mod_std_math_pow_std_math_abs_std_math_negate_std_math_inc_std_math_dec_std_math_clamp_std_math_round_std_math_floor_std_math_ceil_std_logic_compare_std_logic_between_std_logic_xor_std_collection_slice_std_collection_reverse_std_collection_zip_std_collection_zip_with_std_math_range_std_collection_repeat_std_object_keys_std_object_values_std_object_entries_std_object_merge_std_object_assoc_std_object_dissoc_std_object_pick_std_object_omit_std_object_prop_eq_std_object_where_std_fn_compose_std_fn_pipe_std_fn_identity_std_fn_always_std_string_replace_std_string_pad_left_std_string_pad_right_std_type_is_null_std_type_is_bool_std_type_is_number_std_type_is_string_std_type_is_list_std_type_is_dict_check_profile_governance_scan_config_check_assert_spec_lang_builtin_surface_sync_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
  consumes:
  - svc.root_spec_lang_builtin_sync_required_ops_std_math_mul_std_math_div_std_math_mod_std_math_pow_std_math_abs_std_math_negate_std_math_inc_std_math_dec_std_math_clamp_std_math_round_std_math_floor_std_math_ceil_std_logic_compare_std_logic_between_std_logic_xor_std_collection_slice_std_collection_reverse_std_collection_zip_std_collection_zip_with_std_math_range_std_collection_repeat_std_object_keys_std_object_values_std_object_entries_std_object_merge_std_object_assoc_std_object_dissoc_std_object_pick_std_object_omit_std_object_prop_eq_std_object_where_std_fn_compose_std_fn_pipe_std_fn_identity_std_fn_always_std_string_replace_std_string_pad_left_std_string_pad_right_std_type_is_null_std_type_is_bool_std_type_is_number_std_type_is_string_std_type_is_list_std_type_is_dict_check_profile_governance_scan_config_check_assert_spec_lang_builtin_surface_sync_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
```
