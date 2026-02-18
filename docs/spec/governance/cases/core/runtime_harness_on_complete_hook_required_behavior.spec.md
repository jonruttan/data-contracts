# Governance Cases

## SRGOV-RUNTIME-HOOKS-004

```yaml contract-spec
id: SRGOV-RUNTIME-HOOKS-004
title: harness.when complete hook must run after successful contract
purpose: Ensures complete hook dispatch is explicit and ordered after clause pass handling.
type: governance.check
check: runtime.harness_on_complete_hook_required_behavior
harness:
  root: .
  harness_on_complete:
    path: /spec_runner/components/assertion_engine.py
    required_tokens:
    - "def _on_complete"
    - "\"complete\""
    - "on_complete=_on_complete"
contract:
- id: assert_1
  class: must
  target: violation_count
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
```
