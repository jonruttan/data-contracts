# Chapter 10: Getting Started

```yaml doc-meta
doc_id: DOC-REF-110
title: Chapter 10 Getting Started
status: active
audience: author
owns_tokens:
- getting_started_minimal_flow
requires_tokens:
- spec_purpose_foundation
commands:
- run: ./runners/public/runner_adapter.sh --impl rust governance
  purpose: Validate baseline governance before deeper workflows.
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

Provide a short launch page into the spec-first narrative and task guides.

## Inputs

- this repository checkout
- required Rust lane command boundary at `./runners/public/runner_adapter.sh`

## Outputs

- clear first read path
- clear first command sequence

## Failure Modes

- starting with generated references before narrative chapters
- using compatibility lanes as primary merge gate
- skipping guide workflow for task execution

## Start Here

1. Read `docs/book/05_what_is_data_contracts.md`.
2. Read `docs/book/15_spec_lifecycle.md`.
3. Read `docs/book/25_system_topology.md`.
4. Open `docs/book/35_usage_guides_index.md` and choose a task guide.

## First Commands

```bash
./runners/public/runner_adapter.sh --impl rust critical-gate
./runners/public/runner_adapter.sh --impl rust governance
./runners/public/runner_adapter.sh --impl rust docs-generate-check
```

## Next Paths

- New contributor path: `docs/book/guides/guide_01_onboarding.md`
- First authored case path: `docs/book/guides/guide_02_first_spec_authoring.md`
- Maintainer operations path: `docs/book/guides/guide_03_running_checks_and_gates.md`
