# Governance Cases

## SRGOV-STDLIB-001

```yaml spec-test
id: SRGOV-STDLIB-001
title: spec-lang stdlib profile is complete
purpose: Ensures the declared stdlib profile symbols are implemented in Python and PHP.
type: governance.check
check: spec_lang.stdlib_profile_complete
harness:
  root: .
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
assert:
- target: violation_count
  must:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
```
