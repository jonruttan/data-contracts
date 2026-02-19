# Review Snapshot

Date: 2026-02-19
Model: example
Prompt: `docs/reviews/prompts/adoption_7_personas.md`
Prompt revision: example
Repo revision: example
Contract baseline refs:
- /specs/schema/schema_v1.md
- /specs/schema/review_snapshot_schema_v1.yaml
- /specs/contract/12_runner_interface.md
- /specs/contract/25_compatibility_matrix.md
- /specs/contract/26_review_output_contract.md
- /specs/governance/check_sets_v1.yaml
Runner lane: rust|required

## Scope Notes

- What changed since last review: seeded example snapshot for parser and governance fixtures.
- What this run focused on: canonical output contract shape.
- Environment limitations: example-only content.

## Command Execution Log

| command | status | exit_code | stdout_stderr_summary |
|---|---|---:|---|
| ./runners/public/runner_adapter.sh --impl rust critical-gate | pass | 0 | example placeholder result |

## Findings

| Severity | Verified/Hypothesis | File:Line | What | Why | When | Proposed fix |
|---|---|---|---|---|---|---|
| P2 | Verified | docs/reviews/templates/review_snapshot.md:1 | Contract requires stable section order | Downstream tooling parses fixed headings | During review snapshot generation | Use canonical template |

## Synthesis

- North-star: review outputs are machine-consumable without manual cleanup.
- Top risks: parser/schema drift.
- Definition of done: snapshot/template/prompt/tooling/governance contracts remain synchronized.

## Spec Candidates (YAML)

```yaml
- id: REVIEW-CANDIDATE-001
  title: Enforce review prompt schema sync
  type: contract.check
  class: MUST
  target_area: docs.reviews
  acceptance_criteria:
  - Governance fails when required prompt headings are missing.
  affected_paths:
  - /specs/governance/cases/core/docs_reviews_prompt_schema_contract_sync.spec.md
  risk: low
- id: REVIEW-CANDIDATE-002
  title: Enforce review template schema sync
  type: contract.check
  class: MUST
  target_area: docs.reviews
  acceptance_criteria:
  - Governance fails when template headings or table headers drift.
  affected_paths:
  - /specs/governance/cases/core/docs_review_snapshot_template_contract_sync.spec.md
  risk: low
- id: REVIEW-CANDIDATE-003
  title: Enforce review tooling schema sync
  type: contract.check
  class: MUST
  target_area: docs.reviews
  acceptance_criteria:
  - Governance fails when review tooling expects legacy candidate keys.
  affected_paths:
  - /specs/governance/cases/core/docs_review_tooling_contract_sync.spec.md
  risk: low
- id: REVIEW-CANDIDATE-004
  title: Validate active review snapshots
  type: contract.check
  class: MUST
  target_area: docs.reviews
  acceptance_criteria:
  - Governance validates canonical snapshots in docs/reviews/snapshots.
  affected_paths:
  - /specs/governance/cases/core/docs_review_snapshots_schema_valid.spec.md
  risk: low
- id: REVIEW-CANDIDATE-005
  title: Add review snapshot validator command
  type: contract.job
  class: MUST
  target_area: tooling.review
  acceptance_criteria:
  - review-validate returns 0 for canonical snapshots.
  affected_paths:
  - /runners/python/spec_runner/review_snapshot_validate.py
  risk: moderate
- id: REVIEW-CANDIDATE-006
  title: Make snapshot scaffolder contract-complete
  type: contract.job
  class: MUST
  target_area: tooling.review
  acceptance_criteria:
  - new_review_snapshot scaffolds all required sections.
  affected_paths:
  - /runners/python/spec_runner/new_review_snapshot.py
  risk: low
- id: REVIEW-CANDIDATE-007
  title: Make pending extraction parse canonical candidates
  type: contract.job
  class: MUST
  target_area: tooling.review
  acceptance_criteria:
  - review_to_pending parses canonical candidate list and fails on invalid shape.
  affected_paths:
  - /runners/python/spec_runner/review_to_pending.py
  risk: moderate
- id: REVIEW-CANDIDATE-008
  title: Publish review output contract doc
  type: contract.export
  class: MUST
  target_area: docs.contract
  acceptance_criteria:
  - Contract index includes review output contract chapter.
  affected_paths:
  - /specs/contract/26_review_output_contract.md
  risk: low
- id: REVIEW-CANDIDATE-009
  title: Publish review output schema
  type: contract.export
  class: MUST
  target_area: specs.schema
  acceptance_criteria:
  - Schema file documents required sections and candidate keys.
  affected_paths:
  - /specs/schema/review_snapshot_schema_v1.yaml
  risk: low
- id: REVIEW-CANDIDATE-010
  title: Keep review docs rooted in docs/reviews
  type: contract.check
  class: MUST
  target_area: docs.reviews
  acceptance_criteria:
  - Active references to docs/history/reviews are rejected.
  affected_paths:
  - /specs/governance/cases/core/docs_reviews_namespace_active.spec.md
  risk: low
```

## Classification Labels

- `REVIEW-CANDIDATE-001`: docs
- `REVIEW-CANDIDATE-002`: docs
- `REVIEW-CANDIDATE-003`: tooling
- `REVIEW-CANDIDATE-004`: docs
- `REVIEW-CANDIDATE-005`: tooling
- `REVIEW-CANDIDATE-006`: tooling
- `REVIEW-CANDIDATE-007`: tooling
- `REVIEW-CANDIDATE-008`: docs
- `REVIEW-CANDIDATE-009`: docs
- `REVIEW-CANDIDATE-010`: behavior

## Reject / Defer List

- feature: strict reviewer persona scoring weights
  why_defer: out of scope for contract unification
  revisit_trigger: parser quality baseline reaches stable adoption

## Raw Output

Example snapshot fixture for governance/tooling contract checks.
