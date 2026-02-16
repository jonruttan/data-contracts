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
  docs_reference_surface:
    required_files:
    - docs/book/reference_index.md
    - docs/spec/schema/schema_v1.md
    - docs/spec/contract/10_docs_quality.md
    - docs/book/02_core_model.md
    - docs/book/03_assertions.md
    - docs/book/04_spec_lang_guide.md
    - docs/book/05_howto.md
    - docs/book/06_troubleshooting.md
    - docs/book/07_spec_lang_reference.md
    - docs/book/93_appendix_spec_lang_builtin_catalog.md
    - docs/book/93a_std_core.md
    - docs/book/93b_std_logic.md
    - docs/book/93c_std_math.md
    - docs/book/93d_std_string.md
    - docs/book/93e_std_collection.md
    - docs/book/93f_std_object.md
    - docs/book/93g_std_type.md
    - docs/book/93h_std_set.md
    - docs/book/93i_std_json_schema_fn_null.md
    required_globs:
    - docs/spec/contract/*.md
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
      exports:
        policy.pass_when_no_violations:
          from: library.symbol
          path: /policy.pass_when_no_violations
          required: true
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
  target: violation_count
- id: assert_2
  class: must
  checks:
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
      - docs.reference_surface_complete
  target: summary_json
```
