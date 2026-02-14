# Governance Cases

## SRGOV-DOCS-V2-005

```yaml spec-test
id: SRGOV-DOCS-V2-005
title: instruction pages contain required operational sections
purpose: Ensures docs metadata required sections are present in canonical chapter content.
type: governance.check
check: docs.instructions_complete
harness:
  root: .
  docs_v2:
    manifest: docs/book/reference_manifest.yaml
assert:
  - target: text
    must:
      - contain: ["PASS: docs.instructions_complete"]
```
