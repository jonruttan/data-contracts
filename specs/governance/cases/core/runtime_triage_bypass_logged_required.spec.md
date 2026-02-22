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
    - "{'root': '.', 'triage_bypass_logging': {'path': '/.githooks/pre-push', 'required_tokens': ['SPEC_PREPUSH_BYPASS', 'WARNING: bypass enabled']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.triage_bypass_logged_required'}}, 'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
services:
  entries:
  - id: svc.root_triage_bypass_logging_path_githooks_pre_push_required_tokens_spec_prepush_bypass_warning_bypass_enabled_check_profile_governance_scan_config_check_runtime_triage_bypass_logged_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    type: legacy.root_triage_bypass_logging_path_githooks_pre_push_required_tokens_spec_prepush_bypass_warning_bypass_enabled_check_profile_governance_scan_config_check_runtime_triage_bypass_logged_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-TRIAGE-006
  title: emergency bypass remains explicit and logged
  purpose: Ensures pre-push bypass remains explicit and emits deterministic warning output.
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
