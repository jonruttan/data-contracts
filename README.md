# Data Contracts

`data-contracts` is the implementation-agnostic control plane for the Data Contracts ecosystem.

It defines and governs:
- canonical specs, contracts, and schemas
- documentation and reader-facing guidance
- compatibility/status telemetry ingestion and policy evaluation

It does **not** own runner implementation code and does **not** execute runtime lanes as canonical project behavior.

## What This Project Is

- Source of truth for contract semantics and schema shape.
- Source of truth for docs quality, information architecture, and governance checks.
- Consumer of runner release telemetry via status exchange artifacts.

## What This Project Is Not

- Not a runtime implementation repository.
- Not a required-lane executor.
- Not the owner of runner internals (`dc-runner-rust`, `dc-runner-python`, `dc-runner-php`).

## How Users Use This Project

### 1) Author a spec change
- Start with `/Users/jon/Workspace/Development/data-contracts/docs/book/index.md`
- Use task guides at `/Users/jon/Workspace/Development/data-contracts/docs/book/35_usage_guides_index.md`
- Validate contract and schema intent under `/Users/jon/Workspace/Development/data-contracts/specs/contract/index.md`

### 2) Validate docs and contract coherence
- Run control-plane checks through CI and governance surfaces in this repo.
- Use `/Users/jon/Workspace/Development/data-contracts/docs/book/90_reference_guide.md` for narrative-to-normative mapping.

### 3) Read compatibility and status telemetry
- See `/Users/jon/Workspace/Development/data-contracts/docs/book/65_runner_status_and_compatibility.md`
- Inspect generated ingest artifacts under `/.artifacts/runner-status-*`

### 4) Debug governance or documentation drift
- Use troubleshooting and governance chapters in the docs book.
- Inspect generated governance/docs summary artifacts from CI.

## Canonical Entry Points

- Book index: `/Users/jon/Workspace/Development/data-contracts/docs/book/index.md`
- Usage guides index: `/Users/jon/Workspace/Development/data-contracts/docs/book/35_usage_guides_index.md`
- Status exchange and compatibility: `/Users/jon/Workspace/Development/data-contracts/docs/book/65_runner_status_and_compatibility.md`
- Contract index: `/Users/jon/Workspace/Development/data-contracts/specs/contract/index.md`
