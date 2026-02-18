# Governance Cases

## SRGOV-DOCS-NAME-001

```yaml contract-spec
id: SRGOV-DOCS-NAME-001
title: docs filenames follow lowercase separator policy
purpose: Enforces deterministic docs filename shape using underscores for words and
  hyphens for section separators.
type: governance.check
check: naming.filename_policy
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
- id: assert_2
  class: MUST
  asserts:
  - MUST:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - naming.filename_policy
  target: summary_json
```
