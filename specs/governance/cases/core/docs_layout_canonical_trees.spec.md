# Governance Cases

## SRGOV-DOCS-LAYOUT-001

```yaml contract-spec
id: SRGOV-DOCS-LAYOUT-001
title: docs layout canonical trees exist
purpose: Enforces canonical docs root namespaces.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.layout_canonical_trees
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
      - docs.layout_canonical_trees
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```
