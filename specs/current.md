# Current Spec Snapshot

Source of truth: spec.current

Spec-Version: 1
Date: 2026-02-18

## Canonical Model

- Executable fence: `yaml contract-spec`
- Executable case types: `contract.check`, `contract.export`, `contract.job`
- Assertion root: `contract`
- Assertion step shape: `contract.steps[].assert` (mapping or list of expression mappings)
- Assertion imports: `contract.imports` with per-step overrides at `contract.steps[].imports`
- Contract step metadata: `required` (default `true`), `priority` (default `1`), `severity` (default `1`)
- Hook root and events: `when.required|when.optional|when.fail|when.complete`
- Producer exports: `harness.exports`
- Consumer imports: `harness.use[*].symbols`
- Job metadata and dispatch: `harness.jobs` + `ops.job.dispatch`
- Bundle taxonomy: `bundle -> domains[] -> modules[] -> contracts[]` with canonical metadata
  names `bundle_version` and `maintainers`
- Runner sync task contract: required task IDs are `bundle-sync` and `bundle-sync-check`

## Canonical Specs

- `/specs/schema/schema_v1.md`
- `/specs/contract/index.md`
- `/specs/governance/index.md`
- `/specs/libraries/index.md`
- `runner-owned implementation specs/index.md`

## Derived Docs

Generated references in `/docs/book/9*.md` are derived from canonical spec sources and must be regenerated when contracts or governance catalogs change.

## Runtime Profiling Snapshot

- `run_trace_v1` contract snapshot is defined in `/specs/schema/run_trace_v1.yaml`.
