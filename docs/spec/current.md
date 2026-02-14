# Current Spec Snapshot

Spec-Version: 1
Date: 2026-02-12

Notes:

- The canonical assertion DSL is `must` / `can` / `cannot` with `contain`,
  `regex`, and `evaluate` (spec-lang v1 list S-expressions).
- `target` is defined on group nodes; leaf assertions are op-only.
- Execution is internal-IR based: external cases compile to spec-lang-backed
  internal predicates before runtime evaluation.
- Canonical authoring remains `.spec.md`; `.spec.yaml/.spec.yml/.spec.json`
  are opt-in external adapter formats.
- Portability reporting includes a segmented self-containment metric across
  conformance/governance/impl `.spec.md` corpora.
- Spec-lang now supports reusable library symbols via
  `harness.spec_lang.library_paths` and optional `exports` allowlists.
- Docs quality v2 adds schema-backed `doc-meta`, manifest-driven reference
  generation, and governance checks for docs token ownership/dependencies and
  generated artifact freshness.

Canonical spec docs:

- `docs/spec/schema/schema_v1.md`
- `docs/spec/contract/`
- `docs/spec/backlog.md`
