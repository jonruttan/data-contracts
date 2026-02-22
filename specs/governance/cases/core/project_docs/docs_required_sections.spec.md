```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'required_sections': {'docs/book/05_what_is_data_contracts.md': ['## System Intent', '## High-Level Architecture', '## Why This Exists'], 'docs/book/15_spec_lifecycle.md': ['## Lifecycle Flow', '## Feedback Loop'], 'docs/book/20_case_model.md': ['## Canonical Top-Level Topology', '## Responsibility Split', '## Contract Form', '## Normative References'], 'docs/book/25_system_topology.md': ['## Component Topology', '## Ownership Topology'], 'docs/book/30_assertion_model.md': ['## Canonical Contract Shape', '## Imports and Precedence', '## Forbidden prior Forms', '## Group Semantics'], 'docs/book/35_usage_guides_index.md': ['## Guide Paths'], 'docs/book/90_reference_guide.md': ['## Normative Sources', '## Guide To Contract Map', '## Generated References'], 'docs/book/guides/index.md': ['## Guide Set'], 'docs/book/guides/guide_01_onboarding.md': ['## Do This Now', '## How To Verify Success', '## Common Failure Signatures'], 'docs/book/guides/guide_02_first_spec_authoring.md': ['## Do This Now', '## How To Verify Success', '## Common Failure Signatures'], 'docs/book/guides/guide_03_running_checks_and_gates.md': ['## Gate Execution Flow', '## Do This Now', '## How To Verify Success', '## Common Failure Signatures'], 'docs/book/guides/guide_04_debugging_failures.md': ['## Troubleshooting Decision Tree', '## Do This Now', '## How To Verify Success', '## Common Failure Signatures'], 'docs/book/guides/guide_05_release_and_change_control.md': ['## Do This Now', '## How To Verify Success', '## Common Failure Signatures'], 'docs/book/guides/guide_06_governance_tuning.md': ['## Governance Decision Path', '## Do This Now', '## How To Verify Success', '## Common Failure Signatures'], 'docs/book/guides/guide_07_schema_extension_workflow.md': ['## Schema Evolution Flow', '## Do This Now', '## How To Verify Success', '## Common Failure Signatures'], 'docs/book/guides/guide_08_ci_integration.md': ['## CI Flow', '## Do This Now', '## How To Verify Success', '## Common Failure Signatures'], 'docs/book/guides/guide_09_status_exchange_operations.md': ['## Status Exchange Flow', '## Do This Now', '## How To Verify Success', '## Common Failure Signatures'], 'docs/book/guides/guide_10_reference_navigation_patterns.md': ['## Do This Now', '## How To Verify Success', '## Common Failure Signatures'], 'docs/book/reference_index.md': ['# Reference Index', 'Canonical order for reference-manual chapters.', 'how to use'], 'docs/book/40_spec_lang_authoring.md': ['## Mapping-AST Rules', '## Readability Patterns', '## Anti-Patterns', '## Library-Backed Reuse'], 'docs/book/60_runner_and_gates.md': ['## required lane', '## Gate Sequence', '## Exit Code Semantics', '## Compatibility (Non-Blocking)'], 'docs/book/80_troubleshooting.md': ['## Failure Taxonomy', '## Deterministic Recovery Flow', '## Escalation']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'docs.required_sections'}}, 'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
services:
  actions:
  - id: svc.root_required_sections_docs_book_05_what_is_data_contracts_md_system_intent_high_level_architecture_why_this_exists_docs_book_15_spec_lifecycle_md_lifecycle_flow_feedback_loop_docs_book_20_case_model_md_canonical_top_level_topology_responsibility_split_contract_form_normative_references_docs_book_25_system_topology_md_component_topology_ownership_topology_docs_book_30_assertion_model_md_canonical_contract_shape_imports_and_precedence_forbidden_prior_forms_group_semantics_docs_book_35_usage_guides_index_md_guide_paths_docs_book_90_reference_guide_md_normative_sources_guide_to_contract_map_generated_references_docs_book_guides_index_md_guide_set_docs_book_guides_guide_01_onboarding_md_do_this_now_how_to_verify_success_common_failure_signatures_docs_book_guides_guide_02_first_spec_authoring_md_do_this_now_how_to_verify_success_common_failure_signatures_docs_book_guides_guide_03_running_checks_and_gates_md_gate_execution_flow_do_this_now_how_to_verify_success_common_failure_signatures_docs_book_guides_guide_04_debugging_failures_md_troubleshooting_decision_tree_do_this_now_how_to_verify_success_common_failure_signatures_docs_book_guides_guide_05_release_and_change_control_md_do_this_now_how_to_verify_success_common_failure_signatures_docs_book_guides_guide_06_governance_tuning_md_governance_decision_path_do_this_now_how_to_verify_success_common_failure_signatures_docs_book_guides_guide_07_schema_extension_workflow_md_schema_evolution_flow_do_this_now_how_to_verify_success_common_failure_signatures_docs_book_guides_guide_08_ci_integration_md_ci_flow_do_this_now_how_to_verify_success_common_failure_signatures_docs_book_guides_guide_09_status_exchange_operations_md_status_exchange_flow_do_this_now_how_to_verify_success_common_failure_signatures_docs_book_guides_guide_10_reference_navigation_patterns_md_do_this_now_how_to_verify_success_common_failure_signatures_docs_book_reference_index_md_reference_index_canonical_order_for_reference_manual_chapters_how_to_use_docs_book_40_spec_lang_authoring_md_mapping_ast_rules_readability_patterns_anti_patterns_library_backed_reuse_docs_book_60_runner_and_gates_md_required_lane_gate_sequence_exit_code_semantics_compatibility_non_blocking_docs_book_80_troubleshooting_md_failure_taxonomy_deterministic_recovery_flow_escalation_check_profile_governance_scan_config_check_docs_required_sections_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    type: legacy.root_required_sections_docs_book_05_what_is_data_contracts_md_system_intent_high_level_architecture_why_this_exists_docs_book_15_spec_lifecycle_md_lifecycle_flow_feedback_loop_docs_book_20_case_model_md_canonical_top_level_topology_responsibility_split_contract_form_normative_references_docs_book_25_system_topology_md_component_topology_ownership_topology_docs_book_30_assertion_model_md_canonical_contract_shape_imports_and_precedence_forbidden_prior_forms_group_semantics_docs_book_35_usage_guides_index_md_guide_paths_docs_book_90_reference_guide_md_normative_sources_guide_to_contract_map_generated_references_docs_book_guides_index_md_guide_set_docs_book_guides_guide_01_onboarding_md_do_this_now_how_to_verify_success_common_failure_signatures_docs_book_guides_guide_02_first_spec_authoring_md_do_this_now_how_to_verify_success_common_failure_signatures_docs_book_guides_guide_03_running_checks_and_gates_md_gate_execution_flow_do_this_now_how_to_verify_success_common_failure_signatures_docs_book_guides_guide_04_debugging_failures_md_troubleshooting_decision_tree_do_this_now_how_to_verify_success_common_failure_signatures_docs_book_guides_guide_05_release_and_change_control_md_do_this_now_how_to_verify_success_common_failure_signatures_docs_book_guides_guide_06_governance_tuning_md_governance_decision_path_do_this_now_how_to_verify_success_common_failure_signatures_docs_book_guides_guide_07_schema_extension_workflow_md_schema_evolution_flow_do_this_now_how_to_verify_success_common_failure_signatures_docs_book_guides_guide_08_ci_integration_md_ci_flow_do_this_now_how_to_verify_success_common_failure_signatures_docs_book_guides_guide_09_status_exchange_operations_md_status_exchange_flow_do_this_now_how_to_verify_success_common_failure_signatures_docs_book_guides_guide_10_reference_navigation_patterns_md_do_this_now_how_to_verify_success_common_failure_signatures_docs_book_reference_index_md_reference_index_canonical_order_for_reference_manual_chapters_how_to_use_docs_book_40_spec_lang_authoring_md_mapping_ast_rules_readability_patterns_anti_patterns_library_backed_reuse_docs_book_60_runner_and_gates_md_required_lane_gate_sequence_exit_code_semantics_compatibility_non_blocking_docs_book_80_troubleshooting_md_failure_taxonomy_deterministic_recovery_flow_escalation_check_profile_governance_scan_config_check_docs_required_sections_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
    io: io
    profile: default
contracts:
- id: DCGOV-DOCS-REF-003
  title: key reference chapters include required sections
  purpose: Keeps the core reference pages structurally complete by requiring stable section tokens for author and implementer workflows.
  clauses:
    imports:
    - from: artifact
      names:
      - violation_count
    predicates:
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
        - docs.required_sections
      imports:
      - from: artifact
        names:
        - summary_json
```
