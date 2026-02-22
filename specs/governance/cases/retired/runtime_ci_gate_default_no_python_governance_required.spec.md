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
    - "{'root': '.', 'ci_gate_default_no_python_governance': {'files': ['/dc-runner-python'], 'required_tokens': ['governance-broad-native', 'governance_broad'], 'forbidden_tokens': []}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.ci_gate_default_no_python_governance_required'}}, 'use': [{'ref': '/specs/libraries/policy/policy_core.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.pass_when_no_violations']}]}"
services:
  entries:
  - id: svc.root_ci_gate_default_no_python_governance_files_dc_runner_python_required_tokens_governance_broad_native_governance_broad_forbidden_tokens_check_profile_governance_scan_config_check_runtime_ci_gate_default_no_python_governance_required_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: legacy.root_ci_gate_default_no_python_governance_files_dc_runner_python_required_tokens_governance_broad_native_governance_broad_forbidden_tokens_check_profile_governance_scan_config_check_runtime_ci_gate_default_no_python_governance_required_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
    config: {}
contracts:
- id: DCGOV-RUNTIME-TRIAGE-015
  title: ci gate default broad governance path is rust-native
  purpose: Ensures ci-gate-summary defaults to governance-broad-native and does not route broad through Python governance scripts.
  clauses:
    imports:
    - from: artifact
      names:
      - violation_count
    predicates:
    - id: assert_1
      assert:
        std.logic.eq:
        - var: violation_count
        - 0
```
