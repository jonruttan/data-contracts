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
    - "{'root': '.', 'runner_certification_surfaces': {'files': ['/dc-runner-rust', '/dc-runner-rust', '/specs/governance/cases/core/runtime_runner_interface_subcommands.spec.md'], 'required_tokens': ['runner-certify']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.runner_certification_surfaces_sync'}}}"
services:
  actions:
  - id: svc.root_runner_certification_surfaces_files_dc_runner_rust_dc_runner_rust_specs_governance_cases_core_runtime_runner_interface_subcommands_spec_md_required_tokens_runner_certify_check_profile_governance_scan_config_check_runtime_runner_certification_surfaces_sync.default.1
    type: legacy.root_runner_certification_surfaces_files_dc_runner_rust_dc_runner_rust_specs_governance_cases_core_runtime_runner_interface_subcommands_spec_md_required_tokens_runner_certify_check_profile_governance_scan_config_check_runtime_runner_certification_surfaces_sync
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-CERT-002
  title: runner certification command surfaces stay in sync
  purpose: Ensures runner-certify command exists across canonical runtime surfaces.
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
