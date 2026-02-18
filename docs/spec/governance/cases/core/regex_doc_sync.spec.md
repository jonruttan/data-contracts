# Governance Cases

## SRGOV-DOC-REGEX-001

```yaml contract-spec
id: SRGOV-DOC-REGEX-001
title: regex profile and operator tokens are synchronized across core docs
purpose: Ensures regex portability linkage and core assertion operator tokens remain
  aligned in contract/schema/policy docs.
type: governance.check
check: docs.regex_doc_sync
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
      - docs.regex_doc_sync
  target: summary_json
```
