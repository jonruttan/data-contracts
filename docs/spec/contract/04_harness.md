# Harness Contract (v1)

## Dispatch

- Runner dispatches by case `type`.
- Harness receives parsed case and execution context.

## Entrypoint

For `type: cli.run`:

- `harness.entrypoint` SHOULD be provided by the spec.
- Implementations SHOULD support an environment fallback (for example
  `SPEC_RUNNER_ENTRYPOINT`) for local/CI ergonomics when they can read process
  environment variables and resolve dynamic `module:attr` entrypoints.
- Portable conformance fixtures MUST provide `harness.entrypoint` explicitly
  and MUST NOT rely on environment fallback behavior.
- Implementations SHOULD provide a safe mode that disables hook entrypoints and
  env fallback (for example `SPEC_RUNNER_SAFE_MODE=1`).
- Implementations SHOULD support a process-env allowlist control for `cli.run`
  executions (for example `SPEC_RUNNER_ENV_ALLOWLIST=K1,K2`).

Policy ids for these requirements are listed in
`docs/spec/contract/policy_v1.yaml`.

## Canonical Targets

For `cli.run`:

- `stdout`
- `stderr`
- `stdout_path`
- `stdout_path_text`

For `text.file`:

- `text`

## Spec-Lang Reuse

- `harness.spec_lang.library_paths` MAY provide ordered library docs/files
  containing `type: spec_lang.library` reusable function definitions.
- `harness.spec_lang.exports` MAY constrain visible imported symbols to an
  explicit allowlist.

## Path Safety

- `cli.run` `harness.setup_files[*].path` MUST be relative and MUST resolve
  within the runner temp directory.
- `text.file` `path` MUST be relative and MUST resolve within the
  implementation's contract root/workspace boundary.

## Trust Model

- Spec files are trusted inputs. `cli.run` executes commands/module entrypoints
  declared in spec data and harness config.
- Runner hook entrypoints (`hook_before` / `hook_after`) execute project code
  with the same process privileges as the test runner.
- Implementations MAY inherit process environment variables for `cli.run`.
  Operators MUST treat process environment as potentially exposed to the system
  under test and SHOULD avoid loading unrelated secrets in runner environments.
- Running specs from untrusted sources is out of scope for v1 and MUST be
  treated as unsafe.
