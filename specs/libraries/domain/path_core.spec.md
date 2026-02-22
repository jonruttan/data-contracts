```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.export
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - '{''exports'': [{''as'': ''domain.file.has_ext'', ''from'': ''assert.function'', ''path'': ''/__export__domain.file.has_ext'', ''params'': [''meta'', ''ext''], ''required'': True, ''docs'': [{''id'': ''domain.file.has_ext.doc.1'', ''summary'': ''Contract export for `domain.file.has_ext`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  meta: "<meta>"\n  ext: "<ext>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\n- params: - name: meta\n  type: any\n  required: true\n  description: Input parameter `meta`.\n- name: ext\n  type: any\n  required: true\n  description: Input parameter `ext`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.file.is_existing_dir'', ''from'': ''assert.function'', ''path'': ''/__export__domain.file.is_existing_dir'', ''params'': [''meta''], ''required'': True, ''docs'': [{''id'': ''domain.file.is_existing_dir.doc.1'', ''summary'': ''Contract export for `domain.file.is_existing_dir`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  meta: "<meta>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\n- params: - name: meta\n  type: any\n  required: true\n  description: Input parameter `meta`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\ nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.file.is_existing_file'', ''from'': ''assert.function'', ''path'': ''/__export__domain.file.is_existing_file'', ''params'': [''meta''], ''required'': True, ''docs'': [{''id'': ''domain.file.is_existing_file.doc.1'', ''summary'': ''Contract export for `domain.file.is_existing_file`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  meta: "<meta>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\n- params: - name: meta\n  type: any\n  required: true\n  description: Input parameter `meta`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\ nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.file.name'', ''from'': ''assert.function'', ''path'': ''/__export__domain.file.name'', ''params'': [''meta''], ''required'': True, ''docs'': [{''id'': ''domain.file.name.doc.1'', ''summary'': ''Contract export for `domain.file.name`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  meta: "<meta>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\ n- params: - name: meta\n  type: any\n  required: true\n  description: Input parameter `meta`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\ nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.path.eq'', ''from'': ''assert.function'', ''path'': ''/__export__domain.path.eq'', ''params'': [''left'', ''right''], ''required'': True, ''docs'': [{''id'': ''domain.path.eq.doc.1'', ''summary'': ''Contract export for `domain.path.eq`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  left: "<left>"\n  right: "<right>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\n- params: - name: left\n  type: any\n  required: true\n  description: Input parameter `left`.\n- name: right\n  type: any\n  required: true\n  description: Input parameter `right`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.path.is_in_docs'', ''from'': ''assert.function'', ''path'': ''/__export__domain.path.is_in_docs'', ''params'': [''path''], ''required'': True, ''docs'': [{''id'': ''domain.path.is_in_docs.doc.1'', ''summary'': ''Contract export for `domain.path.is_in_docs`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: "<path>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\ n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\ nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.path.is_spec_md'', ''from'': ''assert.function'', ''path'': ''/__export__domain.path.is_spec_md'', ''params'': [''path''], ''required'': True, ''docs'': [{''id'': ''domain.path.is_spec_md.doc.1'', ''summary'': ''Contract export for `domain.path.is_spec_md`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: "<path>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\ n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\ nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.path.normalize'', ''from'': ''assert.function'', ''path'': ''/__export__domain.path.normalize'', ''params'': [''path''], ''required'': True, ''docs'': [{''id'': ''domain.path.normalize.doc.1'', ''summary'': ''Contract export for `domain.path.normalize`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: "<path>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\ n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\ nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
    - '{''exports'': [{''as'': ''domain.path.sorted'', ''from'': ''assert.function'', ''path'': ''/__export__domain.path.sorted'', ''params'': [''paths''], ''required'': True, ''docs'': [{''id'': ''domain.path.sorted.doc.1'', ''summary'': ''Contract export for `domain.path.sorted`.'', ''audience'': ''spec-authors'', ''status'': ''active'', ''description'': ''Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  paths: "<paths>"\nexpected: "<result>"\nnotes: Replace with a concrete scenario.\ n- params: - name: paths\n  type: any\n  required: true\n  description: Input parameter `paths`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats.'', ''since'': ''v1''}]}]}'
services:
  defaults:
    profile: default
  entries:
  - id: svc.exports_as_domain_path_normalize_from_assert_function_path_export_domain_path_normalize_params_path_required_true_docs_id_domain_path_normalize_doc_1_summary_contract_export_for_domain_path_normalize_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_path_normalize_from_assert_function_path_export_domain_path_normalize_params_path_required_true_docs_id_domain_path_normalize_doc_1_summary_contract_export_for_domain_path_normalize_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_path_eq_from_assert_function_path_export_domain_path_eq_params_left_right_required_true_docs_id_domain_path_eq_doc_1_summary_contract_export_for_domain_path_eq_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_left_left_n_right_right_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_left_n_type_any_n_required_true_n_description_input_parameter_left_n_name_right_n_type_any_n_required_true_n_description_input_parameter_right_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_path_eq_from_assert_function_path_export_domain_path_eq_params_left_right_required_true_docs_id_domain_path_eq_doc_1_summary_contract_export_for_domain_path_eq_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_left_left_n_right_right_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_left_n_type_any_n_required_true_n_description_input_parameter_left_n_name_right_n_type_any_n_required_true_n_description_input_parameter_right_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_path_is_spec_md_from_assert_function_path_export_domain_path_is_spec_md_params_path_required_true_docs_id_domain_path_is_spec_md_doc_1_summary_contract_export_for_domain_path_is_spec_md_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_path_is_spec_md_from_assert_function_path_export_domain_path_is_spec_md_params_path_required_true_docs_id_domain_path_is_spec_md_doc_1_summary_contract_export_for_domain_path_is_spec_md_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_path_is_in_docs_from_assert_function_path_export_domain_path_is_in_docs_params_path_required_true_docs_id_domain_path_is_in_docs_doc_1_summary_contract_export_for_domain_path_is_in_docs_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_path_is_in_docs_from_assert_function_path_export_domain_path_is_in_docs_params_path_required_true_docs_id_domain_path_is_in_docs_doc_1_summary_contract_export_for_domain_path_is_in_docs_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_path_path_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_path_n_type_any_n_required_true_n_description_input_parameter_path_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_path_sorted_from_assert_function_path_export_domain_path_sorted_params_paths_required_true_docs_id_domain_path_sorted_doc_1_summary_contract_export_for_domain_path_sorted_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_paths_paths_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_paths_n_type_any_n_required_true_n_description_input_parameter_paths_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_path_sorted_from_assert_function_path_export_domain_path_sorted_params_paths_required_true_docs_id_domain_path_sorted_doc_1_summary_contract_export_for_domain_path_sorted_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_paths_paths_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_paths_n_type_any_n_required_true_n_description_input_parameter_paths_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_file_is_existing_file_from_assert_function_path_export_domain_file_is_existing_file_params_meta_required_true_docs_id_domain_file_is_existing_file_doc_1_summary_contract_export_for_domain_file_is_existing_file_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_meta_meta_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_meta_n_type_any_n_required_true_n_description_input_parameter_meta_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_file_is_existing_file_from_assert_function_path_export_domain_file_is_existing_file_params_meta_required_true_docs_id_domain_file_is_existing_file_doc_1_summary_contract_export_for_domain_file_is_existing_file_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_meta_meta_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_meta_n_type_any_n_required_true_n_description_input_parameter_meta_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_file_is_existing_dir_from_assert_function_path_export_domain_file_is_existing_dir_params_meta_required_true_docs_id_domain_file_is_existing_dir_doc_1_summary_contract_export_for_domain_file_is_existing_dir_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_meta_meta_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_meta_n_type_any_n_required_true_n_description_input_parameter_meta_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_file_is_existing_dir_from_assert_function_path_export_domain_file_is_existing_dir_params_meta_required_true_docs_id_domain_file_is_existing_dir_doc_1_summary_contract_export_for_domain_file_is_existing_dir_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_meta_meta_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_meta_n_type_any_n_required_true_n_description_input_parameter_meta_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_file_has_ext_from_assert_function_path_export_domain_file_has_ext_params_meta_ext_required_true_docs_id_domain_file_has_ext_doc_1_summary_contract_export_for_domain_file_has_ext_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_meta_meta_n_ext_ext_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_meta_n_type_any_n_required_true_n_description_input_parameter_meta_n_name_ext_n_type_any_n_required_true_n_description_input_parameter_ext_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_file_has_ext_from_assert_function_path_export_domain_file_has_ext_params_meta_ext_required_true_docs_id_domain_file_has_ext_doc_1_summary_contract_export_for_domain_file_has_ext_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_meta_meta_n_ext_ext_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_meta_n_type_any_n_required_true_n_description_input_parameter_meta_n_name_ext_n_type_any_n_required_true_n_description_input_parameter_ext_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
  - id: svc.exports_as_domain_file_name_from_assert_function_path_export_domain_file_name_params_meta_required_true_docs_id_domain_file_name_doc_1_summary_contract_export_for_domain_file_name_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_meta_meta_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_meta_n_type_any_n_required_true_n_description_input_parameter_meta_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: legacy.exports_as_domain_file_name_from_assert_function_path_export_domain_file_name_params_meta_required_true_docs_id_domain_file_name_doc_1_summary_contract_export_for_domain_file_name_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_meta_meta_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_meta_n_type_any_n_required_true_n_description_input_parameter_meta_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
contracts:
- id: LIB-DOMAIN-PATH-001-001-DOMAIN-PATH-NORMALIZE
  docs:
  - summary: Case `LIB-DOMAIN-PATH-001-001-DOMAIN-PATH-NORMALIZE` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.path.normalize
      assert:
        ops.fs.path.normalize:
        - var: path
  library:
    id: domain.path.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-PATH-001-002-DOMAIN-PATH-EQ
  docs:
  - summary: Case `LIB-DOMAIN-PATH-001-002-DOMAIN-PATH-EQ` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.path.eq
      assert:
        std.logic.eq:
        - ops.fs.path.normalize:
          - var: left
        - ops.fs.path.normalize:
          - var: right
  library:
    id: domain.path.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-PATH-001-003-DOMAIN-PATH-IS-SPEC-MD
  docs:
  - summary: Case `LIB-DOMAIN-PATH-001-003-DOMAIN-PATH-IS-SPEC-MD` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.path.is_spec_md
      assert:
        std.string.ends_with:
        - ops.fs.path.normalize:
          - var: path
        - ".spec.md"
  library:
    id: domain.path.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-PATH-001-004-DOMAIN-PATH-IS-IN-DOCS
  docs:
  - summary: Case `LIB-DOMAIN-PATH-001-004-DOMAIN-PATH-IS-IN-DOCS` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.path.is_in_docs
      assert:
        ops.fs.path.within:
        - "/docs"
        - ops.fs.path.normalize:
          - var: path
  library:
    id: domain.path.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-PATH-001-005-DOMAIN-PATH-SORTED
  docs:
  - summary: Case `LIB-DOMAIN-PATH-001-005-DOMAIN-PATH-SORTED` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.path.sorted
      assert:
        ops.fs.path.sort:
        - var: paths
  library:
    id: domain.path.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-PATH-001-006-DOMAIN-FILE-IS-EXISTING-FILE
  docs:
  - summary: Case `LIB-DOMAIN-PATH-001-006-DOMAIN-FILE-IS-EXISTING-FILE` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.file.is_existing_file
      assert:
        std.logic.and:
        - ops.fs.file.exists:
          - var: meta
        - ops.fs.file.is_file:
          - var: meta
  library:
    id: domain.path.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-PATH-001-007-DOMAIN-FILE-IS-EXISTING-DIR
  docs:
  - summary: Case `LIB-DOMAIN-PATH-001-007-DOMAIN-FILE-IS-EXISTING-DIR` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.file.is_existing_dir
      assert:
        std.logic.and:
        - ops.fs.file.exists:
          - var: meta
        - ops.fs.file.is_dir:
          - var: meta
  library:
    id: domain.path.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-PATH-001-008-DOMAIN-FILE-HAS-EXT
  docs:
  - summary: Case `LIB-DOMAIN-PATH-001-008-DOMAIN-FILE-HAS-EXT` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.file.has_ext
      assert:
        ops.fs.path.has_ext:
        - ops.fs.file.path:
          - var: meta
        - var: ext
  library:
    id: domain.path.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
- id: LIB-DOMAIN-PATH-001-009-DOMAIN-FILE-NAME
  docs:
  - summary: Case `LIB-DOMAIN-PATH-001-009-DOMAIN-FILE-NAME` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
  clauses:
    predicates:
    - id: __export__domain.file.name
      assert:
        ops.fs.file.name:
        - var: meta
  library:
    id: domain.path.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
```








