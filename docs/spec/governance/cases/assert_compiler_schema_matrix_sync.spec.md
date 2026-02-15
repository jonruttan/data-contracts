# Governance Cases

## SRGOV-ASSERT-SYNC-001

```yaml spec-test
id: SRGOV-ASSERT-SYNC-001
title: compiler behavior stays aligned with universal assertion contract
purpose: Ensures compiler operator handling, schema wording, and assertion contract wording stay synchronized for universal evaluate core semantics.
type: governance.check
check: assert.compiler_schema_matrix_sync
harness:
  root: .
assert:
  - target: text
    must:
      - contain: ["PASS: assert.compiler_schema_matrix_sync"]
```
