# Governance Cases

## SRGOV-CHAIN-001

```yaml spec-test
id: SRGOV-CHAIN-001
title: chain references resolve deterministically
purpose: Ensures harness.chain step references resolve by contract for
type: governance.check
check: runtime.chain_reference_resolution
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
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - runtime.chain_reference_resolution
```
