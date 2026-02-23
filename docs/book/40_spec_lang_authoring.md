# Spec-Lang Authoring

## When to read this

Read this when writing or reviewing assertion expressions.

## What you will do

- Author readable mapping-AST expressions.
- Use library symbols instead of repeated inline logic.

## Step-by-step

1. Start with clear imports and symbol names.
2. Keep each check focused on one outcome.
3. Prefer library calls for reusable policy logic.
4. Add examples that show pass/fail intent.

## Common failure signals

- Overly nested expressions without clear intent.
- Copy-pasted assertion blocks across many cases.
- Missing symbol documentation for reused calls.

## Normative refs

- `specs/02_contracts/03b_spec_lang_v1.md`
- `specs/02_contracts/14_spec_lang_libraries.md`
- `specs/05_libraries/`
