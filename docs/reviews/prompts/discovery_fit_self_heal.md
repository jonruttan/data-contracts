# Discovery Fit + Self-Heal Prompt (Spec Runner)

Use this prompt to evaluate whether `spec_runner` is a good fit for a target problem by walking real entrypoints first, applying safe low-risk self-heals when obvious, and producing machine-consumable outputs.

---

```text
You are performing discovery-fit analysis for `spec_runner`.

Your goal:
1. Determine if this project is a good fit for the problem being evaluated.
2. Trace real onboarding and usage entrypoints before concluding.
3. Apply low-risk self-heals when obvious and safe.
4. Record unresolved findings as canonical candidates.

## Contract context (must anchor findings)

- `/specs/schema/schema_v1.md`
- `/specs/schema/review_snapshot_schema_v1.yaml`
- `/specs/contract/12_runner_interface.md`
- `/specs/contract/25_compatibility_matrix.md`
- `/specs/contract/26_review_output_contract.md`
- `/specs/governance/check_sets_v1.yaml`

Runtime lane policy:
- required lane: rust
- compatibility lanes: python/php/node/c (non-blocking)

## Discovery-first entrypoint walk (required order)

Start at:
- `/README.md`

If missing or insufficient, continue in this exact fallback order:
1. `/docs/book/index.md`
2. `/docs/development.md`
3. `/specs/current.md`
4. `/specs/contract/index.md`
5. `/specs/schema/schema_v1.md`

Build an explicit entrypoint trace with:
- first-run commands
- required setup
- contract/schema anchors
- runner/gate expectations

## Fit evaluation model (required)

Infer target problem profile and score 0-5 on:
- onboarding friction
- operational determinism
- contract clarity
- runtime/tooling requirements
- governance burden

Verdict rules:
- `good_fit`: all critical dimensions >= 4 and no unresolved P0/P1 blockers
- `conditional_fit`: at least one critical dimension <= 3 but blockers are remediable
- `poor_fit`: unresolved high-risk mismatch or multiple core dimensions <= 2

## Self-heal policy (low-risk only)

Allowed auto-fixes (any low-risk file):
- docs wording/path drift
- command example drift
- governance map/index/catalog token sync
- missing or incorrect prompt/template refs
- strict-schema output contract drift
- low-risk parser/CLI wiring inconsistencies that do not redesign semantics

Forbidden auto-fixes:
- architecture redesign
- schema semantic changes
- risky runtime logic changes without deterministic proof
- dependency additions without explicit contract/test evidence

When auto-fix is not safe:
- report finding
- emit canonical candidate in `## Spec Candidates (YAML)`
- ensure output is convertible to `specs/governance/pending/<snapshot>-pending.md`

## Required run sequence (when available)

- `./runners/public/runner_adapter.sh --impl rust critical-gate`
- `./runners/public/runner_adapter.sh --impl rust governance`
- `./runners/public/runner_adapter.sh --impl rust docs-generate-check`
- `./runners/public/runner_adapter.sh --impl rust review-validate --snapshot <snapshot>`
- `./runners/public/runner_adapter.sh --impl rust review-to-pending <snapshot>`

For each attempted command capture:
- `command`
- `status` (`pass|fail|skipped`)
- `exit_code`
- `stdout_stderr_summary`

## Output contract (strict)

Follow `/specs/contract/26_review_output_contract.md` exactly.

Use exact top-level order:
1. `## Scope Notes`
2. `## Command Execution Log`
3. `## Findings`
4. `## Synthesis`
5. `## Spec Candidates (YAML)`
6. `## Classification Labels`
7. `## Reject / Defer List`
8. `## Raw Output`

Required table headers:
- `command | status | exit_code | stdout_stderr_summary`
- `Severity | Verified/Hypothesis | File:Line | What | Why | When | Proposed fix`

`## Synthesis` must include:
- target_problem_profile
- entrypoint_trace_summary
- fit_scores (0-5 per dimension)
- fit_verdict (`good_fit|conditional_fit|poor_fit`)
- blocking_gaps
- recommended_next_step

`## Spec Candidates (YAML)` objects must include:
- `id`
- `title`
- `type`
- `class`
- `target_area`
- `acceptance_criteria`
- `affected_paths`
- `risk`

`## Classification Labels`:
- one label per candidate id
- labels allowed: `behavior|docs|tooling`

## Evidence and style rules

- tag each finding `Verified` or `Hypothesis`
- cite exact file paths and nearby contract tokens
- no praise language
- no speculative redesigns
- keep recommendations executable and bounded
```
