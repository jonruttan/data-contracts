# Conformance Cases

Case fixtures that portable runner implementations execute.

## Authoring Quick Rules

- Keep case ids stable.
- Prefer small, focused cases per behavior.
- Include both pass and fail cases.
- Use Markdown `.spec.md` files with fenced `yaml spec-test` blocks.
- Prefer inline expectations via:
  - `expect.portable`
  - optional `expect.impl.<runtime>` overrides
- Conformance fixture cases should always include `expect.portable.status`.
- Conformance fixture cases must include a non-empty `purpose`.
- Purpose lint defaults/runtime profiles live in `docs/spec/conformance/purpose_lint_v1.yaml`.
- Style details are defined in `docs/spec/conformance/style.md`.

## Fixture File Guide

- `assertion-health.spec.md`: assertion-health diagnostics and mode behavior
- `cli-run-entrypoint.spec.md`: entrypoint precedence and capability gating
- `failure-context.spec.md`: deterministic failure context tokens
- `php-text-file-subset.spec.md`: portable `text.file` subset used for PHP parity

## Case Index

- `SRCONF-AH-001`
- `SRCONF-AH-002`
- `SRCONF-AH-003`
- `SRCONF-AH-004`
- `SRCONF-AH-005`
- `SRCONF-AH-006`
- `SRCONF-CLI-001`
- `SRCONF-CLI-002`
- `SRCONF-ERR-001`
- `SRCONF-PHP-TEXT-001`
- `SRCONF-PHP-TEXT-002`
- `SRCONF-PHP-TEXT-003`
- `SRCONF-PHP-TEXT-004`
- `SRCONF-PHP-TEXT-005`
- `SRCONF-PHP-TEXT-006`
- `SRCONF-PHP-TEXT-007`
- `SRCONF-PHP-TEXT-008`
- `SRCONF-PHP-TEXT-009`
- `SRCONF-PHP-TEXT-010`
- `SRCONF-PHP-TEXT-011`
- `SRCONF-PHP-TEXT-012`
- `SRCONF-PHP-TEXT-013`
- `SRCONF-PHP-TEXT-014`
