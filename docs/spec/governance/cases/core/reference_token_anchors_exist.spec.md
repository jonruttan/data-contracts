# Governance Cases

## SRGOV-REF-TOKENS-001

```yaml spec-test
id: SRGOV-REF-TOKENS-001
title: configured token anchors exist
purpose: Ensures configured token anchors resolve to existing files and token matches.
type: governance.check
check: reference.token_anchors_exist
harness:
  root: .
  token_anchors:
    files:
    - path: /docs/spec/contract/03b_spec_lang_v1.md
      tokens:
      - operator-keyed mapping AST
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
      - reference.token_anchors_exist
```
