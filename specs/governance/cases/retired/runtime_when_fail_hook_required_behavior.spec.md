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
    - '{''root'': ''.'', ''when_fail'': {''path'': ''/dc-runner-python'', ''required_tokens'':
      [''fail_hook_ran'', ''if fail_hook_ran'', ''runtime.on_hook.fail_handler_failed'',
      ''"fail"'']}, ''check'': {''profile'': ''governance.scan'', ''config'': {''check'':
      ''runtime.when_fail_hook_required_behavior''}}}'
services:
  actions:
  - id: svc.root_when_fail_path_dc_runner_python_required_tokens_fail_hook_ran_if_fail_hook_ran_runtime_on_hook_fail_handler_failed_fail_check_profile_governance_scan_config_check_runtime_when_fail_hook_required_behavior.default.1
    type: legacy.root_when_fail_path_dc_runner_python_required_tokens_fail_hook_ran_if_fail_hook_ran_runtime_on_hook_fail_handler_failed_fail_check_profile_governance_scan_config_check_runtime_when_fail_hook_required_behavior
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-HOOKS-003
  title: when fail hook must run once on first failure
  purpose: Ensures fail hook guard and fail-handler token behavior are present.
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
