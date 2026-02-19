# Governance Cases

## SRGOV-RUNTIME-HOOKS-003

```yaml contract-spec
id: SRGOV-RUNTIME-HOOKS-003
title: when fail hook must run once on first failure
purpose: Ensures fail hook guard and fail-handler token behavior are present.
type: contract.check
harness:
  root: .
  when_fail:
    path: /runners/python/spec_runner/components/assertion_engine.py
    required_tokens:
    - fail_hook_ran
    - if fail_hook_ran
    - runtime.on_hook.fail_handler_failed
    - '"fail"'
  check:
    profile: governance.scan
    config:
      check: runtime.when_fail_hook_required_behavior
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    'on': violation_count
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
```
