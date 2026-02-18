# Adoption Profiles Contract (v1)

Defines the supported adoption tiers for running `spec_runner` checks.

## Profiles

### Core Profile

Command: `make core-check`

Goal:

- fast local confidence for teams adopting executable specs
- enforce core documentation/spec hygiene

Minimum checks:

- governance spec checks (`python -m spec_runner.spec_lang_commands run-governance-specs`)
- spec-lang format check (`python -m spec_runner.spec_lang_commands spec-lang-format --check specs`)
- focused core runner tests (`doc_parser`, `dispatcher`, `assertions`,
  `conformance_runner`)

### Full Profile

Command: `make check`

Goal:

- pre-merge confidence aligned with CI gate

Minimum checks:

- all core-profile checks
- lint/type/compile checks
- conformance purpose reports
- Python/PHP parity command
- full pytest suite

## Compatibility Expectation

- Profile names and command entrypoints are part of contributor-facing docs
  contract.
- Implementations SHOULD keep profile wording synchronized in:
  - `README.md`
  - `docs/development.md`
