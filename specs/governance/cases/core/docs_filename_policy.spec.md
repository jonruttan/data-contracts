# Governance Cases

## SRGOV-DOCS-LAYOUT-003

```yaml contract-spec
id: SRGOV-DOCS-LAYOUT-003
title: docs filenames follow canonical lowercase policy
purpose: Enforces lowercase, underscore, and hyphen filename policy across docs.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.filename_policy
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
      key: summary_json
  steps:
  - id: assert_1
    assert:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - docs.filename_policy
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```
