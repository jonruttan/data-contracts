# Appendix: Reference Index

```yaml doc-meta
doc_id: DOC-REF-099
title: Appendix Reference Index Wrapper
status: active
audience: author
owns_tokens:
- appendix_reference_index_wrapper
requires_tokens:
- quickstart_minimal_case
commands:
- run: ./scripts/runner_adapter.sh docs-generate-check
  purpose: Verify generated reference index and coverage surfaces are synchronized.
examples:
- id: EX-APP-REFIDX-001
  runnable: false
  opt_out_reason: Wrapper page links generated surfaces and intentionally contains no runnable fenced examples.
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Provide a stable appendix entrypoint for generated reference navigation surfaces.

## Inputs

- generated `reference_index.md` and `reference_coverage.md` outputs

## Outputs

- canonical pointers to generated chapter order and coverage pages

## Failure Modes

- stale/missing generated reference pages
- stale wrapper links

This appendix is a wrapper around generated reference navigation surfaces.

- `/docs/book/reference_index.md`
- `/docs/book/reference_coverage.md`

Use these generated pages as the authoritative chapter/order and coverage view.
