# Governance Cases

## SRGOV-DOCS-MD-001

```yaml contract-spec
id: SRGOV-DOCS-MD-001
title: markdown checks use structured markdown helper library
purpose: Prevent brittle plain string-contains markdown assertions in governed docs cases.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.markdown_structured_assertions_required
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
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
    imports:
      subject:
        from: artifact
        key: violation_count
  - id: assert_2
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
      - docs.markdown_structured_assertions_required
    imports:
      subject:
        from: artifact
        key: summary_json
```
