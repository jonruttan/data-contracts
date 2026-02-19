# Spec Book

Author-first, contract-backed documentation for writing, running, and governing executable specs.

## Primary Audience

- spec authors and reviewers
- maintainers operating Rust-first gate and governance flows

## Read Paths

Fast start:

1. `docs/book/10_getting_started.md`
2. `docs/book/20_case_model.md`
3. `docs/book/30_assertion_model.md`

Full authoring path:

1. `docs/book/10_getting_started.md`
2. `docs/book/20_case_model.md`
3. `docs/book/30_assertion_model.md`
4. `docs/book/40_spec_lang_authoring.md`
5. `docs/book/50_library_authoring.md`
6. `docs/book/60_runner_and_gates.md`
7. `docs/book/70_governance_and_quality.md`
8. `docs/book/80_troubleshooting.md`
9. `docs/book/90_reference_guide.md`
10. `docs/book/99_generated_reference_index.md`

## Canonical Sources

- `specs/schema/schema_v1.md`
- `specs/contract/`
- `specs/conformance/cases/`
- `specs/libraries/`

## Compatibility (Non-Blocking)

Python/PHP runtime lanes are compatibility matrix lanes and non-blocking by default.
Rust lane is the required lane for merge-blocking behavior.
