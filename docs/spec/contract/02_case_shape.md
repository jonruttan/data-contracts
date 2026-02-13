# Case Shape Contract (v1)

## Common Keys

- `id` (required)
- `type` (required)
- `title` (optional)
- `harness` (optional mapping)
- `assert_health` (optional mapping)

## Harness Namespace Rule

Runner-only setup keys MUST live under `harness`.

## Type-Specific Fields

Type-specific keys are defined per harness contract and schema docs.

## Assertion Health Policy Override

- `assert_health.mode` MAY be provided per case.
- Allowed values: `ignore`, `warn`, `error`.
