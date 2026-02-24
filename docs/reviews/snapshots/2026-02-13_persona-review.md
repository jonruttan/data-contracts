# Review Snapshot

Date: 2026-02-13
Model: codex-gpt5
Prompt: `/specs/07_runner_behavior/review_workflow/prompts/adoption_7_personas.spec.md`
Prompt revision: 6d8f0c2
Repo revision: 6d8f0c2
Contract baseline refs:
- /specs/01_schema/review_snapshot_schema_v1.yaml
- /specs/02_contracts/26_review_output_contract.md
Runner lane: governance

## Scope Notes

- Reviewed `data-contracts` review assets and the newly decoupled canonical review workflow pathing.
- Focus areas: control-plane review prompts, snapshot template alignment, and compatibility pointers.

## Command Execution Log

| command | status | exit_code | stdout_stderr_summary |
| --- | --- | --- | --- |
| `rg --files docs/reviews` | success | 0 | Listed active review namespace, prompts, templates, and snapshots. |
| `dc-runner critical-gate` | failure | 1 | Fails current environment for an unrelated `manifest.invalid` dependency issue. |
| `dc-runner governance` | success | 0 | Governance checks passed. |
| `dc-runner docs-generate-check` | success | 0 | Documentation checks passed. |
| `dc-runner --spec-source workspace critical-gate` | skipped | - | Skipped while validating pointer migration only. |

## Findings

| Severity | Verified/Hypothesis | File:Line | What | Why | When | Proposed fix |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | Verified | docs/reviews/index.md | Active namespace was documented as project-anchored without explicit library source pointers | Prompt and template ownership had drifted to local copies while project wanted canonical library source | discovery | Point index and pointer files to `data-contracts-library` canonical workflow assets and document no-install flow. |
| P2 | Verified | docs/reviews/prompts/adoption_7_personas.md | Local prompt text duplicated canonical logic | Duplicate maintenance burden risks divergence from canonical prompt contracts | ongoing review operation | Keep as a compatibility pointer and route runtime rendering through library prompt template. |
| P2 | Verified | docs/reviews/templates/review_snapshot.md | Snapshot template content drifted from canonical shape | Canonical schema compliance checks depend on exact section set and command table header | artifact generation | Keep this file as a pointer to `/specs/07_runner_behavior/review_workflow/templates/review_snapshot.spec.md`. |
| P2 | Verified | docs/reviews/snapshots/2026-02-13_persona-review.md | Review-validate command usage documented a removed subcommand | Tooling output must reflect current command behavior | historical report capture | Update to current command contract and keep evidence of unavailable command optional. |

## Synthesis

`data-contracts` should treat review prompts and snapshot templates as canonical, reusable library assets and use local `docs/reviews/*` files only as discoverability bridges.

- North-star: keep review instructions templated, versioned, and runnable without touching core project docs for every repository variation.
- 10 highest-value spec items to add next:
  1. Project-level vars file template with required schema validation.
  2. CLI helper contract docs for render/run flow.
  3. Discovery workflow examples for `project_vars.yaml` + CLI overrides.
  4. Stable snapshot-output post-processing checks.
  5. Bundle lifecycle docs for review workflow assets.
  6. Contract tests for prompt variable map completeness.
  7. Endpoint schema examples for render/run workflows.
  8. Bundle smoke test harness for local workspace execution.
  9. Unresolved-template-key diagnostics contract.
  10. Baseline command matrix per review type.
- 5 biggest risks:
  1. Template variable drift across forks.
  2. Snapshot schema mismatch on downstream project updates.
  3. Hidden assumptions in runner checks due variable omission.
  4. Undeclared command override precedence.
  5. Governance checks expecting local template shape while pointers are introduced.
- Definition of done:
  - Local prompts and template files are canonical pointers.
  - Review output validates against snapshot schema and contract.
  - Render/run flow is documented with a deterministic variable contract.

## Spec Candidates (YAML)

```yaml
- id: DOCS-REV-2026-01
  title: Decouple review prompts and snapshot template from project docs
  type: docs
  class: docs
  target_area: docs/reviews
  acceptance_criteria:
    - local review prompt files contain canonical pointer references
    - review workflow documentation links to library assets
    - snapshot example points to canonical template schema
  affected_paths:
    - docs/reviews/index.md
    - docs/reviews/prompts/adoption_7_personas.md
    - docs/reviews/prompts/self_healing.md
    - docs/reviews/templates/review_snapshot.md
    - docs/reviews/frameworks/hardening_pipeline.md
  risk: high
```

## Classification Labels

- DOCS-REV-2026-01: docs

## Reject / Defer List

- Add runtime review UI before prompt-template contract completion.
- Add repository-specific prompt copies before variable support is proven.
- Expand runner command surface before canonical endpoint contracts are stable.
- Introduce a non-schema free-form variable format.
- Add custom retry policies without explicit precedence contracts.

## Raw Output

Rendered snapshot content is documented as part of the discovery workflow and kept
compatible with the canonical review snapshot contract.
