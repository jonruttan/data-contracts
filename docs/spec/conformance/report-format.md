# Conformance Report Format

Implementations SHOULD emit machine-readable case outcomes with:

- `id`
- `status` (`pass`/`fail`)
- `category` (`schema`/`assertion`/`runtime`, or `null` for `pass`)
- `message` (optional, implementation-specific)

Comparison for parity should key on `id`, `status`, and `category`.
