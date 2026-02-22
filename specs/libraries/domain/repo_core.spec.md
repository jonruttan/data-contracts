```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.export
contracts:
- id: LIB-DOMAIN-REPO-001-001-DOMAIN-REPO-WALK-MATCHING
  clauses:
    predicates:
    - id: __export__domain.repo.walk_matching
      assert:
        ops.fs.walk:
        - var: root
        - lit:
            pattern:
              var: pattern
            include_dirs: false
            relative: true
  library:
    id: domain.repo.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-REPO-001-001-DOMAIN-REPO-WALK-MATCHING.doc.1
    summary: Case `LIB-DOMAIN-REPO-001-001-DOMAIN-REPO-WALK-MATCHING` for 
      `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored 
      reference text.
    since: v1
    tags:
    - contract.export
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'exports': [{'as': 'domain.repo.walk_matching', 'from': 'assert.function',
      'path': '/__export__domain.repo.walk_matching', 'params': ['root', 'pattern'],
      'required': True, 'docs': [{'id': 'domain.repo.walk_matching.doc.1', 'summary':
      'Contract export for `domain.repo.walk_matching`.', 'audience': 'spec-authors',
      'status': 'active', 'description': 'Auto-generated metadata stub. Replace with
      authored reference text.\\n\\nLegacy doc fields migrated to description:\\n-
      examples[]: title: Basic usage\\ninput:\\n  root: \"<root>\"\\n  pattern: \"\
      <pattern>\"\\nexpected: \"<result>\"\\nnotes: Replace with a concrete scenario.\\
      n- params: - name: root\\n  type: any\\n  required: true\\n  description: Input
      parameter `root`.\\n- name: pattern\\n  type: any\\n  required: true\\n  description:
      Input parameter `pattern`.\\n- returns: type: any\\ndescription: Result payload
      for this symbol.\\n- errors: - code: SCHEMA_ERROR\\n  when: Input payload does
      not satisfy contract shape requirements.\\n  category: schema\\n- portability:
      python: true\\nphp: true\\nrust: true\\nnotes: Confirm per-runtime behavior
      and caveats.', 'since': 'v1'}]}]}"
services:
  entries:
  - id: 
      svc.exports_as_domain_repo_walk_matching_from_assert_function_path_export_domain_repo_walk_matching_params_root_pattern_required_true_docs_id_domain_repo_walk_matching_doc_1_summary_contract_export_for_domain_repo_walk_matching_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_root_root_n_pattern_pattern_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_root_n_type_any_n_required_true_n_description_input_parameter_root_n_name_pattern_n_type_any_n_required_true_n_description_input_parameter_pattern_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1.default.1
    type: 
      legacy.exports_as_domain_repo_walk_matching_from_assert_function_path_export_domain_repo_walk_matching_params_root_pattern_required_true_docs_id_domain_repo_walk_matching_doc_1_summary_contract_export_for_domain_repo_walk_matching_audience_spec_authors_status_active_description_auto_generated_metadata_stub_replace_with_authored_reference_text_n_nlegacy_doc_fields_migrated_to_description_n_examples_title_basic_usage_ninput_n_root_root_n_pattern_pattern_nexpected_result_nnotes_replace_with_a_concrete_scenario_n_params_name_root_n_type_any_n_required_true_n_description_input_parameter_root_n_name_pattern_n_type_any_n_required_true_n_description_input_parameter_pattern_n_returns_type_any_ndescription_result_payload_for_this_symbol_n_errors_code_schema_error_n_when_input_payload_does_not_satisfy_contract_shape_requirements_n_category_schema_n_portability_python_true_nphp_true_nrust_true_nnotes_confirm_per_runtime_behavior_and_caveats_since_v1
    io: io
    profile: default
    config: {}
    default: true
```
