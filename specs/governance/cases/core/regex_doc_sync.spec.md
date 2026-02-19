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
  imports:
  - from: artifact
    names:
    - violation_count
    as:
      violation_count: subject
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
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
      - docs.regex_doc_sync
    imports:
    - from: artifact
      names:
      - summary_json
      as:
        summary_json: subject
```
