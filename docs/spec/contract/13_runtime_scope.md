# Runtime Scope Contract (v1)

Defines the bounded cross-runtime scope for v1 to keep maintenance sustainable.

## Supported Runtimes (v1)

- Python runner
- PHP runner

These are the only required conformance/parity runtimes for v1 readiness.
The required support targets in v1 are exactly: Python runner, PHP runner.

## Scope Constraint

- New runtime support is out of v1 default scope unless explicitly added through:
  - contract/policy updates
  - conformance parity plan
  - governance enforcement updates
  - explicit contract/governance expansion

## Change Bar For Adding A Runtime

To add a runtime to required support:

1. update `docs/spec/contract/08_v1_scope.md`
2. update this runtime scope contract
3. update policy + traceability + governance cases
4. add parity path and deterministic gate evidence
