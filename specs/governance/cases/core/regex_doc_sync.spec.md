# Governance Cases

## SRGOV-DOC-REGEX-001

```yaml contract-spec
id: SRGOV-DOC-REGEX-001
title: regex profile and operator tokens are synchronized across core docs
purpose: Ensures regex portability linkage and core assertion operator tokens remain aligned
  in contract/schema/policy docs.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.regex_doc_sync
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
      - docs.regex_doc_sync
```
