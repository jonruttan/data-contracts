# Governance Cases

## SRGOV-NORM-004

```yaml spec-test
id: SRGOV-NORM-004
title: normalization spec style policy stays profile-driven
purpose: Ensures conformance style limits and wording remain synchronized with the normalization
  profile and governance scanner constants.
type: governance.check
check: normalization.spec_style_sync
harness:
  root: .
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
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
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: must
  checks:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - normalization.spec_style_sync
  target: summary_json
```
