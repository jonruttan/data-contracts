# Self-Healing Pre-Merge Hardening Pipeline (Data Contracts)

A staged hardening pipeline for `data-contracts` aligned to current contracts, Rust-first required lane policy, and executable-spec governance.

## Repository Context (Hard Requirements)

- Executable case format: fenced `yaml contract-spec` blocks.
- Canonical spec root: `/specs`.
- Canonical schema: `/specs/schema/schema_v1.md`.
- Review snapshot schema: `/specs/schema/review_snapshot_schema_v1.yaml`.
- Runtime interface contract: `/specs/contract/12_runner_interface.md`.
- Compatibility matrix contract: `/specs/contract/25_compatibility_matrix.md`.
- Review output contract: `/specs/contract/26_review_output_contract.md`.
- Governance check sets: `/specs/governance/check_sets_v1.yaml`.
- Runner certification registry: `/specs/schema/runner_certification_registry_v1.yaml`.
- Required lane: rust.
- Compatibility non-blocking lanes: python/php (node/c planned).

## Global Guardrails (Non-Negotiable)

- No speculative behavior changes.
- Minimal, reversible diffs.
- No new dependencies without explicit justification.
- No blanket disabling/silencing of checks.
- No schema drift without contract updates and test evidence.
- No secrets in output artifacts/logs/fixtures.
- Escalate uncertain fixes instead of guessing.

## Proof Standard (Every Stage)

For every stage, output all of:
1. `Auto-fixes applied`
2. `Remaining findings`
3. `Checks run`
4. `Next actions`

Findings table format (required):
`Severity | Verified/Hypothesis | File:Line | What | Why | When | Proposed fix`

Severity set:
- `P0` critical
- `P1` high
- `P2` medium
- `P3` low

## Stop Conditions (Hard Gates)

Stop immediately if:
- Any unresolved `P0` remains.
- Baseline commands cannot be run after reasonable troubleshooting.
- High-risk contract drift appears without explicit intent/tests.
- Security-sensitive parsing/execution path safety cannot be verified.

## Stage Output Schema (strict)

Use exact section order for each stage:
1. `### Stage <N>: <title>`
2. `#### Auto-fixes applied`
3. `#### Remaining findings`
4. `#### Checks run`
5. `#### Next actions`

## Stage 0 - Baseline & Tooling Discovery

Required command probes:
- `./runners/public/runner_adapter.sh --impl rust critical-gate`
- `./runners/public/runner_adapter.sh --impl rust governance`
- `./runners/public/runner_adapter.sh --impl rust docs-generate-check`
- `./runners/public/runner_adapter.sh --impl rust runner-certify --runner rust`
- compatibility certification for python/php is executed in `dc-runner-python` and `dc-runner-php`
- `./scripts/local_ci_parity.sh`

Optional compatibility probes (non-blocking):
- `SPEC_COMPAT_MATRIX_ENABLED=1 ./scripts/local_ci_parity.sh`

For each command include:
`command | status | exit_code | stdout_stderr_summary`

## Stage 1 - Intent Extraction (No Fixes)

Produce:
1. Problem statement
2. Intended behavior
3. Inputs/outputs
4. Affected components
5. Explicit assumptions
6. Implicit assumptions
7. Ambiguities

If parser/contract intent remains ambiguous at high impact, raise `P1` and stop.

## Stage 2 - Make It Green (Mechanical Healing)

Allowed:
- obvious import/rename/format fixes
- localized deterministic bug fixes backed by failing checks

Not allowed:
- architecture shifts
- DSL expansion
- dependency additions without review

## Stage 3 - Contract Boundary Healing

Focus:
- parser/executor separation
- dispatch boundaries by `type`
- schema/version boundaries
- core/runtime leakage

Also verify:
- runner certification command surface sync
- certification registry sync
- certification artifact contract sync

## Stage 4 - Side Effects & Global State

Find/heal:
- mutable module-level state
- order-dependent behavior
- implicit singleton leakage
- uncontrolled env coupling

## Stage 5 - Failure Modes & Resilience

Stress cases:
- malformed markdown/yaml
- unknown type/harness profile
- missing refs/case ids
- partial gate execution

Require actionable errors.

## Stage 6 - Schema Compatibility Safety

Validate compatibility with:
- `/specs/schema/schema_v1.md`
- harness scoping under `harness:`
- canonical contract assertion/import shape

## Stage 7 - Security Healing

Focus:
- parsing safety
- command/path injection risk
- unsafe runner invocation assumptions
- secret exposure in generated artifacts

## Stage 8 - Performance Healing

Focus:
- repeated parsing/walks
- unbounded scans
- avoidable allocations in hot paths

## Stage 9 - Test Integrity Healing

Find/heal:
- missing regressions for P0/P1
- missing negative schema tests
- order-dependent tests
- over-mocked checks that hide contract behavior

## Final Boss - Gatekeeper Summary (No Healing)

Produce only:
- Findings table (required format)
- Verdict quintet:
  1. production_readiness (`ready|conditionally ready|not ready`)
  2. correctness (`correct|incorrect|high-risk`)
  3. isolation (`strong|moderate|weak`)
  4. blast_radius (`minimal|contained|wide|systemic`)
  5. required_fixes_before_merge

If no meaningful risks:
- `No production or correctness risks detected.`

## Optional Waiver Template

- `risk`
- `owner`
- `justification`
- `mitigation`
- `expiry`

## Final Snapshot Contract (required)

When emitting the final deliverable snapshot, use this exact section order:

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
