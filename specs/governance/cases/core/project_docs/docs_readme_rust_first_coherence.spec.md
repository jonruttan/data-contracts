```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-DOCS-REF-010
  title: readme remains implementation-agnostic and canonical for v1 authoring
  purpose: Ensures root README stays gateway-oriented, implementation-agnostic, 
    and free from prior assertion-surface snippets.
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
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'readme_coherence': {'path': '/README.md', 'required_tokens':
      ['./scripts/control_plane.sh critical-gate', './scripts/control_plane.sh governance',
      './scripts/control_plane.sh docs-generate-check', 'Compatibility Matrix (Non-Blocking)',
      'compatibility_non_blocking', 'SPEC_PREPUSH_BYPASS=1 git push'], 'required_paths':
      ['/docs/book/index.md', '/docs/book/99_generated_reference_index.md', '/specs/schema/schema_v2.md',
      '/specs/contract/index.md', '/specs/contract/25_compatibility_matrix.md'], 'forbidden_tokens':
      ['target:', \"'on':\", 'asserts:', 'evaluate wrapper']}, 'check': {'profile':
      'governance.scan', 'config': {'check': 'docs.readme_rust_first_coherence'}},
      'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec',
      'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id',
      'policy.assert.scan_pass']}]}"
services:
  entries:
  - id: 
      svc.root_readme_coherence_path_readme_md_required_tokens_scripts_control_plane_sh_critical_gate_scripts_control_plane_sh_governance_scripts_control_plane_sh_docs_generate_check_compatibility_matrix_non_blocking_compatibility_non_blocking_spec_prepush_bypass_1_git_push_required_paths_docs_book_index_md_docs_book_99_generated_reference_index_md_specs_schema_schema_v2_md_specs_contract_index_md_specs_contract_25_compatibility_matrix_md_forbidden_tokens_target_on_asserts_evaluate_wrapper_check_profile_governance_scan_config_check_docs_readme_rust_first_coherence_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    type: 
      legacy.root_readme_coherence_path_readme_md_required_tokens_scripts_control_plane_sh_critical_gate_scripts_control_plane_sh_governance_scripts_control_plane_sh_docs_generate_check_compatibility_matrix_non_blocking_compatibility_non_blocking_spec_prepush_bypass_1_git_push_required_paths_docs_book_index_md_docs_book_99_generated_reference_index_md_specs_schema_schema_v2_md_specs_contract_index_md_specs_contract_25_compatibility_matrix_md_forbidden_tokens_target_on_asserts_evaluate_wrapper_check_profile_governance_scan_config_check_docs_readme_rust_first_coherence_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
    io: io
    profile: default
    config: {}
```
