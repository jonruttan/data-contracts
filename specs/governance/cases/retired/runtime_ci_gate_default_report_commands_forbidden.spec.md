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
    - "{'root': '.', 'ci_gate_default_reports_forbidden': {'files': ['/dc-runner-python', '/dc-runner-rust'], 'forbidden_tokens': ['spec_portability_json', 'spec_portability_md', 'spec_lang_adoption_json', 'spec_lang_adoption_md', 'runner_independence_json', 'runner_independence_md', 'python_dependency_json', 'python_dependency_md', 'docs_operability_json', 'docs_operability_md', 'contract_assertions_json', 'contract_assertions_md', 'objective_scorecard_json', 'objective_scorecard_md', 'spec_lang_stdlib_json', 'spec_lang_stdlib_md', 'conformance_purpose_json', 'conformance_purpose_md']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.ci_gate_default_report_commands_forbidden'}}, 'use': [{'ref': '/specs/libraries/policy/policy_core.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.pass_when_no_violations']}]}"
services:
  actions:
  - id: svc.root_ci_gate_default_reports_forbidden_files_dc_runner_python_dc_runner_rust_forbidden_tokens_spec_portability_json_spec_portability_md_spec_lang_adoption_json_spec_lang_adoption_md_runner_independence_json_runner_independence_md_python_dependency_json_python_dependency_md_docs_operability_json_docs_operability_md_contract_assertions_json_contract_assertions_md_objective_scorecard_json_objective_scorecard_md_spec_lang_stdlib_json_spec_lang_stdlib_md_conformance_purpose_json_conformance_purpose_md_check_profile_governance_scan_config_check_runtime_ci_gate_default_report_commands_forbidden_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: legacy.root_ci_gate_default_reports_forbidden_files_dc_runner_python_dc_runner_rust_forbidden_tokens_spec_portability_json_spec_portability_md_spec_lang_adoption_json_spec_lang_adoption_md_runner_independence_json_runner_independence_md_python_dependency_json_python_dependency_md_docs_operability_json_docs_operability_md_contract_assertions_json_contract_assertions_md_objective_scorecard_json_objective_scorecard_md_spec_lang_stdlib_json_spec_lang_stdlib_md_conformance_purpose_json_conformance_purpose_md_check_profile_governance_scan_config_check_runtime_ci_gate_default_report_commands_forbidden_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-TRIAGE-016
  title: default ci gate excludes report-generation commands
  purpose: Ensures ci-gate-summary default step list does not include report-generation command invocations.
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
