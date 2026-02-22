```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'readme_makefile_tokens': {'path': '/README.md', 'forbidden_tokens': ['make setup', 'make prepush', 'hooks-install']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'docs.readme_makefile_cookbook_forbidden'}}}"
services:
- type: legacy.root_readme_makefile_tokens_path_readme_md_forbidden_tokens_make_setup_make_prepush_hooks_install_check_profile_governance_scan_config_check_docs_readme_makefile_cookbook_forbidden
  operations:
  - id: svc.root_readme_makefile_tokens_path_readme_md_forbidden_tokens_make_setup_make_prepush_hooks_install_check_profile_governance_scan_config_check_docs_readme_makefile_cookbook_forbidden.default.1
    mode: default
    direction: bidirectional
contracts:
  clauses:
  - id: DCGOV-DOCS-REF-026
    title: readme avoids makefile onboarding cookbook
    purpose: Keeps README focused on project purpose and usage, not local make workflows.
    asserts:
      imports:
      - from: artifact
        names:
        - violation_count
      checks:
      - id: assert_1
        assert:
          call:
          - var: policy.assert.no_violations
          - std.object.assoc:
            - violation_count
            - var: violation_count
            - lit: {}
```
