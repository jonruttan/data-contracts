# Conformance Fixtures

Language-agnostic fixtures used to validate runner parity across
implementations (for example Python and PHP).

Intended structure:

- `cases/`: fixture inputs (`*.spec.md` with fenced `yaml spec-test` blocks)
- `expected/`: legacy artifacts (non-authoritative)

Canonical expectation source:

- inline `expect.portable` and optional `expect.impl.<runtime>` on case records

Fixtures in this tree should avoid implementation-specific details whenever
possible.
