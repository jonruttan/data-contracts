```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - '{''root'': ''.'', ''fast_path_consistency'': {''file_token_sets'': [{''path'':
      ''/scripts/ci_gate.sh'', ''required_tokens'': [''paths_all_in_list "specs/governance/check_sets_v1.yaml"'',
      ''is_fast_path_script_only_change'', ''paths_all_in_list "scripts/ci_gate.sh"
      "scripts/ci_gate.sh"'', ''skip normalize-check (check_sets-only change)'', ''skip
      docs-generate-check (check_sets-only change)'', ''skip normalize-check (gate-script-only
      change)'', ''skip docs-generate-check (gate-script-only change)'']}, {''path'':
      ''/scripts/ci_gate.sh'', ''required_tokens'': [''SPEC_CI_GATE_LOCAL_FAST_PATH'',
      ''only_check_sets_changes'', ''only_gate_script_changes'', ''specs/governance/check_sets_v1.yaml'',
      ''CI:-}'', ''local fast path: check_sets-only change; delegating to ci_gate.sh'',
      ''local fast path: gate-script-only change; delegating to ci_gate.sh'']}, {''path'':
      ''/.githooks/pre-push'', ''required_tokens'': [''is_check_sets_only_change'',
      ''is_gate_script_only_change'', ''specs/governance/check_sets_v1.yaml'', ''scripts/ci_gate.sh'',
      ''scripts/ci_gate.sh'', ''fast path: check_sets-only change'', ''fast path:
      gate-script-only change'', ''make prepush'']}]}, ''check'': {''profile'': ''governance.scan'',
      ''config'': {''check'': ''runtime.fast_path_consistency_required''}}, ''use'':
      [{''ref'': ''/specs/libraries/policy/policy_assertions.spec.md'', ''as'': ''lib_policy_core_spec'',
      ''symbols'': [''policy.assert.no_violations'', ''policy.assert.summary_passed'',
      ''policy.assert.summary_check_id'', ''policy.assert.scan_pass'']}]}'
services:
- type: legacy.root_fast_path_consistency_file_token_sets_path_scripts_ci_gate_sh_required_tokens_paths_all_in_list_specs_governance_check_sets_v1_yaml_is_fast_path_script_only_change_paths_all_in_list_scripts_ci_gate_sh_scripts_ci_gate_sh_skip_normalize_check_check_sets_only_change_skip_docs_generate_check_check_sets_only_change_skip_normalize_check_gate_script_only_change_skip_docs_generate_check_gate_script_only_change_path_scripts_ci_gate_sh_required_tokens_spec_ci_gate_local_fast_path_only_check_sets_changes_only_gate_script_changes_specs_governance_check_sets_v1_yaml_ci_local_fast_path_check_sets_only_change_delegating_to_ci_gate_sh_local_fast_path_gate_script_only_change_delegating_to_ci_gate_sh_path_githooks_pre_push_required_tokens_is_check_sets_only_change_is_gate_script_only_change_specs_governance_check_sets_v1_yaml_scripts_ci_gate_sh_scripts_ci_gate_sh_fast_path_check_sets_only_change_fast_path_gate_script_only_change_make_prepush_check_profile_governance_scan_config_check_runtime_fast_path_consistency_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  operations:
  - id: svc.root_fast_path_consistency_file_token_sets_path_scripts_ci_gate_sh_required_tokens_paths_all_in_list_specs_governance_check_sets_v1_yaml_is_fast_path_script_only_change_paths_all_in_list_scripts_ci_gate_sh_scripts_ci_gate_sh_skip_normalize_check_check_sets_only_change_skip_docs_generate_check_check_sets_only_change_skip_normalize_check_gate_script_only_change_skip_docs_generate_check_gate_script_only_change_path_scripts_ci_gate_sh_required_tokens_spec_ci_gate_local_fast_path_only_check_sets_changes_only_gate_script_changes_specs_governance_check_sets_v1_yaml_ci_local_fast_path_check_sets_only_change_delegating_to_ci_gate_sh_local_fast_path_gate_script_only_change_delegating_to_ci_gate_sh_path_githooks_pre_push_required_tokens_is_check_sets_only_change_is_gate_script_only_change_specs_governance_check_sets_v1_yaml_scripts_ci_gate_sh_scripts_ci_gate_sh_fast_path_check_sets_only_change_fast_path_gate_script_only_change_make_prepush_check_profile_governance_scan_config_check_runtime_fast_path_consistency_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    mode: default
    direction: bidirectional
contracts:
  defaults:
    type: contract.check
  clauses:
  - id: DCGOV-RUNTIME-TRIAGE-023
    title: fast-path consistency is enforced across pre-push and gate scripts
    purpose: Ensures fast-path routing tokens remain aligned across local parity,
      ci gate, and managed pre-push hook.
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
```
