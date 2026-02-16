# Governance Cases

## SRGOV-DOCS-REF-002

```yaml spec-test
id: SRGOV-DOCS-REF-002
title: reference index stays synced with chapter files
purpose: Ensures the machine-checked reference index entries stay aligned with the actual
  chapter set and order.
type: governance.check
check: docs.reference_index_sync
harness:
  root: .
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  reference_index:
    path: /docs/book/reference_index.md
    include_glob: docs/book/*.md
    exclude_files:
    - docs/book/README.md
    - docs/book/reference_index.md
    - docs/book/reference_coverage.md
    - docs/book/runner_api_reference.md
    - docs/book/harness_type_reference.md
    - docs/book/spec_lang_builtin_catalog.md
    - docs/book/contract_policy_reference.md
    - docs/book/traceability_reference.md
    - docs/book/governance_checks_reference.md
    - docs/book/metrics_reference.md
    - docs/book/spec_case_shape_reference.md
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: violation_count
  must:
  - evaluate:
    - eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
    - eq:
      - get:
        - {var: subject}
        - check_id
      - docs.reference_index_sync
```
