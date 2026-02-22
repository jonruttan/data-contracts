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
    - "{'root': '.', 'triage_artifacts': {'files': ['/scripts/governance_triage.sh',
      '/dc-runner-python'], 'required_tokens': ['failing_check_ids', 'failing_check_prefixes']},
      'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.triage_artifacts_emitted_required'}},
      'use': [{'ref': '/specs/libraries/policy/policy_core.spec.md', 'as': 'lib_policy_core_spec',
      'symbols': ['policy.pass_when_no_violations']}]}"
services:
  actions:
  - id: svc.root_triage_artifacts_files_scripts_governance_triage_sh_dc_runner_python_required_tokens_failing_check_ids_failing_check_prefixes_check_profile_governance_scan_config_check_runtime_triage_artifacts_emitted_required_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: legacy.root_triage_artifacts_files_scripts_governance_triage_sh_dc_runner_python_required_tokens_failing_check_ids_failing_check_prefixes_check_profile_governance_scan_config_check_runtime_triage_artifacts_emitted_required_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-TRIAGE-004
  title: triage artifacts are emitted by triage and gate flows
  purpose: Ensures triage artifacts are produced and referenced by governance-triage
    and ci-gate-summary.
  clauses:
    imports:
    - artifact:
      - violation_count
    predicates:
    - id: assert_1
      assert:
        std.logic.eq:
        - var: violation_count
        - 0
```
