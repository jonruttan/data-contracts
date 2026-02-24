# Review Snapshot

Date: 2026-02-13
Model: codex-gpt5
Prompt: `docs/history/reviews/prompts/adoption_7_personas.md`
Prompt revision: 678376d
Repo revision: 678376d
Contract baseline refs:
- /specs/01_schema/review_snapshot_schema_v1.yaml
- /specs/02_contracts/26_review_output_contract.md
- /specs/01_schema/schema_v1.md
Runner lane: governance

## Scope Notes

- Reviewed stale `data-contracts` review namespace docs under `docs/history/reviews`.
- Focused on contract alignment, workflow discoverability, and commandability.
- Main objective: identify gaps where current review assets still assume prior project state.

## Command Execution Log

| command | status | exit_code | stdout_stderr_summary |
| --- | --- | --- | --- |
| `rg --files docs/history/reviews` | success | 0 | Listed all active review assets and historical snapshots. |
| `sed -n '1,260p' docs/history/reviews/index.md` | success | 0 | Confirmed index referenced a missing `README.md`. |
| `dc-runner critical-gate` | failure | 1 | Failed: `runtime.critical_check_set_manifest_required` (`manifest.invalid`) using bundled checks. |
| `dc-runner --spec-source workspace governance run` | success | 0 | Workspace governance run checks passed. |
| `dc-runner docs-generate-check` | success | 0 | Job checks passed. |
| `dc-runner review-validate --snapshot docs/history/reviews/snapshots/2026-02-13_persona-review.md` | failure | 2 | Subcommand unavailable in this runner version (`unrecognized subcommand`). |

## Findings

| Severity | Verified/Hypothesis | File:Line | What | Why | When | Proposed fix |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | Verified | docs/history/reviews/index.md | Missing index target in active scope list | README path did not exist and conflicts with docs namespace policy. | during discovery | Remove nonexistent reference and clarify namespace. |
| P1 | Verified | docs/history/reviews/prompts/adoption_7_personas.md | Prompt context still framed around `spec_runner` | Review command guidance drifted from current control-plane model. | during review | Replace references with `data-contracts` control-plane flow and schema contract docs. |
| P2 | Hypothesis | docs/history/reviews/templates/review_snapshot.md | Template omitted schema-required sections and field coverage | Would break review validation checks and tooling contract sync. | during review artifact generation | Align template with `26_review_output_contract.md` and `review_snapshot_schema_v1.yaml`.
| P2 | Hypothesis | docs/history/reviews/snapshots/2026-02-13_persona-review.md | Snapshot output shape was legacy | Tooling expects canonical section order and required metadata fields. | before this update | Reformat snapshot output to canonical section order and candidate schema.

## Synthesis

`data-contracts` is a control-plane-first executable-specs system: the repository governs
contract language, schemas, and governance while runner implementations execute in
external lanes.

- North-star: keep review, governance, and conformance signals deterministic,
  runnable, and auditable across all repository changes.
- 10 highest-value spec items to add next:
  1. Clarify active review workflow contract in `docs/development.md`.
  2. Add explicit review namespace ownership surface in `docs/book` reference map.
  3. Define a review command matrix in one canonical table.
  4. Add snapshot retention policy for dated outputs.
  5. Require explicit `Contract baseline refs` in every review snapshot.
  6. Document expected `Runner lane` values and usage.
  7. Add a minimal machine-readable review artifact parser contract test.
  8. Add guidance for non-interactive snapshot generation.
  9. Define acceptance criteria for discovery prompt output completeness.
  10. Add a glossary for governance check IDs used in snapshots.
- 5 biggest risks:
  1. Stale review artifacts drift into active tooling paths.
  2. Divergent snapshot shapes reducing validation coverage.
  3. Command output inconsistency across lanes.
  4. Human-facing prompts carrying outdated project names/assumptions.
  5. Missing explicit output contract references in prompts.
- Definition of done for publishable v1:
  - Canonical review workflow and snapshot template pass all governance checks.
  - Discovery prompts, templates, and snapshots validate against contract schema.
  - Command execution evidence is included with statuses and exit codes.
  - No active references to removed/renamed artifacts.

## Spec Candidates (YAML)

```yaml
- id: DOCS-REV-0001
  title: Clarify review namespace active paths and governance expectations
  type: docs
  class: docs
  target_area: docs/history/reviews/index.md
  acceptance_criteria:
    - index.md contains only existing canonical paths.
    - discovery workflow references both prompts and snapshots.
  affected_paths:
    - docs/history/reviews/index.md
  risk: medium
- id: DOCS-REV-0002
  title: Replace obsolete spec_runner references in review prompts
  type: docs
  class: docs
  target_area: docs/history/reviews/prompts
  acceptance_criteria:
    - no prompt file references `spec_runner` as active repository name.
    - prompts reference `data-contracts` contracts/schema docs.
  affected_paths:
    - docs/history/reviews/prompts/adoption_7_personas.md
    - docs/history/reviews/prompts/self_healing.md
  risk: high
- id: DOCS-REV-0003
  title: Align template with review snapshot schema
  type: docs
  class: docs
  target_area: docs/history/reviews/templates/review_snapshot.md
  acceptance_criteria:
    - required sections are present and ordered.
    - command execution table uses required header fields.
  affected_paths:
    - docs/history/reviews/templates/review_snapshot.md
  risk: medium
- id: DOCS-REV-0004
  title: Add canonical output contract references in snapshots
  type: tooling
  class: tooling
  target_area: docs/history/reviews/snapshots
  acceptance_criteria:
    - every snapshot includes Contract baseline refs and Runner lane.
    - findings section uses required table headers.
  affected_paths:
    - docs/history/reviews/snapshots/2026-02-13_persona-review.md
  risk: medium
- id: DOCS-REV-0005
  title: Keep snapshot template pointer accurate
  type: docs
  class: docs
  target_area: docs/history/reviews/template.md
  acceptance_criteria:
    - pointer text does not mention missing canonical README.
  affected_paths:
    - docs/history/reviews/template.md
  risk: low
- id: DOCS-REV-0006
  title: Clarify hardening pipeline compatibility path
  type: tooling
  class: tooling
  target_area: docs/history/reviews/frameworks/hardening_pipeline.md
  acceptance_criteria:
    - framework file points to active self-healing prompt.
    - wording stays compatibility-only for historical references.
  affected_paths:
    - docs/history/reviews/frameworks/hardening_pipeline.md
  risk: low
- id: DOCS-REV-0007
  title: Add review workflow discoverability check in docs references
  type: tooling
  class: tooling
  target_area: docs/book
  acceptance_criteria:
    - reference manifest includes review namespace location.
    - guides map to discovery workflow commands.
  affected_paths:
    - docs/book/reference_guide.md
  risk: medium
- id: DOCS-REV-0008
  title: Standardize review command expectations
  type: tooling
  class: tooling
  target_area: docs/development.md
  acceptance_criteria:
    - include primary command line checks (`critical-gate`, `governance`, `docs-generate-check`).
  affected_paths:
    - docs/development.md
  risk: medium
- id: DOCS-REV-0009
  title: Validate snapshot artifacts in governance pack
  type: tooling
  class: tooling
  target_area: specs/04_governance/cases/core/project_docs
  acceptance_criteria:
    - docs.review_snapshots_schema_valid remains pass.
    - discovery workflow sync references active paths.
  affected_paths:
    - specs/04_governance/cases/core/project_docs/docs_review_snapshots_schema_valid.spec.md
    - specs/04_governance/cases/core/project_docs/docs_reviews_discovery_workflow_sync.spec.md
  risk: high
- id: DOCS-REV-0010
  title: Keep review prompts in sync with schema snapshot
  type: docs
  class: docs
  target_area: docs/history/reviews/prompts
  acceptance_criteria:
    - prompt schema contract check passes for discovery and adoption prompts.
    - output expectations remain machine-readable.
  affected_paths:
    - docs/history/reviews/prompts/adoption_7_personas.md
    - docs/history/reviews/prompts/self_healing.md
  risk: medium
```

## Classification Labels

- DOCS-REV-0001: docs
- DOCS-REV-0002: docs
- DOCS-REV-0003: docs
- DOCS-REV-0004: tooling
- DOCS-REV-0005: docs
- DOCS-REV-0006: tooling
- DOCS-REV-0007: docs
- DOCS-REV-0008: tooling
- DOCS-REV-0009: tooling
- DOCS-REV-0010: docs

## Reject / Defer List

- Add a UI dashboard before command-line validation is stable.
- Replace `dc-runner` with a new CLI wrapper for review snapshots.
- Introduce custom YAML schema beyond `specs/01_schema/schema_v1.md`.
- Add repository-specific review tooling outside `data-contracts` governance checks.
- Expand review output fields without matching governance contract updates.

## Raw Output

Paste the full AI output here. Do not edit it beyond formatting fixes.
