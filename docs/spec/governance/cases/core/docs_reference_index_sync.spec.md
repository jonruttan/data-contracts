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
      check: docs.reference_index_sync
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          std.logic.eq:
          - {var: subject}
          - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          MUST:
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
  target: summary_json
```
