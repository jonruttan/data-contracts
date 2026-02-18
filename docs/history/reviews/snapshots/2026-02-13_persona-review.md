# Review Snapshot

Date: 2026-02-13
Model: codex-gpt5
Prompt: `docs/history/reviews/prompts/adoption_7_personas.md`
Prompt revision: 678376d
Repo revision: 678376d

## Notes (optional)

- What changed since last time:
- What you asked the reviewer to focus on:
- Where spec candidates were copied:
  - backlog: yes/no
  - promoted specs: (list files) or none

## Raw Output

`spec_runner` is trying to be a language-neutral executable-spec contract
system: author behavior once in Markdown (`yaml contract-spec`), execute it in
multiple runtimes, and keep implementations honest via conformance/parity
gates.

## Grey Beard

Top unacceptable:
- no sandbox model for untrusted specs (`specs/contract/04_harness.md`)
- policy stack may be too heavy for small teams (`specs/contract/policy_v1.yaml`)
- env-driven behavior can still surprise (`runners/python/spec_runner/harnesses/cli_run.py`)

Top salvageable:
- deterministic gate exists (`scripts/ci_gate.sh`)
- parity is executable, not rhetorical (`scripts/compare_conformance_parity.py`)
- contract/governance checks are concrete (`runners/python/spec_runner/contract_governance.py`)

## Eager Novice

Top unacceptable:
- onboarding path is fragmented across many docs
- runner exit codes are easy to misread without context
- setup requires Python + PHP + yaml extension for full flow

Top salvageable:
- quickstart exists (`README.md`)
- one-command gate exists (`scripts/ci_gate.sh`)
- report validators provide concrete pass/fail shape checks

## Burnt-Out Manager

Top unacceptable:
- governance overhead can exceed value if team only needs a small subset
- packaging metadata/release posture is not yet polished (`pyproject.toml`)
- broad scope (schema + conformance + parity + governance) risks support load

Top salvageable:
- quality gates are already reliable and deterministic
- parity reduces hidden cross-runtime drift risk
- artifacts support auditability

## Must-do Changes

- publish installable CLI entrypoints for core scripts
- add a "first 10 minutes" deterministic onboarding walkthrough
- add an explicit exit-code contract table per runner command
- define core mode vs full-governance mode for adoption tiers
- publish explicit v1 scope/non-goals and compatibility commitments
- add a compact machine-readable gate summary artifact

## Biggest Risks

- users run untrusted specs and assume the tool is sandboxed
- policy/process complexity slows teams that just need simple behavior checks
- cross-runtime scope creep turns maintenance into a bottleneck
- ambient env/time assumptions leak into supposedly portable fixtures
- packaging/release maturity gaps block enterprise adoption

## North-star

- one canonical, executable, deterministic spec corpus that drives behavior and
  cross-runtime parity without duplicated intent per implementation

## Definition Of Done

- stable semver and compatibility policy for schema/contract
- package metadata + CLI entrypoints ready for external use
- secure-by-default usage profile documented and tested
- canonical conformance set with parity gate required in CI
- documented minimal onboarding path with deterministic outputs
