```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUNTIME-HOOKS-002
  title: when class hook ordering contract required
  purpose: Ensures class hooks run only after successful clause pass and before 
    complete.
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
    - "{'root': '.', 'when_ordering': {'path': '/dc-runner-python', 'required_tokens':
      ['def _on_clause_pass', 'event_map = {\"MUST\": \"must\", \"MAY\": \"may\",
      \"MUST_NOT\": \"must_not\"}', 'event = event_map.get(cls)', '_run_event(', 'def
      _on_complete', '\"complete\"']}, 'check': {'profile': 'governance.scan', 'config':
      {'check': 'runtime.when_ordering_contract_required'}}}"
services:
  entries:
  - id: 
      svc.root_when_ordering_path_dc_runner_python_required_tokens_def_on_clause_pass_event_map_must_must_may_may_must_not_must_not_event_event_map_get_cls_run_event_def_on_complete_complete_check_profile_governance_scan_config_check_runtime_when_ordering_contract_required.default.1
    type: 
      legacy.root_when_ordering_path_dc_runner_python_required_tokens_def_on_clause_pass_event_map_must_must_may_may_must_not_must_not_event_event_map_get_cls_run_event_def_on_complete_complete_check_profile_governance_scan_config_check_runtime_when_ordering_contract_required
    io: io
    profile: default
    config: {}
    default: true
```
