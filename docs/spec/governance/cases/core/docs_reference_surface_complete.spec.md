# Governance Cases

## SRGOV-DOCS-REF-001

```yaml spec-test
id: SRGOV-DOCS-REF-001
title: docs reference surface files exist
purpose: Enforces that the canonical docs reference surface remains complete and cannot silently
  lose required files.
type: governance.check
check: docs.reference_surface_complete
harness:
  root: .
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  docs_reference_surface:
    required_files:
    - docs/book/reference_index.md
    - docs/spec/schema/schema_v1.md
    - docs/spec/contract/10_docs_quality.md
    - docs/book/02_core_model.md
    - docs/book/03_assertions.md
    - docs/book/04_spec_lang_reference.md
    required_globs:
    - docs/spec/contract/*.md
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
      - docs.reference_surface_complete
```
