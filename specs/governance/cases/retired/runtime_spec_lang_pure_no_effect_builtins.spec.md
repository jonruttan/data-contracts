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
    - "{'root': '.', 'spec_lang_purity': {'files': ['dc-runner-python', 'dc-runner-php',
      'dc-runner-php'], 'forbidden_tokens': ['path_exists']}, 'check': {'profile':
      'governance.scan', 'config': {'check': 'runtime.spec_lang_pure_no_effect_builtins'}},
      'use': [{'ref': '/specs/libraries/policy/policy_core.spec.md', 'as': 'lib_policy_core_spec',
      'symbols': ['policy.pass_when_no_violations']}]}"
services:
  actions:
  - id: svc.root_spec_lang_purity_files_dc_runner_python_dc_runner_php_dc_runner_php_forbidden_tokens_path_exists_check_profile_governance_scan_config_check_runtime_spec_lang_pure_no_effect_builtins_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: legacy.root_spec_lang_purity_files_dc_runner_python_dc_runner_php_dc_runner_php_forbidden_tokens_path_exists_check_profile_governance_scan_config_check_runtime_spec_lang_pure_no_effect_builtins_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-SPECLANG-PURE-001
  title: spec-lang evaluators avoid side-effectful builtins
  purpose: Enforces pure evaluation semantics by forbidding side-effectful probes
    in spec-lang implementations.
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
        - runtime.spec_lang_pure_no_effect_builtins
      imports:
      - artifact:
        - summary_json
```
