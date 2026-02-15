# Governance Cases

## SRGOV-ASSERT-PROFILE-003

```yaml spec-test
id: SRGOV-ASSERT-PROFILE-003
title: domain profile docs synchronize with profile schema ids
purpose: Ensures python/php/http/markdown/makefile profile docs and subject profile schema
  stay synchronized.
type: governance.check
check: assert.domain_profiles_docs_sync
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
