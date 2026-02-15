# PHP Implementation Notes

Target implementation: PHP + PHPUnit (Laravel test environment).

Guidance:

- Implement contract behavior from `docs/spec/contract/`.
- Validate parity using conformance fixtures and report format docs.
- Keep PHP-specific runtime concerns in this file only.

## Supported Flags

Conformance runner (`scripts/php/conformance_runner.php`) flags:

- `--help` / `-h`: print usage and exit `0`.
- `--cases` (required): case file or directory path.
- `--out` (required): JSON report output path.
- `--case-file-pattern` (default: `*.spec.md`): directory-mode case glob.
- `--case-formats` (default: `md`): comma-separated formats (`md,yaml,json`).

Alternate runner (`scripts/php/spec_runner.php`) flags:

- `--help` / `-h`: print usage and exit `0`.
- `--cases` (required): case file or directory path.
- `--out` (required): JSON report output path.
- `--case-file-pattern` (default: `*.spec.md`): directory-mode case glob.
- `--case-formats` (default: `md`): comma-separated formats (`md,yaml,json`).

## Default Behavior

- discovery default is Markdown-only (`md`) with case pattern `*.spec.md`.
- conformance runner writes report JSON even when case-level failures exist.
- alternate runner exits non-zero when any case fails.
- assertion runtime follows universal `evaluate` core semantics:
  - `contain` / `regex` / `json_type` / `exists` are compile-only sugar
  - runtime pass/fail uses compiled spec-lang predicates
  - target/type applicability is enforced by subject availability and shape

## Opt-In Behavior

- external formats (`yaml`, `json`) require explicit `--case-formats`.
- process env allowlisting can be enabled with `SPEC_RUNNER_ENV_ALLOWLIST`.
- `SPEC_RUNNER_ENTRYPOINT` fallback may be used when `harness.entrypoint` is
  omitted.

## Failure Mode Notes

- CLI usage/argument validation errors return exit code `2`.
- conformance runner runtime bootstrap failures return exit code `1`.
- alternate runner returns exit code `1` for runtime errors or failing cases.
- missing PHP `yaml_parse` extension is a runtime failure.

## Bootstrap Runner

Conformance bootstrap script path:

- `scripts/php/conformance_runner.php`

Alternate runner script path:

- `scripts/php/spec_runner.php`

Fixture-driven runner suites:

- `docs/spec/impl/php/cases/runner_pass.spec.md`
- `docs/spec/impl/php/cases/runner_failures.spec.md`

Runtime requirement:

- PHP `yaml_parse` extension (for structured fixture parsing)

Current bootstrap behavior:

- Reads case inputs from Markdown spec docs matching the default
  case-file pattern
- For Markdown docs, parses fenced `spec-test` YAML blocks
  (backticks or tildes, matching Python fence/token rules)
- Executes `text.file` cases with:
  - default subject from the containing spec document
  - optional `path` (relative to spec doc)
  - contract-root escape protection for `path`
  - `must`, `can`, `cannot` groups
  - `contain` and `regex` operators
  - `assert_health.mode` validation (`ignore`/`warn`/`error`)
  - assertion-health diagnostics `AH001`..`AH005`
  - `warn` mode emits `WARN: ASSERT_HEALTH ...` lines on stderr
- Emits report JSON envelope:
  - `version: 1`
  - `results: [{id,status,category,message}]`
- Marks unsupported types as `runtime` failures

Example:

```sh
php scripts/php/conformance_runner.php \
  --cases docs/spec/conformance/cases/php_text_file_subset.spec.md \
  --out .artifacts/php-conformance-report.json
```

Validate the produced report against the Python contract validator:

```sh
python3 scripts/validate_conformance_report.py .artifacts/php-conformance-report.json
```

Bootstrap parity subset fixture:

- `docs/spec/conformance/cases/php_text_file_subset.spec.md`

## Alternate Runner Behavior (`spec_runner.php`)

- Reads Markdown case files from a directory or single file path using
  case-file pattern, overrideable via
  `--case-file-pattern`.
- Default discovery format is Markdown (`md`); opt-in formats are available via
  `--case-formats md,yaml,json` (default: `md`).
- Executes core case types:
  - `text.file`
  - `cli.run`
- Supports `text.file.path` with the same relative-path and contract-root
  escape checks used by the Python runner.
- Keeps assertion behavior parity with Python by compiling external operators to
  spec-lang and evaluating one predicate path.
- Supports `cli.run` harness keys:
  - `entrypoint` (or `SPEC_RUNNER_ENTRYPOINT` fallback)
  - `env` (set/unset command environment variables)
- Supports process env allowlisting for `cli.run` via:
  - `SPEC_RUNNER_ENV_ALLOWLIST=K1,K2,...`
    (only allowlisted ambient env vars are inherited by subprocesses)
- Emits report JSON: `{version: 1, results: [{id,status,category,message}]}`.
- Exits non-zero when any case fails.

Example:

```sh
php scripts/php/spec_runner.php \
  --cases docs/spec/conformance/cases \
  --out .artifacts/php-spec-runner-report.json
```

To run the implementation-owned fixture suites:

```sh
php scripts/php/spec_runner.php \
  --cases docs/spec/impl/php/cases \
  --out .artifacts/php-spec-runner-impl-report.json
```

## Remaining Work To Reach Full Runner

- Expand `cli.run` harness parity (`stdin`, setup files, import stubs, hooks)
  if those features are needed for PHP-driven specs.
- Add implementation-owned adapter/harness strategy for project-specific PHP
  systems under test.
- Decide whether conformance capability map should promote `cli.run` from
  `skip` to executable parity for shared fixture sets.
