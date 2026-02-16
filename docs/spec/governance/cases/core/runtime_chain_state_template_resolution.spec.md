# Governance Cases

## SRGOV-CHAIN-005

```yaml spec-test
id: SRGOV-CHAIN-005
title: chain template references resolve against explicit exports
purpose: Ensures api.http chain templates use declared step export names and fail on unresolved
  references.
type: governance.check
check: runtime.chain_state_template_resolution
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
