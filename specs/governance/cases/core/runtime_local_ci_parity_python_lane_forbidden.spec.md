```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - '{''root'': ''.'', ''local_ci_parity_python_lane'': {''path'': ''/scripts/ci_gate.sh'', ''required_tokens'': [''MODE="${SPEC_PREPUSH_MODE:-critical}"'', ''mode=critical: rust-only critical path'', ''expected critical|fast''], ''forbidden_tokens'': [''lane_python_parity'', ''--impl python'', ''SPEC_PREPUSH_MODE:-parity'', ''python-governance-triage'']}, ''check'': {''profile'': ''governance.scan'', ''config'': {''check'': ''runtime.local_ci_parity_python_lane_forbidden''}}, ''use'': [{''ref'': ''/specs/libraries/policy/policy_assertions.spec.md'', ''as'': ''lib_policy_core_spec'', ''symbols'': [''policy.assert.no_violations'', ''policy.assert.summary_passed'', ''policy.assert.summary_check_id'', ''policy.assert.scan_pass'']}]}'
services:
- type: legacy.root_local_ci_parity_python_lane_path_scripts_ci_gate_sh_required_tokens_mode_spec_prepush_mode_critical_mode_critical_rust_only_critical_path_expected_critical_fast_forbidden_tokens_lane_python_parity_impl_python_spec_prepush_mode_parity_python_governance_triage_check_profile_governance_scan_config_check_runtime_local_ci_parity_python_lane_forbidden_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  operations:
  - id: svc.root_local_ci_parity_python_lane_path_scripts_ci_gate_sh_required_tokens_mode_spec_prepush_mode_critical_mode_critical_rust_only_critical_path_expected_critical_fast_forbidden_tokens_lane_python_parity_impl_python_spec_prepush_mode_parity_python_governance_triage_check_profile_governance_scan_config_check_runtime_local_ci_parity_python_lane_forbidden_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    mode: default
    direction: bidirectional
contracts:
  clauses:
  - id: DCGOV-RUNTIME-PREPUSH-001
    title: local ci parity script is rust-only
    purpose: Ensures local prepush parity flow contains no python parity lane hooks.
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
