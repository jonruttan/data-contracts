# Governance Cases

## SRGOV-REF-EXTERNAL-001

```yaml spec-test
id: SRGOV-REF-EXTERNAL-001
title: external refs require explicit policy and capability
purpose: Ensures external:// references are deny-by-default and must declare allow policy.
type: governance.check
check: reference.external_refs_policy
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - check_id
    - reference.external_refs_policy
  target: summary_json
```
