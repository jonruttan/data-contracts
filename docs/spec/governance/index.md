# Governance Index

Source of truth: spec.governance.index

Executable governance checks for canonical contract enforcement.

## Core Inputs

- Check sets: `/docs/spec/governance/check_sets_v1.yaml`
- Check family map: `/docs/spec/governance/check_catalog_map_v1.yaml`
- Cases index: `/docs/spec/governance/cases/core/index.md`

## Execution

```sh
python -m spec_runner.spec_lang_commands run-governance-specs
```

## Canonical Checks

- Governance check catalog is generated into `/docs/book/96_appendix_governance_checks_reference.md`.
- Policy and traceability references are generated into `/docs/book/94_appendix_contract_policy_reference.md` and `/docs/book/95_appendix_traceability_reference.md`.
