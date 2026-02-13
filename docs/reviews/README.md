# Reviews

This folder holds review assets with clear lifecycle separation.

## Structure

- `prompts/`: reusable review prompts.
- `frameworks/`: review/hardening frameworks used during development.
- `snapshots/`: dated, immutable outputs from review runs.
- `templates/`: snapshot templates and helper formats.

## Current Canonical Files

- Prompt: `docs/reviews/prompts/adoption_7_personas.md`
- Self-healing prompt: `docs/reviews/prompts/self_healing.md`
- Snapshot template: `docs/reviews/templates/review_snapshot.md`
- Hardening framework: `docs/reviews/frameworks/hardening_pipeline.md`

## Workflow

1. Run either `adoption_7_personas.md` (critique) or `self_healing.md` (staged hardening) from `docs/reviews/prompts/`.
2. Save raw output under `docs/reviews/snapshots/` using a dated filename.
3. Convert snapshot output into pending specs with:
   - `python scripts/review_to_pending.py docs/reviews/snapshots/<file>.md`
4. Triage resulting pending items and promote selected candidates into
   `docs/spec/backlog.md` or directly into `docs/spec/*.md`.
5. Record `Prompt revision` and `Repo revision` in each snapshot.

## Automation Helpers

Create a dated snapshot stub with revisions prefilled:

```sh
python scripts/new_review_snapshot.py --label persona_review
```

Extract explicit YAML spec candidates and infer implicit suggestions:

```sh
python scripts/review_to_pending.py docs/reviews/snapshots/<snapshot>.md
```

## Recommended Cadence

- Persona review: run anytime; use extraction script to feed pending specs.
- Hardening framework: run when actively fixing quality/reliability issues.
- Final boss review: run near release/merge readiness for high-signal blockers.
