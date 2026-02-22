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
    - "{'root': '.', 'triage_targeted_first': {'path': '/scripts/governance_triage.sh', 'required_tokens': ['TRIAGE_MODE_DEFAULT', 'targeted-first', 'broad-first', 'resolve_targeted_prefixes', 'selection_source']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.governance_triage_targeted_first_required'}}, 'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
services:
  entries:
  - id: svc.root_triage_targeted_first_path_scripts_governance_triage_sh_required_tokens_triage_mode_default_targeted_first_broad_first_resolve_targeted_prefixes_selection_source_check_profile_governance_scan_config_check_runtime_governance_triage_targeted_first_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    type: legacy.root_triage_targeted_first_path_scripts_governance_triage_sh_required_tokens_triage_mode_default_targeted_first_broad_first_resolve_targeted_prefixes_selection_source_check_profile_governance_scan_config_check_runtime_governance_triage_targeted_first_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-TRIAGE-008
  title: governance triage auto mode is targeted-first by default
  purpose: Ensures triage auto mode resolves to targeted-first and exposes broad-first as an explicit mode.
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
