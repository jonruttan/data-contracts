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
- `runtime.config_literals`: rejects duplicated governed config string literals
  in runtime Python code.
- `runtime.settings_import_policy`: rejects importing `DEFAULT_*`/`ENV_*`
  constants from `spec_runner.settings` in runtime Python code.
- `conformance.case_index_sync`: ensures conformance case index ids match
  fixture case ids.
- `conformance.purpose_warning_codes_sync`: ensures purpose warning code docs
  match implementation warning codes.
- `conformance.case_doc_style_guard`: enforces conformance doc style and
  purpose-lint rules (one case/block, heading placement, sorted ids, quality checks).
- `docs.regex_doc_sync`: enforces regex portability profile linkage and
  assertion-operator token sync across contract/schema/policy docs.
- `naming.filename_policy`: enforces configured filename shape rules
  (lowercase separators, allowlist exceptions, and extension scope).
