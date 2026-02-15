# Governance Cases

## SRGOV-DOCS-REF-002

```yaml spec-test
id: SRGOV-DOCS-REF-002
title: reference index stays synced with chapter files
purpose: Ensures the machine-checked reference index entries stay aligned with the actual chapter set and order.
type: governance.check
check: docs.reference_index_sync
harness:
  root: .
  reference_index:
    path: docs/book/reference_index.md
    include_glob: docs/book/*.md
    exclude_files:
      - docs/book/README.md
      - docs/book/reference_index.md
      - docs/book/reference_coverage.md
  policy_evaluate:
    - ["is_empty", ["get", ["subject"], "violations"]]
assert:
  - target: text
    must:
      - contain: ["PASS: docs.reference_index_sync"]
```
