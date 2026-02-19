# Governance Cases

## SRGOV-DOCS-NAME-001

```yaml contract-spec
id: SRGOV-DOCS-NAME-001
title: docs filenames follow lowercase separator policy
purpose: Enforces deterministic docs filename shape using underscores for words and hyphens
  for section separators.
type: contract.check
harness:
  root: .
  filename_policy:
    paths:
    - docs
    include_extensions:
    - .md
    - .yaml
    - .yml
    - .json
    allow_exact:
    - README.md
    allowed_name_regex: ^[a-z0-9]+(?:_[a-z0-9]+)*(?:-[a-z0-9]+(?:_[a-z0-9]+)*)*(?:\.spec)?\.(?:md|yaml|yml|json)$
  check:
    profile: governance.scan
    config:
      check: naming.filename_policy
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    'on': violation_count
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
  - id: assert_2
    'on': summary_json
    assert:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - naming.filename_policy
```
