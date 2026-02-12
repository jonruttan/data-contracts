# Conformance Cases

Case fixtures that portable runner implementations execute.

Recommendations:

- Keep case ids stable.
- Prefer small, focused cases per behavior.
- Include both pass and fail cases.
- Use Markdown `.spec.md` files with fenced `yaml spec-test` blocks.
- Prefer inline expectations via:
  - `expect.portable`
  - optional `expect.impl.<runtime>` overrides
- Conformance fixture cases should always include `expect.portable.status`.
- Style details are defined in `docs/spec/conformance/style.md`.
