```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-HOOKS-004
    title: when complete hook must run after successful contract
    purpose: Ensures complete hook dispatch is explicit and ordered after clause pass handling.
    harness:
      root: .
      when_complete:
        path: /dc-runner-python
        required_tokens:
        - def _on_complete
        - '"complete"'
        - on_complete=_on_complete
      check:
        profile: governance.scan
        config:
          check: runtime.when_complete_hook_required_behavior
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
