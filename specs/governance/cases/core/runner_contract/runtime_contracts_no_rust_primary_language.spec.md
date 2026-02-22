```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUNTIME-CONTRACT-001
  title: contracts avoid rust-primary language
  purpose: Ensures active contracts remain implementation-agnostic.
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
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'contract_language': {'files': ['/specs/contract/10_docs_quality.md',
      '/specs/contract/12_runner_interface.md', '/specs/contract/25_compatibility_matrix.md'],
      'forbidden_tokens': ['implementation-agnostic', 'required lane']}, 'check':
      {'profile': 'governance.scan', 'config': {'check': 'runtime.contracts_no_rust_primary_language'}}}"
services:
  entries:
  - id: 
      svc.root_contract_language_files_specs_contract_10_docs_quality_md_specs_contract_12_runner_interface_md_specs_contract_25_compatibility_matrix_md_forbidden_tokens_implementation_agnostic_required_lane_check_profile_governance_scan_config_check_runtime_contracts_no_rust_primary_language.default.1
    type: 
      legacy.root_contract_language_files_specs_contract_10_docs_quality_md_specs_contract_12_runner_interface_md_specs_contract_25_compatibility_matrix_md_forbidden_tokens_implementation_agnostic_required_lane_check_profile_governance_scan_config_check_runtime_contracts_no_rust_primary_language
    io: io
    profile: default
    config: {}
```
