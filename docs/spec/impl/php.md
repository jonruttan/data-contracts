# PHP Implementation Notes

Target implementation: PHP + PHPUnit (Laravel test environment).

Guidance:

- Implement contract behavior from `docs/spec/contract/`.
- Validate parity using conformance fixtures and report format docs.
- Keep PHP-specific runtime concerns in this file only.

## Bootstrap Runner

Conformance bootstrap script path:

- `scripts/php/conformance_runner.php`

Alternate runner script path:

- `scripts/php/spec_runner.php`

Fixture-driven runner suites:

- `docs/spec/impl/php/cases/runner-pass.spec.md`
- `docs/spec/impl/php/cases/runner-failures.spec.md`

Runtime requirement:

- PHP `yaml_parse` extension (for structured fixture parsing)

Current bootstrap behavior:

- Reads case inputs from Markdown spec docs (`*.md`)
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
  --cases docs/spec/conformance/cases/php-text-file-subset.spec.md \
  --out .artifacts/php-conformance-report.json
```

Validate the produced report against the Python contract validator:

```sh
python3 scripts/validate_conformance_report.py .artifacts/php-conformance-report.json
```

Bootstrap parity subset fixture:

- `docs/spec/conformance/cases/php-text-file-subset.spec.md`

## Alternate Runner Behavior (`spec_runner.php`)

- Reads Markdown case files (`*.md`) from a directory or a single file path.
- Executes core case types:
  - `text.file`
  - `cli.run`
- Supports `text.file.path` with the same relative-path and contract-root
  escape checks used by the Python runner.
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
