# Governance Cases

## DCGOV-RUNTIME-HOOKS-004

```yaml contract-spec
id: DCGOV-RUNTIME-HOOKS-004
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: when complete hook must run after successful contract
purpose: Ensures complete hook dispatch is explicit and ordered after clause pass handling.
type: contract.check
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
contract:
  defaults: {}
  imports:
  - from: artifact
    names:
    - violation_count
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: violation_count}
      - 0
```
