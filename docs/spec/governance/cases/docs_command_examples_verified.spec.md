# Governance Cases

## SRGOV-DOCS-QUAL-006

```yaml spec-test
id: SRGOV-DOCS-QUAL-006
title: docs command and example blocks are validated
purpose: Ensures runnable example blocks parse/validate unless explicitly opted out.
type: governance.check
check: docs.command_examples_verified
harness:
  root: .
  docs_quality:
    manifest: docs/book/reference_manifest.yaml
  policy_evaluate:
    - ["is_empty", ["get", ["subject"], "violations"]]
assert:
  - target: text
    must:
      - contain: ["PASS: docs.command_examples_verified"]
```
