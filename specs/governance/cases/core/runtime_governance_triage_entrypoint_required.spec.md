```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'governance_triage': {'path': '/scripts/governance_triage.sh', 'required_tokens': ['--mode auto', '--mode auto|targeted|broad-first', '--from-failures', '--check-prefix', '--check-id', '.artifacts/governance-triage.json', '.artifacts/governance-triage-summary.md']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.governance_triage_entrypoint_required'}}, 'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
contracts:
  clauses:
  - id: DCGOV-RUNTIME-TRIAGE-001
    title: governance triage entrypoint exists with required surface
    purpose: Ensures canonical governance triage script exists and exposes required flags.
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
- type: legacy.root_governance_triage_path_scripts_governance_triage_sh_required_tokens_mode_auto_mode_auto_targeted_broad_first_from_failures_check_prefix_check_id_artifacts_governance_triage_json_artifacts_governance_triage_summary_md_check_profile_governance_scan_config_check_runtime_governance_triage_entrypoint_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  actions:
  - id: svc.root_governance_triage_path_scripts_governance_triage_sh_required_tokens_mode_auto_mode_auto_targeted_broad_first_from_failures_check_prefix_check_id_artifacts_governance_triage_json_artifacts_governance_triage_summary_md_check_profile_governance_scan_config_check_runtime_governance_triage_entrypoint_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    direction: bidirectional
    profile: default
services:
- id: svc.root_governance_triage_path_scripts_governance_triage_sh_required_tokens_mode_auto_mode_auto_targeted_broad_first_from_failures_check_prefix_check_id_artifacts_governance_triage_json_artifacts_governance_triage_summary_md_check_profile_governance_scan_config_check_runtime_governance_triage_entrypoint_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
  consumes:
  - svc.root_governance_triage_path_scripts_governance_triage_sh_required_tokens_mode_auto_mode_auto_targeted_broad_first_from_failures_check_prefix_check_id_artifacts_governance_triage_json_artifacts_governance_triage_summary_md_check_profile_governance_scan_config_check_runtime_governance_triage_entrypoint_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
```
