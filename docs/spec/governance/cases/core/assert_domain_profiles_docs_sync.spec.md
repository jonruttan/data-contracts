# Governance Cases

## SRGOV-ASSERT-PROFILE-003

```yaml contract-spec
id: SRGOV-ASSERT-PROFILE-003
title: domain profile docs synchronize with profile schema ids
purpose: Ensures python/php/http/markdown/makefile profile docs and subject profile
  schema stay synchronized.
type: governance.check
check: assert.domain_profiles_docs_sync
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
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
```
