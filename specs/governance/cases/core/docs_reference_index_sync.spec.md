# Governance Cases

## SRGOV-DOCS-REF-002

```yaml contract-spec
id: SRGOV-DOCS-REF-002
title: reference index stays synced with chapter files
purpose: Ensures the machine-checked reference index entries stay aligned with the actual
  chapter set and order.
type: contract.check
harness:
  root: .
  reference_index:
    path: /docs/book/reference_index.md
    include_glob: docs/book/*.md
    exclude_files:
    - docs/book/index.md
    - docs/book/reference_index.md
    - docs/book/reference_coverage.md
  check:
    profile: governance.scan
    config:
      check: docs.reference_index_sync
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
      - docs.reference_index_sync
    imports:
      subject:
        from: artifact
        key: summary_json
```
