```yaml contract-spec
spec_version: 2
schema_ref: "/specs/01_schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'taxonomy_layout': {'required_paths': ['/specs/04_governance/metrics', '/specs/04_governance/tools', '/specs/governance', '/specs/current.md', '/specs/01_schema/index.md', '/specs/02_contracts/index.md'], 'forbidden_paths': ['/specs/metrics', '/specs/tools', '/specs/pending', '/specs/schema.md', '/specs/portable_contract.md']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'spec.taxonomy_hard_cut_required'}}, 'use': [{'ref': '/specs/05_libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
contracts:
  clauses:
  - id: DCGOV-SPEC-TOPO-001
    title: specs taxonomy hard-cut layout is canonical
    purpose: Ensures governance utility domains are folded under `/specs/04_governance/*` and prior root shim paths are removed.
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
adapters:
- type: legacy.root_taxonomy_layout_required_paths_specs_governance_metrics_specs_governance_tools_specs_governance_specs_current_md_specs_schema_index_md_specs_contract_index_md_forbidden_paths_specs_metrics_specs_tools_specs_pending_specs_schema_md_specs_portable_contract_md_check_profile_governance_scan_config_check_spec_taxonomy_hard_cut_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  actions:
  - id: svc.root_taxonomy_layout_required_paths_specs_governance_metrics_specs_governance_tools_specs_governance_specs_current_md_specs_schema_index_md_specs_contract_index_md_forbidden_paths_specs_metrics_specs_tools_specs_pending_specs_schema_md_specs_portable_contract_md_check_profile_governance_scan_config_check_spec_taxonomy_hard_cut_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    direction: bidirectional
    profile: default
services:
- id: svc.root_taxonomy_layout_required_paths_specs_governance_metrics_specs_governance_tools_specs_governance_specs_current_md_specs_schema_index_md_specs_contract_index_md_forbidden_paths_specs_metrics_specs_tools_specs_pending_specs_schema_md_specs_portable_contract_md_check_profile_governance_scan_config_check_spec_taxonomy_hard_cut_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
  consumes:
  - svc.root_taxonomy_layout_required_paths_specs_governance_metrics_specs_governance_tools_specs_governance_specs_current_md_specs_schema_index_md_specs_contract_index_md_forbidden_paths_specs_metrics_specs_tools_specs_pending_specs_schema_md_specs_portable_contract_md_check_profile_governance_scan_config_check_spec_taxonomy_hard_cut_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
```
