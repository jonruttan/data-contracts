# Spec-Lang Libraries Contract (v1)

## Purpose

Provide portable, reusable spec-lang function libraries shared across cases
without host-language hooks.

## Harness Shape

Cases MAY configure library loading via `harness.spec_lang`:

- `includes` (list[string]): ordered paths to library spec docs/files
- `exports` (list[string], optional): explicit symbol allowlist visible to case
- `imports` (list[mapping], optional): case-scoped stdlib import bindings
  (`from`, `names`, optional `as`)

Governance policy reuse:

- `type: governance.check` cases MUST provide `harness.spec_lang.includes`
  and MUST call exported library symbols from `policy_evaluate`.

Library paths:

- use virtual-root path semantics (`/` = contract root)
- root-relative values normalize to canonical `/...`
- MUST resolve within contract root
- MUST point to existing files
- MAY reference `.spec.md`, `.spec.yaml`, or `.spec.yml` library files
- external references (`external://provider/id`) are deny-by-default and
  require explicit capability + harness policy allowlist
- Canonical in-repo library case surfaces under `docs/spec/libraries` MUST be
  `.spec.md`; yaml/yml include support exists for non-canonical external
  adapter surfaces only.

## Library Document Shape

Library files are normal spec docs containing `type: spec_lang.library` cases.

Required fields for each library case:

- `id`
- `type: spec_lang.library`
- `defines` (mapping)
  - `public` (mapping: symbol -> expression, optional)
  - `private` (mapping: symbol -> expression, optional)

`defines.public.<symbol>` and
`defines.private.<symbol>` expression encoding:

- MUST use operator-keyed mapping-AST expression nodes (same canonical encoding
  as `evaluate`/`policy_evaluate`)
- MUST NOT use list s-expr authoring form
- scalar literals are allowed

Optional fields:

- `imports` (list[string]): additional library files loaded before this one

Export model:

- Exported symbols are derived from all `defines.public` symbol keys.
- `defines.private` symbols are loadable only inside library code and
  are not externally importable via harness exports.

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
