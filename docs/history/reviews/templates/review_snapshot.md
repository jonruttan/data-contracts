# Review Snapshot

Date: YYYY-MM-DD
Model: <fill in>
Prompt: `docs/history/reviews/prompts/adoption_7_personas.md`
Prompt revision: <git sha>
Repo revision: <git sha>
Contract baseline refs:
- /specs/01_schema/review_snapshot_schema_v1.yaml
- /specs/02_contracts/26_review_output_contract.md
Runner lane: <docs|governance|discovery>

## Scope Notes
- What changed since last time:
- What you asked the reviewer to focus on:
- Which checks were run:

## Command Execution Log

| command | status | exit_code | stdout_stderr_summary |
| --- | --- | --- | --- |
| `<command>` | success \| failure \| skipped | <exit code> | <short summary> |

## Findings

| Severity | Verified/Hypothesis | File:Line | What | Why | When | Proposed fix |
| --- | --- | --- | --- | --- | --- | --- |
| High | Hypothesis | - | Add at least one row with severity and fix intent | Placeholder | During review snapshot collection | Add concrete finding and fix before merging |

## Synthesis

- North-star:
- 10 highest-value spec items:
- 5 biggest risks:
- Definition of done:

## Spec Candidates (YAML)

```yaml
- id: DOCS-REV-0001
  title: Example reviewer candidate
  type: review
  class: docs
  target_area: docs/history/reviews
  acceptance_criteria:
    - "Candidate rows include required fields."
    - "Contract baseline refs are updated."
  affected_paths:
    - docs/history/reviews/index.md
  risk: medium
```

## Classification Labels

- DOCS-REV-0001: behavior

## Reject / Defer List

- Out-of-scope feature requests for this run.

## Raw Output

Paste the full AI output here. Do not edit it beyond formatting fixes.
