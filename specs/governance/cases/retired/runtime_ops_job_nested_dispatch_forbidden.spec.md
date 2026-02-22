```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUNTIME-JOB-DISPATCH-005
  title: ops.job.dispatch nested dispatch is forbidden
  purpose: Ensures runtime emits deterministic failure token when nested 
    dispatch is attempted.
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
    - "{'root': '.', 'ops_job_nested_dispatch': {'path': '/dc-runner-rust', 'required_tokens':
      ['runtime.dispatch.nested_forbidden']}, 'check': {'profile': 'governance.scan',
      'config': {'check': 'runtime.ops_job_nested_dispatch_forbidden'}}}"
services:
  entries:
  - id: 
      svc.root_ops_job_nested_dispatch_path_dc_runner_rust_required_tokens_runtime_dispatch_nested_forbidden_check_profile_governance_scan_config_check_runtime_ops_job_nested_dispatch_forbidden.default.1
    type: 
      legacy.root_ops_job_nested_dispatch_path_dc_runner_rust_required_tokens_runtime_dispatch_nested_forbidden_check_profile_governance_scan_config_check_runtime_ops_job_nested_dispatch_forbidden
    io: io
    profile: default
    config: {}
```
