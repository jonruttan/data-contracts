# Self-Healing Pre-Merge Hardening Pipeline (for `data-contracts`)

A staged sequence for the `data-contracts` control-plane repository that discovers
issues, applies safe fixes, and escalates risk before merge.

## Repository Context (Hard Requirements)

- Project: control-plane repo for executable contract specifications and governance.
- Core behavior: author, validate, and gate Markdown-embedded executable specs and
the review artifacts that summarize results.
- Schema reference: `specs/01_schema/schema_v1.md`.
- Runner-only setup inputs must be under `harness:` (never arbitrary top-level keys).
- Keep dependencies minimal: stdlib preferred, small stable deps only if justified
(for example `PyYAML`).
- Prefer adapters/harnesses over expanding core DSL.
- Error messages must be direct and actionable.

## Global Guardrails (Non-Negotiable)

- No behavior changes unless needed to match clearly stated intent or fix a
  demonstrated bug/regression.
- Minimal diffs only; surgical changes over broad rewrites.
- No new dependencies without explicit justification and rollback plan.
- No blanket silencing: no disabling checks, no broad catches, no timeout inflation
  without evidence.
- No secrets in logs/docs/fixtures/examples.
- Follow existing project patterns and tooling.
- If a fix is not clearly safe, escalate as a finding.

## Proof Standard (Every Stage)

For each stage output:
1. Auto-fixes applied (files changed + why safe)
2. Remaining findings (`Severity | File:Line | What | Why | When | Proposed fix`)
3. Checks run + results (commands + pass/fail + key failure snippet)
4. Next actions before proceeding

Severity:
- P0 critical
- P1 high
- P2 medium
- P3 low

## Stop Conditions (Hard Gates)

Stop immediately if:
- P0 remains unresolved.
- Baseline commands cannot be run reliably after reasonable investigation.
- Changes introduce unclear/high-risk core contract drift (schema compatibility,
  harness dispatch semantics) without tests and explicit intent.
- Potential security issue in markdown/spec parsing or harness execution path is
  suspected but unproven safe.
- Backward compatibility for schema behavior is broken without normalization/
  versioning plan.

## Commit Discipline (Adjusted for this Repo)

- Do not run `git commit` unless the user explicitly approves (`approved` or
  `commit it`).
- If a stage changes files, propose a commit message:
  - `hardening(stage-N): <short description>`
- Keep stage changes isolated and reversible.
- If behavior changed, include/adjust tests and note behavior change in proposed
  commit body.

## Change Budget

- Prefer <=200 changed lines per stage.
- If larger change is needed, escalate:
  - `P1 | <area> | exceeds safe change budget` with split-plan proposal.

---

## Stage 0 - Baseline & Tooling Discovery

- Detect and record exact commands:
  - `dc-runner critical-gate`
  - `dc-runner governance`
  - `dc-runner docs-generate-check`
  - `.dc-runner review-validate --snapshot <snapshot-path>` (when validating review artifacts)
- Discover lint/type/static tools from config (`pyproject.toml`, etc). If absent,
  report explicitly.
- Run fastest checks first.
- Fix only trivial setup issues when intent is obvious.
- Missing/inconsistent tooling is P1 with remediation.

## Stage 1 - Intent Extraction (No Fixes)

You are a code analyst.

Output only:
1. Problem being solved
2. Intended behavior
3. Inputs/outputs
4. Affected components
5. Explicit assumptions
6. Implicit assumptions
7. Ambiguities

If intent is unclear for parser/schema/dispatch behavior, raise P1 and stop.

## Stage 2 - Make It Green (Mechanical Healing)

You are a build sheriff.

- Run Stage 0 commands (fast to slow).
- Apply only safe mechanical fixes:
  - formatter/lint trivial fixes
  - missing imports/renames with clear intent
  - localized obvious bug fix proven by failing tests
- No new dependencies.
- No speculative behavior changes.

## Stage 3 - Contract Boundary Healing

You are an architectural refactorer.

Focus on this repo's contracts:
- parser vs execution separation
- dispatch boundaries by `type`
- schema-version and validation boundaries
- core docs/contracts separation from runner implementation details

Allowed:
- small extractions aligned with existing patterns
- tighten validation paths
- move project-specific logic out of core

Not allowed:
- new architectural paradigm
- DSL expansion without explicit schema/versioning intent

Output:
- `Severity | File:Line | Violation | Why | When | Fix`
- `Isolation rating: strong | moderate | weak`

## Stage 4 - Side Effects & Global State

You are an adversarial stabilizer.

Find and heal:
- mutable module-level state
- order-dependent parser behavior
- implicit singletons in registry/dispatch paths
- direct env reads outside explicit config/harness inputs

Allowed:
- localize state
- explicit dependency passing
- namespacing and deterministic behavior

## Stage 5 - Failure Modes & Resilience

You are a resilience engineer.

Assume malformed markdown, invalid YAML, unknown `type`, bad harness config, and
partial test runs.

Find and heal:
- unhelpful validation errors
- swallowed exceptions
- non-actionable error messages
- non-deterministic failure handling

Allowed:
- improve actionable error messages
- tighten error typing/paths
- add bounded safeguards consistent with current patterns

Output:
- `Severity | File:Line | Failure Scenario | Risk | Fix`

## Stage 6 - Schema Compatibility Safety

You are a schema reliability engineer.

Goal:
- preserve compatibility with `specs/01_schema/schema_v1.md`
- prevent unsafe top-level runner config drift
- ensure `harness:` contract is enforced

Find and heal:
- undocumented schema behavior
- backward-incompatible parser changes
- weak validation around `harness:`

Output:
- P0/P1 risks
- compatibility notes
- rollback risk (`low | moderate | high`)

## Stage 7 - Security Healing

You are a security engineer with attacker mindset.

Focus on:
- YAML/Markdown parsing safety
- injection/path traversal in harness or file handling
- unsafe execution assumptions
- secret leakage in logs/errors/fixtures

Allowed:
- enforce safe parsing/validation patterns already used in repo
- tighten path/input validation
- redact sensitive fields in logs/errors

Output:
- `Severity | File:Line | Exploit Scenario | Risk | Fix`

## Stage 8 - Performance Healing

You are a performance engineer.

Focus on obvious library bottlenecks:
- repeated full-document parsing
- unnecessary re-parsing of YAML/spec blocks
- unbounded loops over docs/cases
- hot-path allocations

Allowed:
- local memoization within call scope
- reduce repeated parsing/work without changing semantics

Output:
- `Severity | File:Line | Bottleneck | Scale Risk | Fix`
- `Scale confidence: high | moderate | low`

## Stage 9 - Test Integrity Healing

You are a test reliability engineer.

Find and heal:
- missing regression tests for P0/P1 fixes
- missing negative tests for schema/validation errors
- order-dependent/shared-state tests
- over-mocking that hides parser/dispatch behavior

Allowed:
- minimal targeted regression tests
- isolation improvements
- clearer fixtures for contract-spec markdown cases

Output:
- `Severity | File:Line | Gap | Risk | Required Test`
- `Test isolation: strong | moderate | weak`

## Final Boss - Production Gatekeeper (No Healing)

You are a production gatekeeper.

Review all branch changes (staged, unstaged, untracked).

Output only:
- `Severity | File:Line | What | Why | When | Fix`

Final verdicts:
1. Production readiness: `ready | conditionally ready | not ready`
2. Correctness: `correct | incorrect | high-risk`
3. Isolation: `strong | moderate | weak`
4. Blast radius: `minimal | contained | wide | systemic`
5. Required fixes before merge

If no meaningful risks:
- `No production or correctness risks detected.`

## Optional Waiver Template

- Risk: `<describe>`
- Owner: `<name>`
- Justification: `<why acceptable now>`
- Mitigation: `<monitoring/rollback>`
- Expiry: `<date or condition>`
