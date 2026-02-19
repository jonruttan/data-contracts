# Chapter 50: Library Authoring

```yaml doc-meta
doc_id: DOC-REF-150
title: Chapter 50 Library Authoring
status: active
audience: author
owns_tokens:
- export_doc_metadata_contract
requires_tokens:
- mapping_ast_authoring_patterns
commands:
- run: ./scripts/control_plane.sh docs-generate-check
  purpose: Ensure library symbol and case reference docs remain synchronized.
examples:
- id: EX-LIB-AUTH-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Define how to author `contract.export` libraries with executable behavior and complete documentation metadata.

## Inputs

- `specs/libraries/**/*.spec.md`
- `contract.export` schema requirements

## Outputs

- reusable symbol exports
- generated library reference docs and indexes

## Failure Modes

- missing required root `doc` metadata on export cases
- missing `library` metadata block
- incomplete `harness.exports[].doc` metadata

## Export Case Model

`contract.export` cases include:

- root `library` metadata (`id`, `module`, `stability`, `owner`)
- root `doc` metadata (`summary`, `description`, `audience`, `since`)
- `harness.exports[]` with per-symbol docs metadata
- optional root `domain` for grouping and export prefixing

## Symbol and Domain Conventions

- use stable, verb-first symbol semantics
- apply `domain` when grouping related exports
- keep names portable and runtime-neutral

## Reference Generation

Generated surfaces driven from specs:

- `docs/book/93j_library_symbol_reference.md`
- `docs/book/93k_library_symbol_index.md`
- `.artifacts/library-symbol-catalog.json`
