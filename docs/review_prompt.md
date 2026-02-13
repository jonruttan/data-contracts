# Review Prompt

Use this prompt to solicit brutally honest feedback on `spec_runner` as a
publishable, reusable tool.

Before running the review, point the reviewer to:

- `docs/spec/schema/schema-v1.md`
- `docs/spec/contract/`
- `docs/spec/conformance/`

Ask for findings as:

- `Severity | File:Line | What | Why | Fix`

- Review the schema and stability guarantees.
- Review extensibility approach (kinds/harnesses).
- Review documentation quality and “time-to-first-win”.
- Identify missing contracts and sharp edges.
