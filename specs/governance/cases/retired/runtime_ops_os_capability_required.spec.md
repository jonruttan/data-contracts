```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUNTIME-OPS-OS-CAP-001
  title: ops.os usage requires explicit capability gate
  purpose: Ensures spec-lang enforces capability.ops_os.required and harness 
    capability parsing.
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
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'ops_os_capability': {'path': '/dc-runner-python', 'required_tokens':
      ['capability.ops_os.required', 'def capabilities_from_harness', 'ops.os.exec']},
      'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.ops_os_capability_required'}}}"
services:
  entries:
  - id: 
      svc.root_ops_os_capability_path_dc_runner_python_required_tokens_capability_ops_os_required_def_capabilities_from_harness_ops_os_exec_check_profile_governance_scan_config_check_runtime_ops_os_capability_required.default.1
    type: 
      legacy.root_ops_os_capability_path_dc_runner_python_required_tokens_capability_ops_os_required_def_capabilities_from_harness_ops_os_exec_check_profile_governance_scan_config_check_runtime_ops_os_capability_required
    io: io
    profile: default
    config: {}
    default: true
```
