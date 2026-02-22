```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUNTIME-OPS-OS-SURFACE-001
  title: ops.os stdlib symbols are declared in profile and symbol maps
  purpose: Ensures ops.os builtins are synchronized across stdlib mapping and 
    stdlib profile contract surfaces.
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
    - "{'root': '.', 'ops_os_stdlib_surface': {'files': ['/dc-runner-python', '/specs/schema/spec_lang_stdlib_profile_v1.yaml'],
      'required_symbols': ['ops.os.exec', 'ops.os.exec_capture', 'ops.os.env_get',
      'ops.os.env_has', 'ops.os.cwd', 'ops.os.pid', 'ops.os.sleep_ms', 'ops.os.exit_code']},
      'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.ops_os_stdlib_surface_sync'}}}"
services:
  entries:
  - id: 
      svc.root_ops_os_stdlib_surface_files_dc_runner_python_specs_schema_spec_lang_stdlib_profile_v1_yaml_required_symbols_ops_os_exec_ops_os_exec_capture_ops_os_env_get_ops_os_env_has_ops_os_cwd_ops_os_pid_ops_os_sleep_ms_ops_os_exit_code_check_profile_governance_scan_config_check_runtime_ops_os_stdlib_surface_sync.default.1
    type: 
      legacy.root_ops_os_stdlib_surface_files_dc_runner_python_specs_schema_spec_lang_stdlib_profile_v1_yaml_required_symbols_ops_os_exec_ops_os_exec_capture_ops_os_env_get_ops_os_env_has_ops_os_cwd_ops_os_pid_ops_os_sleep_ms_ops_os_exit_code_check_profile_governance_scan_config_check_runtime_ops_os_stdlib_surface_sync
    io: io
    profile: default
    config: {}
```
