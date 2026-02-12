# Harness Contract (v1)

## Dispatch

- Runner dispatches by case `type`.
- Harness receives parsed case and execution context.

## Entrypoint

For `type: cli.run`:

- `harness.entrypoint` MUST be provided by the spec.
- Implementations SHOULD support an environment fallback (for example
  `SPEC_RUNNER_ENTRYPOINT`) when feasible for local/CI ergonomics.
- Portable conformance fixtures MUST provide `harness.entrypoint` explicitly
  and MUST NOT rely on environment fallback behavior.

## Canonical Targets

For `cli.run`:

- `stdout`
- `stderr`
- `stdout_path`
- `stdout_path_text`

For `text.file`:

- `text`
