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
- `core/api_http.spec.md`: portable `api.http` extension behavior, CORS, verbs, and scenario coverage
- `core/codemod_scripts.spec.md`: codemod script check/write behavior coverage
- `domain_libraries.spec.md`: domain library contract coverage for non-core projection helpers
- `spec_lang.spec.md`: `evaluate` operator behavior, schema/runtime failures, TCO, and ramda-style utility conformance
- `spec_lang_library_contract.spec.md`: flat `spec_lang.export` defines contract coverage
- `subject_profiles.spec.md`: JSON-core subject profile envelope contract coverage
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
- `SRCONF-API-001`
- `SRCONF-API-002`
- `SRCONF-API-003`
- `SRCONF-API-004`
- `SRCONF-API-005`
- `SRCONF-API-006`
- `SRCONF-API-007`
- `SRCONF-API-008`
- `SRCONF-API-009`
- `SRCONF-API-010`
- `SRCONF-API-011`
- `SRCONF-API-012`
- `SRCONF-API-013`
- `SRCONF-API-014`
- `SRCONF-API-015`
- `SRCONF-API-016`
- `SRCONF-API-017`
- `SRCONF-CLI-001`
- `SRCONF-CLI-002`
- `SRCONF-CODEMOD-001`
- `SRCONF-CODEMOD-002`
- `SRCONF-CODEMOD-003`
- `SRCONF-CHAIN-EXPORT-001`
- `SRCONF-DOMAIN-LIB-001`
- `SRCONF-DOMAIN-LIB-002`
- `SRCONF-ERR-001`
- `SRCONF-EXPR-001`
- `SRCONF-EXPR-002`
- `SRCONF-EXPR-003`
- `SRCONF-EXPR-004`
- `SRCONF-EXPR-005`
- `SRCONF-EXPR-006`
- `SRCONF-EXPR-007`
- `SRCONF-EXPR-008`
- `SRCONF-EXPR-009`
- `SRCONF-EXPR-010`
- `SRCONF-EXPR-011`
- `SRCONF-EXPR-012`
- `SRCONF-EXPR-013`
- `SRCONF-EXPR-014`
- `SRCONF-EXPR-015`
- `SRCONF-EXPR-016`
- `SRCONF-EXPR-017`
- `SRCONF-EXPR-018`
- `SRCONF-EXPR-019`
- `SRCONF-EXPR-020`
- `SRCONF-EXPR-021`
- `SRCONF-EXPR-022`
- `SRCONF-EXPR-023`
- `SRCONF-EXPR-024`
- `SRCONF-LIB-CONTRACT-001`
- `SRCONF-LIB-CONTRACT-002`
- `SRCONF-LIB-CONTRACT-003`
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
- `SRCONF-PROFILE-001`
- `SRCONF-PROFILE-002`
- `SRCONF-SCHEMA-CASE-001`
- `SRCONF-SCHEMA-CASE-002`
- `SRCONF-SCHEMA-REG-001`
- `SRCONF-MARKDOWN-NS-001`

- `SRCONF-STDLIB-001`
- `SRCONF-STDLIB-002`
- `SRCONF-STDLIB-003`
- `SRCONF-STDLIB-004`
