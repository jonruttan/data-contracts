```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-HOOKS-003
    title: when fail hook must run once on first failure
    purpose: Ensures fail hook guard and fail-handler token behavior are present.
    harness:
      root: .
      when_fail:
        path: /dc-runner-python
        required_tokens:
        - fail_hook_ran
        - if fail_hook_ran
        - runtime.on_hook.fail_handler_failed
        - '"fail"'
      check:
        profile: governance.scan
        config:
          check: runtime.when_fail_hook_required_behavior
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - violation_count
      predicates:
      - id: assert_1
        assert:
          std.logic.eq:
          - {var: violation_count}
          - 0
```
