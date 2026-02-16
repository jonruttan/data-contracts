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
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  docs_quality:
    manifest: docs/book/reference_manifest.yaml
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: violation_count
  must:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - docs.command_examples_verified
```
