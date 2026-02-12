---
id: SR-PORT-002
title: Assertion Health Policy (Brittle and Degenerate Checks)
priority: P1
---

# Assertion Health Policy (Brittle and Degenerate Checks)

## Problem

The runner currently evaluates assertions but does not explicitly classify
assertion quality risks (for example brittle text matches or vacuous logic).
As specs grow, these patterns can hide regressions, create flakiness, or give
false confidence.

## Proposal

Add assertion-health diagnostics that detect likely brittle or degenerate
assertions and route them through policy controls.

The runner SHOULD:

- classify diagnostics by code/category
- attach case id + assertion path metadata
- support severity policy at two levels:
  - global runner policy
  - per-test override

Initial policy modes:

- `ignore`: diagnostics are collected but do not affect outcome
- `warn`: diagnostics are reported as warnings
- `error`: diagnostics fail the case/run

## Candidate Diagnostic Classes

Initial classes to specify and test:

- vacuous group usage (constructs that are always true/false by shape)
- contradictory assertion combinations on a single target
- brittle text/regex checks likely to overfit incidental output structure

The exact heuristics MUST be explicit and deterministic.

## Slices

1. Define diagnostic taxonomy and payload shape in contract docs.
2. Add schema/config entry points for global policy.
3. Add per-test override shape in DSL.
4. Implement Python diagnostics and reporting.
5. Add conformance fixtures for warning/error behavior.
6. Mirror behavior in PHP implementation and parity checks.

## Compatibility

Default behavior SHOULD remain non-breaking (`warn` or `ignore`) until a
strict mode is explicitly enabled.
