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
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - normalization.spec_style_sync
```
