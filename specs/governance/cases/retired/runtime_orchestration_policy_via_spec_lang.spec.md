```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUNTIME-ORCH-001
  title: gate orchestration verdict is policy-driven via spec-lang
  purpose: Ensures CI gate summary determines final verdict from assert-derived 
    step statuses without evaluate expressions.
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
    - id: assert_2
      assert:
      - std.logic.eq:
        - std.object.get:
          - var: summary_json
          - passed
        - true
      - std.logic.eq:
        - std.object.get:
          - var: summary_json
          - check_id
        - runtime.orchestration_policy_via_spec_lang
      imports:
      - from: artifact
        names:
        - summary_json
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'orchestration_policy': {'files': [{'path': '/dc-runner-python',
      'required_tokens': ['_evaluate_gate_policy(', 'all(str(row.get(\"status\", \"\
      \")) == \"pass\"', 'policy_verdict']}, {'path': '/specs/governance/cases/core/runtime_orchestration_policy_via_spec_lang.spec.md',
      'required_tokens': ['runtime.orchestration_policy_via_spec_lang', '_evaluate_gate_policy(']}],
      'forbidden_tokens': []}, 'check': {'profile': 'governance.scan', 'config': {'check':
      'runtime.orchestration_policy_via_spec_lang'}}, 'use': [{'ref': '/specs/libraries/policy/policy_core.spec.md',
      'as': 'lib_policy_core_spec', 'symbols': ['policy.pass_when_no_violations']}]}"
services:
  entries:
  - id: 
      svc.root_orchestration_policy_files_path_dc_runner_python_required_tokens_evaluate_gate_policy_all_str_row_get_status_pass_policy_verdict_path_specs_governance_cases_core_runtime_orchestration_policy_via_spec_lang_spec_md_required_tokens_runtime_orchestration_policy_via_spec_lang_evaluate_gate_policy_forbidden_tokens_check_profile_governance_scan_config_check_runtime_orchestration_policy_via_spec_lang_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: 
      legacy.root_orchestration_policy_files_path_dc_runner_python_required_tokens_evaluate_gate_policy_all_str_row_get_status_pass_policy_verdict_path_specs_governance_cases_core_runtime_orchestration_policy_via_spec_lang_spec_md_required_tokens_runtime_orchestration_policy_via_spec_lang_evaluate_gate_policy_forbidden_tokens_check_profile_governance_scan_config_check_runtime_orchestration_policy_via_spec_lang_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
    config: {}
    default: true
```
