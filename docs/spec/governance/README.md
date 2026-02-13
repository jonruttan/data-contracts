# Governance Spec Cases

Governance checks expressed as executable `yaml spec-test` cases.

Run:

```sh
python scripts/run_governance_specs.py
```

Current checks:

- `pending.no_resolved_markers`: fails when files in `docs/spec/pending/`
  contain `resolved:` or `completed:` markers.
- `docs.security_warning_contract`: requires trust-model docs to include
  non-sandboxed/trusted-input/untrusted-spec language.
- `docs.v1_scope_contract`: requires
  `docs/spec/contract/08_v1_scope.md` and core section tokens.
