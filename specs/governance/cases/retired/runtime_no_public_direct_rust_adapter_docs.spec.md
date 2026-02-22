```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUNTIME-ENTRY-004
  title: public docs do not instruct direct rust adapter invocation
  purpose: Ensures public docs point to the canonical adapter entrypoint rather 
    than internal rust adapter paths.
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
          - check_id
        - runtime.no_public_direct_rust_adapter_docs
      - std.logic.eq:
        - std.object.get:
          - var: summary_json
          - passed
        - true
      imports:
      - from: artifact
        names:
        - summary_json
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'public_docs': {'files': ['/README.md', '/docs/development.md',
      '/specs/current.md', '/specs/contract/12_runner_interface.md'], 'forbidden_tokens':
      ['dc-runner-rust'], 'allowlist': ['/specs/contract/12_runner_interface.md']},
      'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.no_public_direct_rust_adapter_docs'}},
      'use': [{'ref': '/specs/libraries/policy/policy_core.spec.md', 'as': 'lib_policy_core_spec',
      'symbols': ['policy.pass_when_no_violations']}]}"
services:
  entries:
  - id: 
      svc.root_public_docs_files_readme_md_docs_development_md_specs_current_md_specs_contract_12_runner_interface_md_forbidden_tokens_dc_runner_rust_allowlist_specs_contract_12_runner_interface_md_check_profile_governance_scan_config_check_runtime_no_public_direct_rust_adapter_docs_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: 
      legacy.root_public_docs_files_readme_md_docs_development_md_specs_current_md_specs_contract_12_runner_interface_md_forbidden_tokens_dc_runner_rust_allowlist_specs_contract_12_runner_interface_md_check_profile_governance_scan_config_check_runtime_no_public_direct_rust_adapter_docs_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
    config: {}
    default: true
```
