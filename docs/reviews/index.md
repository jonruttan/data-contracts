# Reviews Namespace

`docs/reviews` is the active review workflow namespace for:

- discoverability of review prompts and templates
- historical review artifacts
- compatibility pointers to canonical review workflow assets in `data-contracts-library`

Canonical review artifacts in-repo remain compatibility pointers:

- `/docs/reviews/prompts/` → points to canonical review prompt templates
- `/docs/reviews/templates/review_snapshot.md` → points to canonical snapshot template

Canonical workflow source of truth:

- `/specs/07_runner_behavior/review_workflow/prompts/adoption_7_personas.spec.md`
- `/specs/07_runner_behavior/review_workflow/prompts/self_healing.spec.md`
- `/specs/07_runner_behavior/review_workflow/templates/review_snapshot.spec.md`
- `/specs/07_runner_behavior/review_workflow/review_variables.schema.md`
- `/specs/07_runner_behavior/review_workflow/endpoints/render_prompt.spec.md`
- `/specs/07_runner_behavior/review_workflow/endpoints/run_review_bundle.spec.md`

Active usage paths:

- Prompts (pointer files): `/docs/reviews/prompts/adoption_7_personas.md`, `/docs/reviews/prompts/self_healing.md`
- Snapshot template pointer: `/docs/reviews/templates/review_snapshot.md`
- Snapshot storage: `/docs/reviews/snapshots/`
- Compatibility helper pointer: `/docs/reviews/template.md`
- Compatibility workflow reference: `/docs/reviews/frameworks/hardening_pipeline.md`

Discovery and pending-conversion workflow:

1. Prepare project variables in YAML (example `project_vars.yaml`) and optional `--var` overrides.
2. Render selected prompt via workflow endpoint or local render script.
3. Execute review with selected lane (`docs`, `governance`, `discovery`).
4. Render/write snapshot with the canonical template and keep artifacts under `/docs/reviews/snapshots/`.

## No-install execution workflow

- Use workspace-scoped execution paths to load local review artifacts.
- Prefer bundle + schema references over local hardcoded prompts.
- Canonical bundle id: `data-contracts-library-review-workflow`.
- Example bundle materialization:
  - `cd /Users/jon/Workspace/Development/data-contracts-bundles`
  - `scripts/bundle resolve --runner rust --root data-contracts-library-review-workflow --out /tmp/review-workflow-bundle`
- Endpoint contracts in-library:
  - `/specs/07_runner_behavior/review_workflow/endpoints/render_prompt.spec.md`
  - `/specs/07_runner_behavior/review_workflow/endpoints/run_review_bundle.spec.md`
