# Governance Cases

## SRGOV-DOCS-NAME-001

```yaml spec-test
id: SRGOV-DOCS-NAME-001
title: docs filenames follow lowercase separator policy
purpose: Enforces deterministic docs filename shape using underscores for words and hyphens
  for section separators.
type: governance.check
check: naming.filename_policy
harness:
  root: .
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
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
      - naming.filename_policy
```
