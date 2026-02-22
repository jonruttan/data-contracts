```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUNTIME-ENTRY-002
  title: public runner defaults to rust mode
  purpose: Ensures the canonical runner launcher targets the rust runtime lane 
    and forbids python runtime dispatch.
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
        - runtime.public_runner_default_rust
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
    - "{'root': '.', 'public_runner_default': {'path': '/scripts/runner_bin.sh', 'required_tokens':
      ['dc-runner-rust', 'unsupported platform', 'dc-runner-rust release artifact'],
      'forbidden_tokens': ['dc-runner-python']}, 'check': {'profile': 'governance.scan',
      'config': {'check': 'runtime.public_runner_default_rust'}}, 'use': [{'ref':
      '/specs/libraries/policy/policy_core.spec.md', 'as': 'lib_policy_core_spec',
      'symbols': ['policy.pass_when_no_violations']}]}"
services:
  entries:
  - id: 
      svc.root_public_runner_default_path_scripts_runner_bin_sh_required_tokens_dc_runner_rust_unsupported_platform_dc_runner_rust_release_artifact_forbidden_tokens_dc_runner_python_check_profile_governance_scan_config_check_runtime_public_runner_default_rust_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: 
      legacy.root_public_runner_default_path_scripts_runner_bin_sh_required_tokens_dc_runner_rust_unsupported_platform_dc_runner_rust_release_artifact_forbidden_tokens_dc_runner_python_check_profile_governance_scan_config_check_runtime_public_runner_default_rust_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
    config: {}
```
