# Reference Coverage

## When to read this

Read this to confirm tutorial chapters, guides, and reference entrypoints are fully represented in the canonical manifest.

## What you will do

- Confirm every active book chapter is represented.
- Confirm generated reference surface is intentionally minimal.

## Step-by-step

1. Compare chapter files under `docs/book/` with `docs/book/reference_manifest.yaml`.
2. Verify guide order matches `docs/book/guides/index.md`.
3. Verify only `docs/book/99_generated_reference_index.md` is retained as generated entrypoint in the core manifest.

## Common failure signals

- chapter exists but missing in manifest
- manifest includes chapter that does not exist
- guide order differs between index and manifest

## Normative refs

- `docs/book/reference_manifest.yaml`
- `docs/book/reference_index.md`
- `specs/02_contracts/10_docs_quality.md`
