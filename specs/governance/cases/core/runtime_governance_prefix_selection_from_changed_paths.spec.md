```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - '{''root'': ''.'', ''triage_prefix_selection'': {''path'': ''/scripts/governance_triage.sh'',
      ''required_tokens'': [''collect_changed_paths'', ''select_prefixes_from_changed_paths'',
      ''selection_source="changed_paths"'', ''CHECK_PREFIXES'']}, ''check'': {''profile'':
      ''governance.scan'', ''config'': {''check'': ''runtime.governance_prefix_selection_from_changed_paths''}},
      ''use'': [{''ref'': ''/specs/libraries/policy/policy_assertions.spec.md'', ''as'':
      ''lib_policy_core_spec'', ''symbols'': [''policy.assert.no_violations'', ''policy.assert.summary_passed'',
      ''policy.assert.summary_check_id'', ''policy.assert.scan_pass'']}]}'
services:
- type: legacy.root_triage_prefix_selection_path_scripts_governance_triage_sh_required_tokens_collect_changed_paths_select_prefixes_from_changed_paths_selection_source_changed_paths_check_prefixes_check_profile_governance_scan_config_check_runtime_governance_prefix_selection_from_changed_paths_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  operations:
  - id: svc.root_triage_prefix_selection_path_scripts_governance_triage_sh_required_tokens_collect_changed_paths_select_prefixes_from_changed_paths_selection_source_changed_paths_check_prefixes_check_profile_governance_scan_config_check_runtime_governance_prefix_selection_from_changed_paths_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    mode: default
    direction: bidirectional
contracts:
  defaults:
    type: contract.check
  clauses:
  - id: DCGOV-RUNTIME-TRIAGE-011
    title: governance triage selects prefixes from changed paths
    purpose: Ensures triage auto mode derives targeted check prefixes from changed
      paths before fallback prefixes.
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
