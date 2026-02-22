```yaml contract-spec
spec_version: 2
schema_ref: "/specs/01_schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'release_contract': {'files': ['docs/release_checklist.md'], 'required_tokens': ['Release readiness is defined by executable gates, not manual checklists.', 'make ci-smoke', './scripts/ci_gate.sh', 'convert it into an executable'], 'forbidden_patterns': ['(?m)^##\\\\s+[0-9]+\\\\)', '(?m)^\\\\s*[0-9]+\\\\.\\\\s+(Run|Then|Check|Inspect)\\\\b']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'docs.release_contract_automation_policy'}}, 'use': [{'ref': '/specs/05_libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
contracts:
  clauses:
  - id: DCGOV-DOCS-QUAL-009
    title: release contract forbids manual sequential checklist choreography
    purpose: Ensures release guidance uses executable gate entrypoints and codifies that manual do-X-then-inspect-Y sequences are an anti-pattern.
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
      - id: assert_2
        assert:
        - call:
          - var: policy.assert.summary_passed
          - std.object.assoc:
            - summary_json
            - var: summary_json
            - lit: {}
        - call:
          - var: policy.assert.summary_check_id
          - std.object.assoc:
            - summary_json
            - var: summary_json
            - lit: {}
          - docs.release_contract_automation_policy
        imports:
        - from: artifact
          names:
          - summary_json
adapters:
- type: legacy.root_release_contract_files_docs_release_checklist_md_required_tokens_release_readiness_is_defined_by_executable_gates_not_manual_checklists_make_ci_smoke_scripts_ci_gate_sh_convert_it_into_an_executable_forbidden_patterns_m_s_0_9_m_s_0_9_s_run_then_check_inspect_b_check_profile_governance_scan_config_check_docs_release_contract_automation_policy_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  actions:
  - id: svc.root_release_contract_files_docs_release_checklist_md_required_tokens_release_readiness_is_defined_by_executable_gates_not_manual_checklists_make_ci_smoke_scripts_ci_gate_sh_convert_it_into_an_executable_forbidden_patterns_m_s_0_9_m_s_0_9_s_run_then_check_inspect_b_check_profile_governance_scan_config_check_docs_release_contract_automation_policy_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    direction: bidirectional
    profile: default
services:
- id: svc.root_release_contract_files_docs_release_checklist_md_required_tokens_release_readiness_is_defined_by_executable_gates_not_manual_checklists_make_ci_smoke_scripts_ci_gate_sh_convert_it_into_an_executable_forbidden_patterns_m_s_0_9_m_s_0_9_s_run_then_check_inspect_b_check_profile_governance_scan_config_check_docs_release_contract_automation_policy_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
  consumes:
  - svc.root_release_contract_files_docs_release_checklist_md_required_tokens_release_readiness_is_defined_by_executable_gates_not_manual_checklists_make_ci_smoke_scripts_ci_gate_sh_convert_it_into_an_executable_forbidden_patterns_m_s_0_9_m_s_0_9_s_run_then_check_inspect_b_check_profile_governance_scan_config_check_docs_release_contract_automation_policy_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
```
