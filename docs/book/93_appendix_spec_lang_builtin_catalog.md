# Spec-Lang Builtin Catalog

```yaml doc-meta
doc_id: DOC-REF-093
title: Appendix Spec-Lang Builtin Catalog
status: active
audience: reviewer
owns_tokens:
- appendix_spec_lang_builtin_catalog
requires_tokens:
- spec-lang
commands:
- run: ./scripts/runner_adapter.sh docs-generate-check
  purpose: Verify generated builtin catalog remains synchronized.
examples:
- id: EX-APP-BUILTIN-001
  runnable: false
  opt_out_reason: Generated reference page intentionally contains no runnable fenced examples.
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

Machine-generated spec-lang builtin catalog index.

## Purpose

Provide namespace-level table-of-contents and quality/parity summary for spec-lang stdlib references.

## Inputs

- `/.artifacts/spec-lang-builtin-catalog.json`

## Outputs

- Namespace chapter map for:
  - `/docs/book/93a_std_core.md`
  - `/docs/book/93b_std_logic.md`
  - `/docs/book/93c_std_math.md`
  - `/docs/book/93d_std_string.md`
  - `/docs/book/93e_std_collection.md`
  - `/docs/book/93f_std_object.md`
  - `/docs/book/93g_std_type.md`
  - `/docs/book/93h_std_set.md`
  - `/docs/book/93i_std_json_schema_fn_null.md`

## Failure Modes

- stale generated block after builtin/profile changes
- missing generated markers
- docs quality score below governance threshold

<!-- GENERATED:START spec_lang_builtin_catalog -->

## Generated Spec-Lang Builtin Catalog

- builtin_count: 189
- namespace_count: 9
- parity_count: 189
- all_parity: true
- doc_quality_score: 0.9788

| namespace | chapter | symbols |
|---|---|---|
| `core` | `/docs/book/93a_std_core.md` | 60 |
| `logic` | `/docs/book/93b_std_logic.md` | 13 |
| `math` | `/docs/book/93c_std_math.md` | 18 |
| `string` | `/docs/book/93d_std_string.md` | 14 |
| `collection` | `/docs/book/93e_std_collection.md` | 36 |
| `object` | `/docs/book/93f_std_object.md` | 20 |
| `type` | `/docs/book/93g_std_type.md` | 11 |
| `set` | `/docs/book/93h_std_set.md` | 7 |
| `json_schema_fn_null` | `/docs/book/93i_std_json_schema_fn_null.md` | 10 |
<!-- GENERATED:END spec_lang_builtin_catalog -->
