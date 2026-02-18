# Governance Cases

## SRGOV-DOCS-MD-001

```yaml contract-spec
id: SRGOV-DOCS-MD-001
title: markdown checks use structured markdown helper library
purpose: Prevent brittle plain string-contains markdown assertions in governed docs cases.
type: contract.check
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: docs.markdown_structured_assertions_required
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
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
  target: summary_json
```
