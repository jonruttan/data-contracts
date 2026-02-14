# Governance Cases

## SRGOV-DOCS-V2-006

```yaml spec-test
id: SRGOV-DOCS-V2-006
title: docs command and example blocks are validated
purpose: Ensures runnable example blocks parse/validate unless explicitly opted out.
type: governance.check
check: docs.command_examples_verified
harness:
  root: .
  docs_v2:
    manifest: docs/book/reference_manifest.yaml
assert:
  - target: text
    must:
      - contain: ["PASS: docs.command_examples_verified"]
```
