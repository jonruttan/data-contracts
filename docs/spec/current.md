# Current Spec Snapshot

Source of truth: spec.current

Spec-Version: 1
Date: 2026-02-18

## Canonical Model

- Executable fence: `yaml contract-spec`
- Executable case types: `contract.check`, `contract.export`, `contract.job`
- Assertion root: `contract`
- Assertion leaf list key: `asserts`
- Contract class schema: `MUST|MAY|MUST_NOT`
- Hook root and events: `when.must|when.may|when.must_not|when.fail|when.complete`
- Producer exports: `harness.exports`
- Consumer imports: `harness.chain.imports`
- Job metadata and dispatch: `harness.jobs` + `ops.job.dispatch`

## Canonical Specs

- `/docs/spec/schema/schema_v1.md`
- `/docs/spec/contract/index.md`
- `/docs/spec/governance/index.md`
- `/docs/spec/libraries/index.md`
- `/docs/spec/impl/index.md`

## Derived Docs

Generated references in `/docs/book/9*.md` are derived from canonical spec sources and must be regenerated when contracts or governance catalogs change.
