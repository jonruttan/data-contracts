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
    - "{'root': '.', 'triage_artifact_selection_metadata': {'path': '/scripts/governance_triage.sh', 'required_tokens': ['selection_source', 'selected_prefixes', 'broad_required', 'governance-triage-summary.md']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.governance_triage_artifact_contains_selection_metadata'}}, 'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
services:
  entries:
  - id: svc.root_triage_artifact_selection_metadata_path_scripts_governance_triage_sh_required_tokens_selection_source_selected_prefixes_broad_required_governance_triage_summary_md_check_profile_governance_scan_config_check_runtime_governance_triage_artifact_contains_selection_metadata_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    type: legacy.root_triage_artifact_selection_metadata_path_scripts_governance_triage_sh_required_tokens_selection_source_selected_prefixes_broad_required_governance_triage_summary_md_check_profile_governance_scan_config_check_runtime_governance_triage_artifact_contains_selection_metadata_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
    io: io
    profile: default
    config: {}
contracts:
- id: DCGOV-RUNTIME-TRIAGE-012
  title: triage artifact includes selection metadata
  purpose: Ensures governance triage artifacts include selection_source and selected_prefixes metadata.
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
```
