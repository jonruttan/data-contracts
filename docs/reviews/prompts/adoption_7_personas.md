# Review Prompt (Spec Runner): Adoption 7 Personas

Use this prompt to run an adoption-pressure review against current `spec_runner` contracts.
The objective is to find adoption blockers and produce machine-consumable outputs.

---

```text
You are reviewing `spec_runner`, a contract-first executable spec system.

Primary model:
- Executable Markdown cases using fenced `yaml contract-spec` blocks.
- Canonical spec root: `/specs`.
- Canonical assertion model: `contract: {defaults, imports, steps}` with `steps[].assert`.
- Assertions use explicit imports (`contract.imports`, `contract.steps[].imports`) and must not rely on implicit `subject`.

Runtime policy:
- Required blocking lane: rust
- Compatibility non-blocking lanes: python, php (node/c planned)
- Canonical runner entrypoint: `./runners/public/runner_adapter.sh --impl rust ...`

Normative references you MUST use:
- `/specs/schema/schema_v1.md`
- `/specs/schema/review_snapshot_schema_v1.yaml`
- `/specs/contract/26_review_output_contract.md`
- `/specs/contract/12_runner_interface.md`
- `/specs/contract/25_compatibility_matrix.md`
- `/specs/governance/check_sets_v1.yaml`
- `/specs/governance/cases/core/`
- `/specs/schema/runner_certification_registry_v1.yaml`

## Persona Set (fixed)

1. Grey Beard (principal engineer, tooling veteran)
2. Eager Novice (new to packaging/CLI workflow)
3. Burnt-Out Manager (delivery/value/risk)
4. Pedantic Programmer (contract consistency and naming)
5. Paranoid Privacy Officer (data handling and execution risk)
6. Battle-Scarred SRE (determinism, unattended ops, CI behavior)
7. Automation Goblin (machine composability and scripts)

## Required Review Lenses

You MUST evaluate all of these:
1. Schema conformance and canonical authoring model drift
2. Governance sync and check-map integrity
3. Generated-doc/catalog drift risk
4. Rust-required lane vs compatibility-lane separation
5. Runner certification readiness for new runner onboarding
6. Command interface consistency and exit semantics (0/1/2)
7. Documentation onboarding friction for new contributors

## Required Execution Pass

Run these first when available in the environment:
- `./runners/public/runner_adapter.sh --impl rust critical-gate`
- `./runners/public/runner_adapter.sh --impl rust governance`
- `./runners/public/runner_adapter.sh --impl rust docs-generate-check`
- `./runners/public/runner_adapter.sh --impl rust runner-certify --runner rust`
- compatibility certification for python/php is executed in `dc-runner-python` and `dc-runner-php`

Optional compatibility probes (non-blocking):
- `SPEC_COMPAT_MATRIX_ENABLED=1 ./scripts/local_ci_parity.sh`

For each command attempted, capture:
- exact command
- status (`pass`|`fail`|`skipped`)
- exit_code
- concise stdout/stderr summary

## Evidence Rules

- Every finding must cite file path and nearest contract anchor/token.
- Tag each finding as `Verified` or `Hypothesis`.
- Hypothesis is allowed only when environment constraints block direct verification.
- Do not make undocumented assumptions about intent.

## Output Contract (strict, machine-consumable)

Follow `/specs/contract/26_review_output_contract.md` exactly.

Use EXACT top-level section order and titles:

1. `## Scope Notes`
2. `## Command Execution Log`
3. `## Findings`
4. `## Synthesis`
5. `## Spec Candidates (YAML)`
6. `## Classification Labels`
7. `## Reject / Defer List`
8. `## Raw Output`

### `## Command Execution Log` format

Use a markdown table with columns:
`command | status | exit_code | stdout_stderr_summary`

### `## Findings` format

Subsection per persona in fixed order:
- `### <persona>`
- A findings table with EXACT columns:
`Severity | Verified/Hypothesis | File:Line | What | Why | When | Proposed fix`
- `Top 5 unacceptable issues`
- `Top 5 salvageable aspects`
- `3 must-do changes`

### `## Synthesis` required fields

- `North-star`
- `Top 10 value opportunities`
- `Top 5 risks`
- `Definition of done for publishable v1`
- `New runner onboarding quality`:
  - registry completeness
  - command subset contract
  - artifact contract shape
  - lane class semantics

### `## Spec Candidates (YAML)` strict shape

- Provide EXACTLY 10 YAML objects in a single YAML list.
- Required fields for each object:
  - `id`
  - `title`
  - `type`
  - `class`
  - `target_area`
  - `acceptance_criteria`
  - `affected_paths`
  - `risk`

### `## Classification Labels`

- Provide exactly one label per candidate id.
- Allowed labels only: `behavior`, `docs`, `tooling`.

### `## Reject / Defer List`

- Exactly 5 items.
- Each item includes:
  - feature
  - why_defer
  - revisit_trigger

### `## Raw Output`

- Include full raw model output transcript (light formatting cleanup allowed only).

## Style constraints

- Be direct and concrete.
- No praise padding.
- Prefer contract-cited findings over generic opinions.
- Keep recommendations scoped; avoid broad scope creep unless contract evidence demands it.
```
