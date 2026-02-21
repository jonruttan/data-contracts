```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-DOCS-REF-026
  title: readme avoids makefile onboarding cookbook
  purpose: Keeps README focused on project purpose and usage, not local make workflows.
  harness:
    root: "."
    readme_makefile_tokens:
      path: "/README.md"
      forbidden_tokens:
      - make setup
      - make prepush
      - hooks-install
    check:
      profile: governance.scan
      config:
        check: docs.readme_makefile_cookbook_forbidden
  clauses:
    imports:
    - from: artifact
      names:
      - violation_count
    predicates:
    - id: assert_1
      assert:
        call:
        - var: policy.assert.no_violations
        - std.object.assoc:
          - violation_count
          - var: violation_count
          - lit: {}
```
