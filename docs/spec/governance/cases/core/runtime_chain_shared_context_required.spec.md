# Governance Cases

## SRGOV-CHAIN-011

```yaml spec-test
id: SRGOV-CHAIN-011
title: chain shared context is declared in dispatcher
purpose: Ensures chain state, trace, imports, and chain payload surfaces are carried in shared
  runtime context.
type: governance.check
check: runtime.chain_shared_context_required
harness:
  root: .
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: violation_count
  must:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
```
