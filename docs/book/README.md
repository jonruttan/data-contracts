# YAML `spec-test` Book

Practical guide for authoring and running executable spec tests in this repo.

## Who This Is For

- Engineers writing new `yaml spec-test` cases.
- Reviewers validating schema/assertion correctness.
- Port maintainers comparing behavior across Python and PHP runners.

## Read Paths

Fast start:

1. `docs/book/01_quickstart.md`
2. `docs/book/appendix_cheatsheet.md`

Deterministic onboarding:

1. `docs/book/00_first_10_minutes.md`
2. `docs/book/01_quickstart.md`

Full authoring:

1. `docs/book/01_quickstart.md`
2. `docs/book/02_core_model.md`
3. `docs/book/03_assertions.md`
4. `docs/book/04_spec_lang_reference.md`
5. `docs/spec/schema/schema_v1.md`
6. `docs/spec/contract/`

Portability and conformance:

1. `docs/spec/conformance/README.md`
2. `docs/spec/conformance/cases/*.spec.md`
3. `docs/spec/impl/php.md`

## Canonical Sources

- Stable schema: `docs/spec/schema/schema_v1.md`
- Portable contract: `docs/spec/contract/`
- Conformance fixtures: `docs/spec/conformance/cases/`
- PHP implementation fixtures: `docs/spec/impl/php/cases/`

## Chapter Guide

- `00_first_10_minutes.md`: deterministic first run and safety model
- `01_quickstart.md`: smallest runnable examples
- `02_core_model.md`: case shape, discovery, types, harness rules
- `03_assertions.md`: assertion tree and operators
- `04_spec_lang_reference.md`: complete `evaluate`/spec-lang reference
