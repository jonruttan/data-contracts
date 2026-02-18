# Conformance Cases

Case fixtures that portable runner implementations execute.

## Authoring Quick Rules

- Keep case ids stable.
- Prefer small, focused cases per behavior.
- Include both pass and fail cases.
- Use Markdown `.spec.md` files with fenced `yaml contract-spec` blocks.
- Prefer inline expectations via:
  - optional `expect.impl.<runtime>` overrides
- Conformance fixture cases should always include `expect.portable.status`.
- Conformance fixture cases must include a non-empty `purpose`.
- Purpose lint defaults/runtime profiles live in `docs/spec/conformance/purpose_lint_v1.yaml`.
- Style details are defined in `docs/spec/conformance/style.md`.

## Fixture File Guide

- `assertion-health.spec.md`: assertion-health diagnostics and mode behavior
- `core/api_http.spec.md`: portable `api.http` extension behavior, CORS, verbs, and scenario coverage
- `domain_libraries.spec.md`: domain library contract coverage for non-core projection helpers
- `spec_lang.spec.md`: `evaluate` operator behavior, schema/runtime failures, TCO, and ramda-style utility conformance
- `spec_lang_library_contract.spec.md`: `spec.export` producer contract coverage
- `subject_profiles.spec.md`: JSON-core subject profile envelope contract coverage
- `cli-run-entrypoint.spec.md`: entrypoint precedence and capability gating
- `failure-context.spec.md`: deterministic failure context tokens
- `php-text-file-subset.spec.md`: portable `text.file` subset used for PHP parity

## Case Index


