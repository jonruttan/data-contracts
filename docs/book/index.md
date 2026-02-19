# Spec Book

Spec-first, contract-backed documentation for authors, maintainers, and reviewers.

## Primary Audience

- spec authors onboarding to executable contract workflows
- maintainers operating required-lane checks and governance
- reviewers mapping narrative guidance to normative sources

## Read Paths

Quick orientation:

1. `docs/book/05_what_is_data_contracts.md`
2. `docs/book/10_getting_started.md`
3. `docs/book/35_usage_guides_index.md`

Core narrative path:

1. `docs/book/05_what_is_data_contracts.md`
2. `docs/book/10_getting_started.md`
3. `docs/book/15_spec_lifecycle.md`
4. `docs/book/20_case_model.md`
5. `docs/book/25_system_topology.md`
6. `docs/book/30_assertion_model.md`
7. `docs/book/35_usage_guides_index.md`
8. `docs/book/40_spec_lang_authoring.md`
9. `docs/book/50_library_authoring.md`
10. `docs/book/60_runner_and_gates.md`
11. `docs/book/65_runner_status_and_compatibility.md`
12. `docs/book/70_governance_and_quality.md`
13. `docs/book/80_troubleshooting.md`
14. `docs/book/90_reference_guide.md`
15. `docs/book/99_generated_reference_index.md`

Guide-first path:

1. `docs/book/guides/index.md`
2. `docs/book/guides/guide_01_onboarding.md`
3. `docs/book/guides/guide_02_first_spec_authoring.md`
4. `docs/book/guides/guide_03_running_checks_and_gates.md`
5. `docs/book/guides/guide_04_debugging_failures.md`
6. `docs/book/guides/guide_05_release_and_change_control.md`
7. `docs/book/guides/guide_06_governance_tuning.md`
8. `docs/book/guides/guide_07_schema_extension_workflow.md`
9. `docs/book/guides/guide_08_ci_integration.md`
10. `docs/book/guides/guide_09_status_exchange_operations.md`
11. `docs/book/guides/guide_10_reference_navigation_patterns.md`

## Canonical Sources

- `specs/schema/schema_v1.md`
- `specs/contract/`
- `specs/governance/`
- `docs/book/reference_manifest.yaml`

## Compatibility (Non-Blocking)

Python/PHP runtime lanes are compatibility telemetry lanes and non-blocking by default.
required-lane policy is evaluated from status telemetry and contracts.
