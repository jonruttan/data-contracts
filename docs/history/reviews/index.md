# Reviews Namespace

`docs/history/reviews` is the canonical review workflow namespace for the
`data-contracts` control-plane repository, plus historical review artifacts.

## Canonical Active Scope

- `/docs/history/reviews/index.md`: this file.
- `/docs/history/reviews/prompts/`: active review prompts (adoption + self-healing)
  used for discovery and periodic hardening checks.
- `/docs/history/reviews/templates/review_snapshot.md`: canonical machine-consumable
  review snapshot template.
- `/docs/history/reviews/frameworks/`: compatibility pointers for historical
  workflow names.
- `/docs/history/reviews/snapshots/`: dated review outputs and current canonical
  snapshots.

## Discovery and Pending-Conversion Workflow

- Use prompts under `prompts/` as active review entrypoints.
- Render outputs into `snapshots/` using `templates/review_snapshot.md`.
- Keep dated outputs for provenance while keeping the active template and prompt
  surfaces in sync.

## Archive Contents

- `prompts/`: active prompt files and historical prompt iterations.
- `frameworks/`: compatibility pointers and legacy names.
- `templates/`: canonical active template plus historical scaffolding references.
- `snapshots/`: active and historical review outputs.
