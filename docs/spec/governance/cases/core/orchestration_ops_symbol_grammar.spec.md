# Governance Cases

## SRGOV-OPS-001

```yaml spec-test
id: SRGOV-OPS-001
title: orchestration ops symbols follow deep-dot grammar
purpose: Ensures effect symbols use canonical deep-dot ops names.
type: governance.check
check: orchestration.ops_symbol_grammar
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
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - orchestration.ops_symbol_grammar
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```
