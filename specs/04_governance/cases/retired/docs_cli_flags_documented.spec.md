```yaml contract-spec
spec_version: 1
schema_ref: "/specs/01_schema/schema_v1.md"
defaults:
  type: contract.check
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'cli_docs': {'python_scripts': ['dc-runner-python'], 'php_scripts': ['dc-runner-php', 'dc-runner-php'], 'python_docs': ['docs/development.md', 'dc-runner-python'], 'php_docs': ['docs/development.md', 'dc-runner-php']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'docs.cli_flags_documented'}}, 'use': [{'ref': '/specs/05_libraries/policy/policy_core.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.pass_when_no_violations']}]}"
services:
  actions:
  - id: svc.root_cli_docs_python_scripts_dc_runner_python_php_scripts_dc_runner_php_dc_runner_php_python_docs_docs_development_md_dc_runner_python_php_docs_docs_development_md_dc_runner_php_check_profile_governance_scan_config_check_docs_cli_flags_documented_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: legacy.root_cli_docs_python_scripts_dc_runner_python_php_scripts_dc_runner_php_dc_runner_php_python_docs_docs_development_md_dc_runner_python_php_docs_docs_development_md_dc_runner_php_check_profile_governance_scan_config_check_docs_cli_flags_documented_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
contracts:
- id: DCGOV-DOCS-REF-005
  title: runner cli flags are documented in development and impl docs
  purpose: Prevents CLI contract drift by requiring script flags to be documented in the development guide and implementation reference pages.
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
        - docs.cli_flags_documented
      imports:
      - artifact:
        - summary_json
```
