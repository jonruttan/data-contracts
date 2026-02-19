# Reviews

This directory contains active review assets for project-aligned critiques and hardening passes.

## Structure

- `prompts/`: reusable prompts
- `snapshots/`: dated immutable outputs
- `templates/`: snapshot templates and output contract scaffolds

## Canonical Prompt Set

- Adoption/persona review:
  - `docs/reviews/prompts/adoption_7_personas.md`
- Self-healing staged hardening:
  - `docs/reviews/prompts/self_healing.md`
- Final gatekeeper review:
  - `docs/reviews/prompts/final_boss_gatekeeper.md`

## Workflow

1. Choose a prompt from `docs/reviews/prompts/`.
2. Produce a dated snapshot in `docs/reviews/snapshots/`.
3. Preserve raw output and include required metadata from the snapshot template.
4. Derive pending/governance candidates from the structured sections.
5. Promote selected candidates into canonical spec/governance surfaces under `specs/`.

## Snapshot Metadata (required)

Every snapshot should include:
- `Prompt`
- `Prompt revision`
- `Repo revision`
- `Contract baseline refs`
- `Runner lane`

Use:
- `docs/reviews/templates/review_snapshot.md`

## Output Contract Policy

Active review prompts require strict machine-consumable sections:
- stable heading order
- structured findings tables
- explicit `Verified/Hypothesis` evidence tagging
- deterministic command execution logs

This is required so review outputs can be transformed into pending/governance candidates without manual reinterpretation.

## Contract Alignment Expectations

All active reviews should align to current project contracts:
- `/specs/schema/schema_v1.md`
- `/specs/contract/12_runner_interface.md`
- `/specs/contract/25_compatibility_matrix.md`
- `/specs/governance/check_sets_v1.yaml`
- `/specs/schema/runner_certification_registry_v1.yaml`

Runtime lane policy in active reviews:
- required blocking lane: rust
- compatibility non-blocking lanes: python/php/node/c
