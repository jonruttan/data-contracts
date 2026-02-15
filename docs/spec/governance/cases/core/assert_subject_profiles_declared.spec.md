# Governance Cases

## SRGOV-ASSERT-PROFILE-001

```yaml spec-test
id: SRGOV-ASSERT-PROFILE-001
title: subject profile contract artifacts are declared
purpose: Ensures subject profile contract/schema/type docs and domain libraries are present
  as required artifacts.
type: governance.check
check: assert.subject_profiles_declared
harness:
  root: .
  spec_lang:
    library_paths:
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
    - eq:
      - {var: subject}
      - 0
```
