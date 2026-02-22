# Chapter 10: Getting Started

```yaml doc-meta
doc_id: DOC-REF-110
title: Chapter 10 Getting Started
status: active
audience: author
owns_tokens:
- getting_started_control_plane_flow
requires_tokens:
- spec_purpose_foundation
commands:
- run: ./scripts/ci_gate.sh
  purpose: Run control-plane gate checks for this repository.
examples:
- id: EX-GETTING-STARTED-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Provide a short launch path for users who need to understand and use the `data-contracts` control plane.

## Inputs

- this repository checkout
- intent to author/review contract, schema, docs, or governance changes

## Outputs

- clear task path to specs/docs/governance usage
- first successful control-plane check run

## Failure Modes

- assuming this repository owns runtime execution
- starting from generated references before core narrative chapters
- skipping usage guides and relying on implicit workflow knowledge

## Start Here

1. Read `/Users/jon/Workspace/Development/data-contracts/docs/book/05_what_is_data_contracts.md`.
2. Read `/Users/jon/Workspace/Development/data-contracts/docs/book/15_spec_lifecycle.md`.
3. Read `/Users/jon/Workspace/Development/data-contracts/docs/book/25_system_topology.md`.
4. Open `/Users/jon/Workspace/Development/data-contracts/docs/book/35_usage_guides_index.md` and choose a task path.

## First Command

```sh
./scripts/ci_gate.sh
```

## Runner Test Packs

- `/Users/jon/Workspace/Development/data-contracts/specs/00_core/packs/runner_contract_pack_v1.yaml`
- `/Users/jon/Workspace/Development/data-contracts/specs/00_core/packs/spec_core_maintenance_pack_v1.yaml`
- `/Users/jon/Workspace/Development/data-contracts/specs/00_core/packs/project_docs_maintenance_pack_v1.yaml`
