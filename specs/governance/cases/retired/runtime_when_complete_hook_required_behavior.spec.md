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
    - '{''root'': ''.'', ''when_complete'': {''path'': ''/dc-runner-python'', ''required_tokens'': [''def _on_complete'', ''"complete"'', ''on_complete=_on_complete'']}, ''check'': {''profile'': ''governance.scan'', ''config'': {''check'': ''runtime.when_complete_hook_required_behavior''}}}'
services:
  actions:
  - id: svc.root_when_complete_path_dc_runner_python_required_tokens_def_on_complete_complete_on_complete_on_complete_check_profile_governance_scan_config_check_runtime_when_complete_hook_required_behavior.default.1
    type: legacy.root_when_complete_path_dc_runner_python_required_tokens_def_on_complete_complete_on_complete_on_complete_check_profile_governance_scan_config_check_runtime_when_complete_hook_required_behavior
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-HOOKS-004
  title: when complete hook must run after successful contract
  purpose: Ensures complete hook dispatch is explicit and ordered after clause pass handling.
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
