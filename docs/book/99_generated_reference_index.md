# Generated Reference Index

```yaml doc-meta
doc_id: DOC-REF-199
title: Generated Reference Index
status: active
audience: reviewer
owns_tokens:
- generated_reference_gateway
requires_tokens:
- normative_reference_map
commands:
- run: ./runners/public/runner_adapter.sh --impl rust docs-generate-check
  purpose: Ensure generated surfaces and index links are synchronized.
examples:
- id: EX-GENERATED-INDEX-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Act as the canonical navigation gateway for generated reference surfaces.

## Inputs

- generated docs under `docs/book/9*`
- generated artifacts under `.artifacts/`

## Outputs

- stable links to generated references

## Failure Modes

- missing generated chapter links
- stale links after generator surface changes

## Generated Chapter Surfaces

- `docs/book/91_appendix_runner_api_reference.md`
- `docs/book/92_appendix_harness_type_reference.md`
- `docs/book/93_appendix_spec_lang_builtin_catalog.md`
- `docs/book/93a_std_core.md`
- `docs/book/93b_std_logic.md`
- `docs/book/93c_std_math.md`
- `docs/book/93d_std_string.md`
- `docs/book/93e_std_collection.md`
- `docs/book/93f_std_object.md`
- `docs/book/93g_std_type.md`
- `docs/book/93h_std_set.md`
- `docs/book/93i_std_json_schema_fn_null.md`
- `docs/book/93j_library_symbol_reference.md`
- `docs/book/93k_library_symbol_index.md`
- `docs/book/93l_spec_case_reference.md`
- `docs/book/93m_spec_case_index.md`
- `docs/book/94_appendix_contract_policy_reference.md`
- `docs/book/95_appendix_traceability_reference.md`
- `docs/book/96_appendix_governance_checks_reference.md`
- `docs/book/97_appendix_metrics_reference.md`
- `docs/book/98_appendix_spec_case_shape_reference.md`

## Generated Artifact Surfaces

- `.artifacts/runner-api-catalog.json`
- `.artifacts/harness-type-catalog.json`
- `.artifacts/spec-lang-builtin-catalog.json`
- `.artifacts/library-symbol-catalog.json`
- `.artifacts/spec-case-catalog.json`
- `.artifacts/policy-rule-catalog.json`
- `.artifacts/traceability-catalog.json`
- `.artifacts/governance-check-catalog.json`
- `.artifacts/metrics-field-catalog.json`
- `.artifacts/spec-schema-field-catalog.json`
