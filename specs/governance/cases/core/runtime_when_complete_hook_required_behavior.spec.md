# Governance Cases

## SRGOV-RUNTIME-HOOKS-004

```yaml contract-spec
id: SRGOV-RUNTIME-HOOKS-004
title: when complete hook must run after successful contract
purpose: Ensures complete hook dispatch is explicit and ordered after clause pass handling.
type: contract.check
harness:
  root: .
  when_complete:
    path: /spec_runner/components/assertion_engine.py
    required_tokens:
    - def _on_complete
    - '"complete"'
    - on_complete=_on_complete
  check:
    profile: governance.scan
    config:
      check: runtime.when_complete_hook_required_behavior
contract:
- id: assert_1
  class: MUST
  target: violation_count
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
```
