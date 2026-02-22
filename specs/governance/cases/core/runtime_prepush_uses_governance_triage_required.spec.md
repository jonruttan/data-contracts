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
    - '{''root'': ''.'', ''prepush_governance_triage'': {''path'': ''/scripts/ci_gate.sh'', ''required_tokens'': [''governance-triage'', ''./scripts/governance_triage.sh''], ''forbidden_tokens'': [''run_step governance "${SPEC_RUNNER_BIN}" governance'']}, ''check'': {''profile'': ''governance.scan'', ''config'': {''check'': ''runtime.prepush_uses_governance_triage_required''}}, ''use'': [{''ref'': ''/specs/libraries/policy/policy_assertions.spec.md'', ''as'': ''lib_policy_core_spec'', ''symbols'': [''policy.assert.no_violations'', ''policy.assert.summary_passed'', ''policy.assert.summary_check_id'', ''policy.assert.scan_pass'']}]}'
services:
  actions:
  - id: svc.root_prepush_governance_triage_path_scripts_ci_gate_sh_required_tokens_governance_triage_scripts_governance_triage_sh_forbidden_tokens_run_step_governance_spec_runner_bin_governance_check_profile_governance_scan_config_check_runtime_prepush_uses_governance_triage_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    type: legacy.root_prepush_governance_triage_path_scripts_ci_gate_sh_required_tokens_governance_triage_scripts_governance_triage_sh_forbidden_tokens_run_step_governance_spec_runner_bin_governance_check_profile_governance_scan_config_check_runtime_prepush_uses_governance_triage_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-TRIAGE-002
  title: prepush lane uses governance triage entrypoint
  purpose: Ensures prepush parity lane calls governance triage instead of direct broad governance.
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
