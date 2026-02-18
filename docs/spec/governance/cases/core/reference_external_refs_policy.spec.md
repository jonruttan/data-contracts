# Governance Cases

## SRGOV-REF-EXTERNAL-001

```yaml contract-spec
id: SRGOV-REF-EXTERNAL-001
title: external refs require explicit policy and capability
purpose: Ensures external:// references are deny-by-default and must declare allow policy.
type: contract.check
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: reference.external_refs_policy
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - check_id
    - reference.external_refs_policy
  target: summary_json
```
