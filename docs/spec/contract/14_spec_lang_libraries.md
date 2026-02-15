# Spec-Lang Libraries Contract (v1)

## Purpose

Provide portable, reusable spec-lang function libraries shared across cases
without host-language hooks.

## Harness Shape

Cases MAY configure library loading via `harness.spec_lang`:

- `library_paths` (list[string]): ordered paths to library spec docs/files
- `exports` (list[string], optional): explicit symbol allowlist visible to case

Library paths:

- MAY be relative to the current spec document or absolute
- MUST resolve within contract root
- MUST point to existing files
- MAY reference `.spec.md`, `.spec.yaml`, or `.spec.yml` library files

## Library Document Shape

Library files are normal spec docs containing `type: spec_lang.library` cases.

Required fields for each library case:

- `id`
- `type: spec_lang.library`
- `functions` (mapping: symbol -> spec-lang expression)

Optional fields:

- `imports` (list[string]): additional library files loaded before this one
- `exports` (list[string]): symbols exported by this library case

## Resolution Rules

- Load order is deterministic and import-first.
- Import cycles MUST fail with schema error.
- Duplicate exported symbol names across loaded libraries MUST fail.
- Symbol resolution for evaluation is:
  - local `let` / function params
  - imported library symbols
  - core builtins

## Determinism and Safety

- Library expressions execute in the same bounded spec-lang evaluator.
- No implementation-defined host callbacks are allowed.
- Errors in library loading/binding are schema failures.
