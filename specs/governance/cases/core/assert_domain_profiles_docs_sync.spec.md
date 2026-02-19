# Governance Cases

## SRGOV-ASSERT-PROFILE-003

```yaml contract-spec
id: SRGOV-ASSERT-PROFILE-003
title: domain profile docs synchronize with profile schema ids
purpose: Ensures python/php/http/markdown/makefile profile docs and subject profile schema
  stay synchronized.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: assert.domain_profiles_docs_sync
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  imports:
    subject:
      from: artifact
      key: violation_count
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
```
