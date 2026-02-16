# Harness Contract (v1)

## Dispatch

- Runner dispatches by case `type`.
- Harness receives parsed case and execution context.

## Entrypoint

For `type: cli.run`:

- `harness.entrypoint` MUST be provided by the spec.
- Portable conformance fixtures MUST provide `harness.entrypoint` explicitly.
- Implementations SHOULD provide a safe mode that disables hook entrypoints
  (for example `SPEC_RUNNER_SAFE_MODE=1`).
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
- `context_json` (JSON subject profile envelope)

For `text.file`:

- `text`
- `context_json` (JSON subject profile envelope)

For `api.http`:

- `status`
- `headers`
- `body_text`
- `body_json`
- `context_json` (JSON subject profile envelope)

`api.http` auth/runtime profile:

- `harness.api_http.mode` (optional): `deterministic` (default) or `live`
  - `deterministic` forbids network `http(s)` fetches for request/token URLs
  - `live` allows network `http(s)` fetches
- `harness.api_http.auth.oauth` (optional mapping):
  - `grant_type`: must be `client_credentials`
  - `token_url` (required)
  - `client_id_env` / `client_secret_env` (required): env var names only
  - `scope` / `audience` (optional)
  - `auth_style`: `basic` (default) or `body`
  - `token_field`: default `access_token`
  - `expires_field`: default `expires_in`
  - `refresh_skew_seconds`: default `30`

OAuth behavior:

- credentials are resolved from env references only (no inline secret fields)
- bearer token is injected as `Authorization: Bearer <token>` unless request
  headers already define `Authorization`
- `api.http` context metadata must not include raw secret/token values

For `orchestration.run`:

- `result_json`
- `stdout`
- `stderr`
- `exit_code`
- `context_json` (JSON subject profile envelope)

For `docs.generate`:

- `result_json`
- `output_text`
- `context_json` (JSON subject profile envelope)

## Subject-Driven Assertion Contract

- Harnesses/adapters own target subject extraction and normalization.
- Assertion applicability is determined by subject availability/shape.
- Projected subjects consumed by spec-lang MUST be JSON values; native/runtime
  structures MUST be represented by JSON profile envelopes.
- External operators (`contain`, `regex`, `json_type`, `exists`) are authoring
  sugar that compile to `evaluate`-equivalent predicates.
- Runtime pass/fail decisions MUST execute compiled predicates through the
  spec-lang evaluator.

Subject profile envelope contract:

- `docs/spec/contract/20_subject_profiles_v1.md`

## Spec-Lang Reuse

- `harness.spec_lang.includes` MAY provide ordered library docs/files
  containing `type: spec_lang.library` reusable function definitions.
- `harness.spec_lang.exports` MAY constrain visible imported symbols to an
  explicit allowlist.
- `harness.spec_lang.imports` MAY declare case-scoped imports using
  `from: std.<namespace>` and `names: [...]` with optional `as` aliases.

## Orchestration Tooling

- `type: orchestration.run` uses `harness.orchestration` for runner tool
  dispatch contracts.
- tool definitions are registry-backed per implementation:
  - `docs/spec/tools/python/tools_v1.yaml`
  - `docs/spec/tools/rust/tools_v1.yaml`
- `effect_symbol` naming MUST use deep-dot `ops.*` hierarchy:
  `ops.<segment>(.<segment>)+`
  (for example `ops.fs.file.read`, `ops.time.clock.now_utc`,
  `ops.proc.command.exec`).
- legacy underscore forms are forbidden.

## Docs Generation Harness

- `type: docs.generate` uses `harness.docs_generate` for spec-driven docs
  generation surfaces.
- `surface_id` MUST resolve to a declared docs generator surface in
  `docs/spec/schema/docs_generator_registry_v1.yaml`.
- output behavior is explicit: `output_mode` is `markers` or `full_file`.
- marker mode writes only inside generated marker boundaries.
- template rendering uses moustache-core semantics and declared data sources
  (`json_file`, `yaml_file`, `generated_artifact`, `command_output`).

## Path Safety

- `cli.run` `harness.setup_files[*].path` MUST be relative and MUST resolve
  within the runner temp directory.
- spec-authored contract paths use virtual-root semantics:
  `/` means contract root (not OS root).
- root-relative values normalize to canonical `/...`.
- `text.file` `path` MUST resolve within contract root; `..` escapes are
  invalid.
- external references are `external://provider/id` and are deny-by-default
  unless explicitly enabled by capability + harness external ref policy.

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
