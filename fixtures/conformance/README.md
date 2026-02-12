# Conformance Fixtures

Language-agnostic fixtures used to validate runner parity across
implementations (for example Python and PHP).

Intended structure:

- `cases/`: fixture inputs (spec blocks / harness inputs)
- `expected/`: expected results keyed by case id

Fixtures in this tree should avoid implementation-specific details whenever
possible.
