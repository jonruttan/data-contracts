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
    - "{'root': '.', 'meta_json_targets': {'files': ['/dc-runner-python', '/dc-runner-python', '/dc-runner-python', '/dc-runner-python', '/dc-runner-python'], 'required_tokens': ['meta_json']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.meta_json_target_required'}}}"
services:
  entries:
  - id: svc.root_meta_json_targets_files_dc_runner_python_dc_runner_python_dc_runner_python_dc_runner_python_dc_runner_python_required_tokens_meta_json_check_profile_governance_scan_config_check_runtime_meta_json_target_required.default.1
    type: legacy.root_meta_json_targets_files_dc_runner_python_dc_runner_python_dc_runner_python_dc_runner_python_dc_runner_python_required_tokens_meta_json_check_profile_governance_scan_config_check_runtime_meta_json_target_required
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-META-TARGET-001
  title: executable harnesses expose meta_json assertion target
  purpose: Ensures all core executable harness adapters project meta_json.
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
