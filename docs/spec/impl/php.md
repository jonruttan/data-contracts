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

- Reads fixtures from `fixtures/conformance/cases/*.yaml`
- Executes `text.file` cases with:
  - `must` groups
  - `contain` and `regex` operators
- Emits report JSON envelope:
  - `version: 1`
  - `results: [{id,status,category,message}]`
- Marks unsupported types as `runtime` failures

Example:

```sh
php scripts/php/conformance_runner.php \
  --cases fixtures/conformance/cases/php-text-file-subset.yaml \
  --out .artifacts/php-conformance-report.json
```

Validate the produced report against the Python contract validator:

```sh
python3 scripts/validate_conformance_report.py .artifacts/php-conformance-report.json
```

Bootstrap parity subset fixture:

- `fixtures/conformance/cases/php-text-file-subset.yaml`
- `fixtures/conformance/expected/php-text-file-subset.yaml`
