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
    - '{''root'': ''.'', ''local_prepush_broad_forbidden'': {''path'': ''/scripts/ci_gate.sh'',
      ''required_tokens'': [''skip broad governance (set SPEC_PREPUSH_REQUIRE_BROAD=1
      to enable)'', ''SPEC_PREPUSH_REQUIRE_BROAD=1''], ''forbidden_tokens'': [''run_step
      governance "${SPEC_RUNNER_BIN}" governance'']}, ''check'': {''profile'': ''governance.scan'',
      ''config'': {''check'': ''runtime.local_prepush_broad_governance_forbidden''}},
      ''use'': [{''ref'': ''/specs/libraries/policy/policy_assertions.spec.md'', ''as'':
      ''lib_policy_core_spec'', ''symbols'': [''policy.assert.no_violations'', ''policy.assert.summary_passed'',
      ''policy.assert.summary_check_id'', ''policy.assert.scan_pass'']}]}'
services:
- id: svc.root_local_prepush_broad_forbidden_path_scripts_ci_gate_sh_required_tokens_skip_broad_governance_set_spec_prepush_require_broad_1_to_enable_spec_prepush_require_broad_1_forbidden_tokens_run_step_governance_spec_runner_bin_governance_check_profile_governance_scan_config_check_runtime_local_prepush_broad_governance_forbidden_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
  type: legacy.root_local_prepush_broad_forbidden_path_scripts_ci_gate_sh_required_tokens_skip_broad_governance_set_spec_prepush_require_broad_1_to_enable_spec_prepush_require_broad_1_forbidden_tokens_run_step_governance_spec_runner_bin_governance_check_profile_governance_scan_config_check_runtime_local_prepush_broad_governance_forbidden_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  mode: default
  direction: bidirectional
contracts:
- id: DCGOV-RUNTIME-TRIAGE-009
  title: local prepush does not require broad governance
  purpose: Ensures local parity flow keeps broad governance out of default prepush
    path.
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
