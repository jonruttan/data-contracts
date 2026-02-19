# Chapter 90: Reference Guide

```yaml doc-meta
doc_id: DOC-REF-190
title: Chapter 90 Reference Guide
status: active
audience: reviewer
owns_tokens:
- normative_reference_map
requires_tokens:
- deterministic_failure_triage
commands:
- run: ./runners/public/runner_adapter.sh --impl rust docs-generate-check
  purpose: Verify generated reference surfaces are synchronized.
examples:
- id: EX-REFERENCE-GUIDE-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Provide a concise map from operational author guidance to normative schema/contract references.

## Inputs

- schema docs under `specs/schema`
- contract docs under `specs/contract`
- generated reference outputs under `docs/book`

## Outputs

- authoritative lookup path for reviewers and maintainers

## Failure Modes

- using narrative docs where normative contract text is required
- stale generated refs interpreted as source of truth

## Normative Sources

- `specs/schema/schema_v1.md`
- `specs/contract/02_case_shape.md`
- `specs/contract/03_assertions.md`
- `specs/contract/03b_spec_lang_v1.md`
- `specs/contract/10_docs_quality.md`
- `specs/contract/12_runner_interface.md`

## Generated References

Use `docs/book/99_generated_reference_index.md` as the canonical entrypoint.
