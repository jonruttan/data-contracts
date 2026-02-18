# Governance Cases

## SRGOV-RUNTIME-HOOKS-002

```yaml contract-spec
id: SRGOV-RUNTIME-HOOKS-002
title: when class hook ordering contract required
purpose: Ensures class hooks run only after successful clause pass and before complete.
type: governance.check
check: runtime.harness_on_ordering_contract_required
harness:
  root: .
  harness_on_ordering:
    path: /spec_runner/components/assertion_engine.py
    required_tokens:
    - def _on_clause_pass
    - 'event_map = {"MUST": "must", "MAY": "can", "MUST_NOT": "cannot"}'
    - event = event_map.get(cls)
    - _run_event(
    - def _on_complete
    - '"complete"'
contract:
- id: assert_1
  class: MUST
  target: violation_count
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
```
