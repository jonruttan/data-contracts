# PHP Implementation Notes

Target implementation: PHP + PHPUnit (Laravel test environment).

Guidance:

- Implement contract behavior from `docs/spec/contract/`.
- Validate parity using conformance fixtures and report format docs.
- Keep PHP-specific runtime concerns in this file only.

## Bootstrap Runner

Bootstrap script path:

- `scripts/php/conformance_runner.php`

Runtime requirement:

- PHP `yaml_parse` extension (for structured fixture parsing)

Current bootstrap behavior:

- Reads case inputs from Markdown spec docs (`*.spec.md`)
- For Markdown docs, parses fenced `spec-test` YAML blocks
  (backticks or tildes, matching Python fence/token rules)
- Executes `text.file` cases with:
  - `must`, `can`, `cannot` groups
  - `contain` and `regex` operators
  - `assert_health.mode` validation (`ignore`/`warn`/`error`)
  - `AH005` non-portable-regex diagnostics in `error` mode
- Emits report JSON envelope:
  - `version: 1`
  - `results: [{id,status,category,message}]`
- Marks unsupported types as `runtime` failures

Example:

```sh
php scripts/php/conformance_runner.php \
  --cases fixtures/conformance/cases/php-text-file-subset.spec.md \
  --out .artifacts/php-conformance-report.json
```

Validate the produced report against the Python contract validator:

```sh
python3 scripts/validate_conformance_report.py .artifacts/php-conformance-report.json
```

Bootstrap parity subset fixture:

- `fixtures/conformance/cases/php-text-file-subset.spec.md`
