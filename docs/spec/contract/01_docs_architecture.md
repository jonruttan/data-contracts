# Docs Architecture Contract

Source of truth: spec.contract.docs_architecture

## Canonical Ownership

- `/docs/spec/current.md` is the active model snapshot entrypoint.
- `/docs/spec/schema/**` owns case-shape, schema registry, and profile contracts.
- `/docs/spec/contract/**` owns normative policy/traceability contracts.
- `/docs/spec/governance/**` owns executable governance checks.
- `/docs/spec/libraries/**` owns reusable spec-lang library surfaces.
- `/docs/spec/impl/**` owns implementation fixture suites.

## Generated References

Generated appendices in `/docs/book/9*.md` are derived artifacts and must be regenerated from canonical sources.

## Non-canonical Historical Content

- `/docs/history/**` is archival and non-canonical.
