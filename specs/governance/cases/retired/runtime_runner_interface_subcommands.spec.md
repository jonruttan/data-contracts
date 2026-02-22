```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'runner_interface_subcommands': {'path': '/dc-runner-rust', 'required_subcommands': ['governance', 'style-check', 'normalize-check', 'normalize-fix', 'schema-registry-check', 'schema-registry-build', 'schema-docs-check', 'schema-docs-build', 'lint', 'typecheck', 'compilecheck', 'conformance-purpose-json', 'conformance-purpose-md', 'spec-portability-json', 'spec-portability-md', 'runner-independence-json', 'runner-independence-md', 'python-dependency-json', 'python-dependency-md', 'ci-gate-summary', 'docs-build', 'docs-build-check', 'docs-lint', 'docs-graph', 'conformance-parity', 'runner-certify', 'test-core', 'test-full']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.runner_interface_subcommands'}}, 'use': [{'ref': '/specs/libraries/policy/policy_core.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.pass_when_no_violations']}]}"
services:
  actions:
  - id: svc.root_runner_interface_subcommands_path_dc_runner_rust_required_subcommands_governance_style_check_normalize_check_normalize_fix_schema_registry_check_schema_registry_build_schema_docs_check_schema_docs_build_lint_typecheck_compilecheck_conformance_purpose_json_conformance_purpose_md_spec_portability_json_spec_portability_md_runner_independence_json_runner_independence_md_python_dependency_json_python_dependency_md_ci_gate_summary_docs_build_docs_build_check_docs_lint_docs_graph_conformance_parity_runner_certify_test_core_test_full_check_profile_governance_scan_config_check_runtime_runner_interface_subcommands_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: legacy.root_runner_interface_subcommands_path_dc_runner_rust_required_subcommands_governance_style_check_normalize_check_normalize_fix_schema_registry_check_schema_registry_build_schema_docs_check_schema_docs_build_lint_typecheck_compilecheck_conformance_purpose_json_conformance_purpose_md_spec_portability_json_spec_portability_md_runner_independence_json_runner_independence_md_python_dependency_json_python_dependency_md_ci_gate_summary_docs_build_docs_build_check_docs_lint_docs_graph_conformance_parity_runner_certify_test_core_test_full_check_profile_governance_scan_config_check_runtime_runner_interface_subcommands_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-CONFIG-004
  title: rust runner adapter declares required interface subcommands
  purpose: Ensures the Rust runner adapter exposes the required runner interface subcommand labels.
  clauses:
    imports:
    - artifact:
      - violation_count
    predicates:
    - id: assert_1
      assert:
        std.logic.eq:
        - var: violation_count
        - 0
    - id: assert_2
      assert:
      - std.logic.eq:
        - std.object.get:
          - var: summary_json
          - passed
        - true
      - std.logic.eq:
        - std.object.get:
          - var: summary_json
          - check_id
        - runtime.runner_interface_subcommands
      imports:
      - artifact:
        - summary_json
```
