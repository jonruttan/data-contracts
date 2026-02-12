# PHP Implementation Notes

Target implementation: PHP + PHPUnit (Laravel test environment).

Guidance:

- Implement contract behavior from `docs/spec/contract/`.
- Validate parity using conformance fixtures and report format docs.
- Keep PHP-specific runtime concerns in this file only.

## Bootstrap Runner

Bootstrap script path:

- `scripts/php/conformance_runner.php`

Current bootstrap behavior:

- Reads fixture case IDs from `fixtures/conformance/cases/*.yaml`
- Emits report JSON envelope:
  - `version: 1`
  - `results: [{id,status,category,message}]`
- Uses placeholder runtime failures until PHP parser/assertion parity is built

Example:

```sh
php scripts/php/conformance_runner.php \
  --cases fixtures/conformance/cases \
  --out .artifacts/php-conformance-report.json
```

Validate the produced report against the Python contract validator:

```sh
python3 scripts/validate_conformance_report.py .artifacts/php-conformance-report.json
```
