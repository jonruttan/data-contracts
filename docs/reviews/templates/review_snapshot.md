# Review Snapshot

Date: YYYY-MM-DD
Model: <fill in>
Prompt: `docs/reviews/prompts/<prompt>.md`
Prompt revision: <git sha>
Repo revision: <git sha>
Contract baseline refs:
- /specs/schema/schema_v1.md
- /specs/contract/12_runner_interface.md
- /specs/contract/25_compatibility_matrix.md
- /specs/governance/check_sets_v1.yaml
Runner lane: rust|required | python|compatibility | php|compatibility | mixed

## Scope Notes

- What changed since last review:
- What this run focused on:
- Environment limitations:

## Command Execution Log

| command | status | exit_code | stdout_stderr_summary |
|---|---|---:|---|
| <command> | pass/fail/skipped | <code> | <summary> |

## Findings

| Severity | Verified/Hypothesis | File:Line | What | Why | When | Proposed fix |
|---|---|---|---|---|---|---|
| P1 | Verified | path:line | ... | ... | ... | ... |

## Synthesis

- North-star:
- Top risks:
- Definition of done:

## Spec Candidates (YAML)

```yaml
- id: <ID>
  title: <title>
  type: <contract.check|contract.job|contract.export>
  class: <MUST|MAY|MUST_NOT>
  target_area: <area>
  acceptance_criteria:
  - <criterion>
  affected_paths:
  - <path>
  risk: <low|moderate|high>
```

## Classification Labels

- `<candidate_id>: behavior|docs|tooling`

## Reject / Defer List

- feature: <name>
  why_defer: <reason>
  revisit_trigger: <trigger>

## Raw Output

Paste the full AI output here. Keep content intact except light formatting cleanup.
