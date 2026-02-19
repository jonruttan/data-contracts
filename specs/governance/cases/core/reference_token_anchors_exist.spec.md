# Governance Cases

## SRGOV-REF-TOKENS-001

```yaml contract-spec
id: SRGOV-REF-TOKENS-001
title: configured token anchors exist
purpose: Ensures configured token anchors resolve to existing files and token matches.
type: contract.check
harness:
  root: .
  token_anchors:
    files:
    - path: /specs/contract/03b_spec_lang_v1.md
      tokens:
      - operator-keyed mapping AST
  check:
    profile: governance.scan
    config:
      check: reference.token_anchors_exist
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - reference.token_anchors_exist
    imports:
      subject:
        from: artifact
        key: summary_json
```
