# Governance Cases

## SRGOV-RUNTIME-HOOKS-003

```yaml contract-spec
id: SRGOV-RUNTIME-HOOKS-003
title: harness.when fail hook must run once on first failure
purpose: Ensures fail hook guard and fail-handler token behavior are present.
type: governance.check
check: runtime.harness_on_fail_hook_required_behavior
harness:
  root: .
  harness_on_fail:
    path: /spec_runner/components/assertion_engine.py
    required_tokens:
    - "fail_hook_ran"
    - "if fail_hook_ran"
    - "runtime.on_hook.fail_handler_failed"
    - "\"fail\""
contract:
- id: assert_1
  class: must
  target: violation_count
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
```
