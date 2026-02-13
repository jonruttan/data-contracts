# PHP Runner Fixture Cases

Executable fixture cases for the alternate PHP runner:

- `scripts/php/spec_runner.php`

These files are intentionally `*.spec.md` so behavior expectations live next to
the executable cases.

Files:

- `runner-pass.spec.md`: positive-path runner behavior checks
- `runner-failures.spec.md`: expected schema/assertion/runtime failures
- `fixtures/`: supporting files referenced by `text.file path` and
  `stdout_path_text` checks
