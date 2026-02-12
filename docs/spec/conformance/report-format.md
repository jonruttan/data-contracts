# Conformance Report Format

Implementations SHOULD emit machine-readable case outcomes with:

- `id`
- `status` (`pass`/`fail`)
- `category` (`schema`/`assertion`/`runtime`, or `null` for `pass`)
- `message` (optional, implementation-specific)

When `status=fail`, `message` SHOULD include assertion context tokens when
available (`case_id`, `assert_path`, and optionally `target`/`op`).

Comparison for parity should key on `id`, `status`, and `category`.
