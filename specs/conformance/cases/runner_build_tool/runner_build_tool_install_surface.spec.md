```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCCONF-BTOOL-007
  title: bundle tooling exposes install command surface
  purpose: Bundle CLI must expose install and install-check commands for multi-bundle project workflows.
  harness:
    check:
      profile: text.file
      config:
        path: "/scripts/bundle"
  clauses:
    imports:
    - from: artifact
      names:
      - text
    predicates:
    - id: assert_1
      assert:
        std.string.contains:
        - var: text
        - scripts/bundle install --project-lock
    - id: assert_2
      assert:
        std.string.contains:
        - var: text
        - scripts/bundle install-check --project-lock
```
