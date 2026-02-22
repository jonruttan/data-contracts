```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  harness: job
harness:
  type: unit.test
  profile: check
services:
  defaults:
    type: assert.check
    io: input
    profile: default
  entries:
  - id: svc.assert_check.default.1
    config:
      jobs:
      - id: main
        mode: report
        helper: helper.report.emit
        inputs:
          report_name: conformance-purpose
          format: json
          out: ".artifacts/conformance-purpose.json"
      - id: on_fail
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-001.fail.json"
          format: json
          report_name: DCCONF-JOB-REP-001.fail
      - id: on_complete
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-001.complete.json"
          format: json
          report_name: DCCONF-JOB-REP-001.complete
      use:
      - ref: "/specs/libraries/policy/policy_job.spec.md"
        as: lib_policy_job
        symbols:
        - policy.job.dispatch_ok
        - policy.job.written_path_contains
      spec_lang:
        capabilities:
        - ops.helper
        - ops.job
  - id: svc.assert_check.default.2
    config:
      jobs:
      - id: main
        mode: report
        helper: helper.report.emit
        inputs:
          report_name: conformance-purpose
          format: md
          out: ".artifacts/conformance-purpose-summary.md"
      - id: on_fail
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-002.fail.json"
          format: json
          report_name: DCCONF-JOB-REP-002.fail
      - id: on_complete
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-002.complete.json"
          format: json
          report_name: DCCONF-JOB-REP-002.complete
      use:
      - ref: "/specs/libraries/policy/policy_job.spec.md"
        as: lib_policy_job
        symbols:
        - policy.job.dispatch_ok
        - policy.job.written_path_contains
      spec_lang:
        capabilities:
        - ops.helper
        - ops.job
  - id: svc.assert_check.default.3
    config:
      jobs:
      - id: main
        mode: report
        helper: helper.report.emit
        inputs:
          report_name: spec-portability
          format: json
          out: ".artifacts/spec-portability.json"
      - id: on_fail
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-003.fail.json"
          format: json
          report_name: DCCONF-JOB-REP-003.fail
      - id: on_complete
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-003.complete.json"
          format: json
          report_name: DCCONF-JOB-REP-003.complete
      use:
      - ref: "/specs/libraries/policy/policy_job.spec.md"
        as: lib_policy_job
        symbols:
        - policy.job.dispatch_ok
        - policy.job.written_path_contains
      spec_lang:
        capabilities:
        - ops.helper
        - ops.job
  - id: svc.assert_check.default.4
    config:
      jobs:
      - id: main
        mode: report
        helper: helper.report.emit
        inputs:
          report_name: spec-portability
          format: md
          out: ".artifacts/spec-portability-summary.md"
      - id: on_fail
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-004.fail.json"
          format: json
          report_name: DCCONF-JOB-REP-004.fail
      - id: on_complete
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-004.complete.json"
          format: json
          report_name: DCCONF-JOB-REP-004.complete
      use:
      - ref: "/specs/libraries/policy/policy_job.spec.md"
        as: lib_policy_job
        symbols:
        - policy.job.dispatch_ok
        - policy.job.written_path_contains
      spec_lang:
        capabilities:
        - ops.helper
        - ops.job
  - id: svc.assert_check.default.5
    config:
      jobs:
      - id: main
        mode: report
        helper: helper.report.emit
        inputs:
          report_name: contract-assertions
          format: json
          out: ".artifacts/contract-assertions.json"
      - id: on_fail
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-005.fail.json"
          format: json
          report_name: DCCONF-JOB-REP-005.fail
      - id: on_complete
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-005.complete.json"
          format: json
          report_name: DCCONF-JOB-REP-005.complete
      use:
      - ref: "/specs/libraries/policy/policy_job.spec.md"
        as: lib_policy_job
        symbols:
        - policy.job.dispatch_ok
        - policy.job.written_path_contains
      spec_lang:
        capabilities:
        - ops.helper
        - ops.job
  - id: svc.assert_check.default.6
    config:
      jobs:
      - id: main
        mode: report
        helper: helper.report.emit
        inputs:
          report_name: contract-assertions
          format: md
          out: ".artifacts/contract-assertions-summary.md"
      - id: on_fail
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-006.fail.json"
          format: json
          report_name: DCCONF-JOB-REP-006.fail
      - id: on_complete
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-006.complete.json"
          format: json
          report_name: DCCONF-JOB-REP-006.complete
      use:
      - ref: "/specs/libraries/policy/policy_job.spec.md"
        as: lib_policy_job
        symbols:
        - policy.job.dispatch_ok
        - policy.job.written_path_contains
      spec_lang:
        capabilities:
        - ops.helper
        - ops.job
  - id: svc.assert_check.default.7
    config:
      jobs:
      - id: main
        mode: report
        helper: helper.report.emit
        inputs:
          report_name: spec-lang-adoption
          format: json
          out: ".artifacts/spec-lang-adoption.json"
      - id: on_fail
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-007.fail.json"
          format: json
          report_name: DCCONF-JOB-REP-007.fail
      - id: on_complete
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-007.complete.json"
          format: json
          report_name: DCCONF-JOB-REP-007.complete
      use:
      - ref: "/specs/libraries/policy/policy_job.spec.md"
        as: lib_policy_job
        symbols:
        - policy.job.dispatch_ok
        - policy.job.written_path_contains
      spec_lang:
        capabilities:
        - ops.helper
        - ops.job
  - id: svc.assert_check.default.8
    config:
      jobs:
      - id: main
        mode: report
        helper: helper.report.emit
        inputs:
          report_name: spec-lang-adoption
          format: md
          out: ".artifacts/spec-lang-adoption-summary.md"
      - id: on_fail
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-008.fail.json"
          format: json
          report_name: DCCONF-JOB-REP-008.fail
      - id: on_complete
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-008.complete.json"
          format: json
          report_name: DCCONF-JOB-REP-008.complete
      use:
      - ref: "/specs/libraries/policy/policy_job.spec.md"
        as: lib_policy_job
        symbols:
        - policy.job.dispatch_ok
        - policy.job.written_path_contains
      spec_lang:
        capabilities:
        - ops.helper
        - ops.job
  - id: svc.assert_check.default.9
    config:
      jobs:
      - id: main
        mode: report
        helper: helper.report.emit
        inputs:
          report_name: runner-independence
          format: json
          out: ".artifacts/runner-independence.json"
      - id: on_fail
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-009.fail.json"
          format: json
          report_name: DCCONF-JOB-REP-009.fail
      - id: on_complete
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-009.complete.json"
          format: json
          report_name: DCCONF-JOB-REP-009.complete
      use:
      - ref: "/specs/libraries/policy/policy_job.spec.md"
        as: lib_policy_job
        symbols:
        - policy.job.dispatch_ok
        - policy.job.written_path_contains
      spec_lang:
        capabilities:
        - ops.helper
        - ops.job
  - id: svc.assert_check.default.10
    config:
      jobs:
      - id: main
        mode: report
        helper: helper.report.emit
        inputs:
          report_name: runner-independence
          format: md
          out: ".artifacts/runner-independence-summary.md"
      - id: on_fail
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-010.fail.json"
          format: json
          report_name: DCCONF-JOB-REP-010.fail
      - id: on_complete
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-010.complete.json"
          format: json
          report_name: DCCONF-JOB-REP-010.complete
      use:
      - ref: "/specs/libraries/policy/policy_job.spec.md"
        as: lib_policy_job
        symbols:
        - policy.job.dispatch_ok
        - policy.job.written_path_contains
      spec_lang:
        capabilities:
        - ops.helper
        - ops.job
  - id: svc.assert_check.default.11
    config:
      jobs:
      - id: main
        mode: report
        helper: helper.report.emit
        inputs:
          report_name: python-dependency
          format: json
          out: ".artifacts/python-dependency.json"
      - id: on_fail
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-011.fail.json"
          format: json
          report_name: DCCONF-JOB-REP-011.fail
      - id: on_complete
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-011.complete.json"
          format: json
          report_name: DCCONF-JOB-REP-011.complete
      use:
      - ref: "/specs/libraries/policy/policy_job.spec.md"
        as: lib_policy_job
        symbols:
        - policy.job.dispatch_ok
        - policy.job.written_path_contains
      spec_lang:
        capabilities:
        - ops.helper
        - ops.job
  - id: svc.assert_check.default.12
    config:
      jobs:
      - id: main
        mode: report
        helper: helper.report.emit
        inputs:
          report_name: python-dependency
          format: md
          out: ".artifacts/python-dependency-summary.md"
      - id: on_fail
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-012.fail.json"
          format: json
          report_name: DCCONF-JOB-REP-012.fail
      - id: on_complete
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-012.complete.json"
          format: json
          report_name: DCCONF-JOB-REP-012.complete
      use:
      - ref: "/specs/libraries/policy/policy_job.spec.md"
        as: lib_policy_job
        symbols:
        - policy.job.dispatch_ok
        - policy.job.written_path_contains
      spec_lang:
        capabilities:
        - ops.helper
        - ops.job
  - id: svc.assert_check.default.13
    config:
      jobs:
      - id: main
        mode: report
        helper: helper.report.emit
        inputs:
          report_name: docs-operability
          format: json
          out: ".artifacts/docs-operability.json"
      - id: on_fail
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-013.fail.json"
          format: json
          report_name: DCCONF-JOB-REP-013.fail
      - id: on_complete
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-013.complete.json"
          format: json
          report_name: DCCONF-JOB-REP-013.complete
      use:
      - ref: "/specs/libraries/policy/policy_job.spec.md"
        as: lib_policy_job
        symbols:
        - policy.job.dispatch_ok
        - policy.job.written_path_contains
      spec_lang:
        capabilities:
        - ops.helper
        - ops.job
  - id: svc.assert_check.default.14
    config:
      jobs:
      - id: main
        mode: report
        helper: helper.report.emit
        inputs:
          report_name: docs-operability
          format: md
          out: ".artifacts/docs-operability-summary.md"
      - id: on_fail
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-014.fail.json"
          format: json
          report_name: DCCONF-JOB-REP-014.fail
      - id: on_complete
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-014.complete.json"
          format: json
          report_name: DCCONF-JOB-REP-014.complete
      use:
      - ref: "/specs/libraries/policy/policy_job.spec.md"
        as: lib_policy_job
        symbols:
        - policy.job.dispatch_ok
        - policy.job.written_path_contains
      spec_lang:
        capabilities:
        - ops.helper
        - ops.job
  - id: svc.assert_check.default.15
    config:
      jobs:
      - id: main
        mode: report
        helper: helper.report.emit
        inputs:
          report_name: objective-scorecard
          format: json
          out: ".artifacts/objective-scorecard.json"
      - id: on_fail
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-015.fail.json"
          format: json
          report_name: DCCONF-JOB-REP-015.fail
      - id: on_complete
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-015.complete.json"
          format: json
          report_name: DCCONF-JOB-REP-015.complete
      use:
      - ref: "/specs/libraries/policy/policy_job.spec.md"
        as: lib_policy_job
        symbols:
        - policy.job.dispatch_ok
        - policy.job.written_path_contains
      spec_lang:
        capabilities:
        - ops.helper
        - ops.job
  - id: svc.assert_check.default.16
    config:
      jobs:
      - id: main
        mode: report
        helper: helper.report.emit
        inputs:
          report_name: objective-scorecard
          format: md
          out: ".artifacts/objective-scorecard-summary.md"
      - id: on_fail
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-016.fail.json"
          format: json
          report_name: DCCONF-JOB-REP-016.fail
      - id: on_complete
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-016.complete.json"
          format: json
          report_name: DCCONF-JOB-REP-016.complete
      use:
      - ref: "/specs/libraries/policy/policy_job.spec.md"
        as: lib_policy_job
        symbols:
        - policy.job.dispatch_ok
        - policy.job.written_path_contains
      spec_lang:
        capabilities:
        - ops.helper
        - ops.job
  - id: svc.assert_check.default.17
    config:
      jobs:
      - id: main
        mode: report
        helper: helper.report.emit
        inputs:
          report_name: spec-lang-stdlib
          format: json
          out: ".artifacts/spec-lang-stdlib.json"
      - id: on_fail
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-017.fail.json"
          format: json
          report_name: DCCONF-JOB-REP-017.fail
      - id: on_complete
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-017.complete.json"
          format: json
          report_name: DCCONF-JOB-REP-017.complete
      use:
      - ref: "/specs/libraries/policy/policy_job.spec.md"
        as: lib_policy_job
        symbols:
        - policy.job.dispatch_ok
        - policy.job.written_path_contains
      spec_lang:
        capabilities:
        - ops.helper
        - ops.job
  - id: svc.assert_check.default.18
    config:
      jobs:
      - id: main
        mode: report
        helper: helper.report.emit
        inputs:
          report_name: spec-lang-stdlib
          format: md
          out: ".artifacts/spec-lang-stdlib-summary.md"
      - id: on_fail
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-018.fail.json"
          format: json
          report_name: DCCONF-JOB-REP-018.fail
      - id: on_complete
        helper: helper.report.emit
        mode: report
        inputs:
          out: ".artifacts/job-hooks/DCCONF-JOB-REP-018.complete.json"
          format: json
          report_name: DCCONF-JOB-REP-018.complete
      use:
      - ref: "/specs/libraries/policy/policy_job.spec.md"
        as: lib_policy_job
        symbols:
        - policy.job.dispatch_ok
        - policy.job.written_path_contains
      spec_lang:
        capabilities:
        - ops.helper
        - ops.job
contracts:
- id: DCCONF-JOB-REP-001
  title: conformance purpose json report
  purpose: Ensures report contract jobs dispatch and write the expected artifact output path.
  clauses:
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
      - ops.job.dispatch:
        - main
      - call:
        - var: policy.job.dispatch_ok
        - var: summary_json
      - call:
        - var: policy.job.written_path_contains
        - var: summary_json
        - ".artifacts/conformance-purpose.json"
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
- id: DCCONF-JOB-REP-002
  title: conformance purpose markdown report
  purpose: Ensures report contract jobs dispatch and write the expected artifact output path.
  clauses:
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
      - ops.job.dispatch:
        - main
      - call:
        - var: policy.job.dispatch_ok
        - var: summary_json
      - call:
        - var: policy.job.written_path_contains
        - var: summary_json
        - ".artifacts/conformance-purpose-summary.md"
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
- id: DCCONF-JOB-REP-003
  title: spec portability json report
  purpose: Ensures report contract jobs dispatch and write the expected artifact output path.
  clauses:
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
      - ops.job.dispatch:
        - main
      - call:
        - var: policy.job.dispatch_ok
        - var: summary_json
      - call:
        - var: policy.job.written_path_contains
        - var: summary_json
        - ".artifacts/spec-portability.json"
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
- id: DCCONF-JOB-REP-004
  title: spec portability markdown report
  purpose: Ensures report contract jobs dispatch and write the expected artifact output path.
  clauses:
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
      - ops.job.dispatch:
        - main
      - call:
        - var: policy.job.dispatch_ok
        - var: summary_json
      - call:
        - var: policy.job.written_path_contains
        - var: summary_json
        - ".artifacts/spec-portability-summary.md"
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
- id: DCCONF-JOB-REP-005
  title: contract assertions json report
  purpose: Ensures report contract jobs dispatch and write the expected artifact output path.
  clauses:
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
      - ops.job.dispatch:
        - main
      - call:
        - var: policy.job.dispatch_ok
        - var: summary_json
      - call:
        - var: policy.job.written_path_contains
        - var: summary_json
        - ".artifacts/contract-assertions.json"
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
- id: DCCONF-JOB-REP-006
  title: contract assertions markdown report
  purpose: Ensures report contract jobs dispatch and write the expected artifact output path.
  clauses:
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
      - ops.job.dispatch:
        - main
      - call:
        - var: policy.job.dispatch_ok
        - var: summary_json
      - call:
        - var: policy.job.written_path_contains
        - var: summary_json
        - ".artifacts/contract-assertions-summary.md"
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
- id: DCCONF-JOB-REP-007
  title: spec lang adoption json report
  purpose: Ensures report contract jobs dispatch and write the expected artifact output path.
  clauses:
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
      - ops.job.dispatch:
        - main
      - call:
        - var: policy.job.dispatch_ok
        - var: summary_json
      - call:
        - var: policy.job.written_path_contains
        - var: summary_json
        - ".artifacts/spec-lang-adoption.json"
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
- id: DCCONF-JOB-REP-008
  title: spec lang adoption markdown report
  purpose: Ensures report contract jobs dispatch and write the expected artifact output path.
  clauses:
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
      - ops.job.dispatch:
        - main
      - call:
        - var: policy.job.dispatch_ok
        - var: summary_json
      - call:
        - var: policy.job.written_path_contains
        - var: summary_json
        - ".artifacts/spec-lang-adoption-summary.md"
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
- id: DCCONF-JOB-REP-009
  title: runner independence json report
  purpose: Ensures report contract jobs dispatch and write the expected artifact output path.
  clauses:
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
      - ops.job.dispatch:
        - main
      - call:
        - var: policy.job.dispatch_ok
        - var: summary_json
      - call:
        - var: policy.job.written_path_contains
        - var: summary_json
        - ".artifacts/runner-independence.json"
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
- id: DCCONF-JOB-REP-010
  title: runner independence markdown report
  purpose: Ensures report contract jobs dispatch and write the expected artifact output path.
  clauses:
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
      - ops.job.dispatch:
        - main
      - call:
        - var: policy.job.dispatch_ok
        - var: summary_json
      - call:
        - var: policy.job.written_path_contains
        - var: summary_json
        - ".artifacts/runner-independence-summary.md"
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
- id: DCCONF-JOB-REP-011
  title: python dependency json report
  purpose: Ensures report contract jobs dispatch and write the expected artifact output path.
  clauses:
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
      - ops.job.dispatch:
        - main
      - call:
        - var: policy.job.dispatch_ok
        - var: summary_json
      - call:
        - var: policy.job.written_path_contains
        - var: summary_json
        - ".artifacts/python-dependency.json"
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
- id: DCCONF-JOB-REP-012
  title: python dependency markdown report
  purpose: Ensures report contract jobs dispatch and write the expected artifact output path.
  clauses:
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
      - ops.job.dispatch:
        - main
      - call:
        - var: policy.job.dispatch_ok
        - var: summary_json
      - call:
        - var: policy.job.written_path_contains
        - var: summary_json
        - ".artifacts/python-dependency-summary.md"
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
- id: DCCONF-JOB-REP-013
  title: docs operability json report
  purpose: Ensures report contract jobs dispatch and write the expected artifact output path.
  clauses:
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
      - ops.job.dispatch:
        - main
      - call:
        - var: policy.job.dispatch_ok
        - var: summary_json
      - call:
        - var: policy.job.written_path_contains
        - var: summary_json
        - ".artifacts/docs-operability.json"
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
- id: DCCONF-JOB-REP-014
  title: docs operability markdown report
  purpose: Ensures report contract jobs dispatch and write the expected artifact output path.
  clauses:
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
      - ops.job.dispatch:
        - main
      - call:
        - var: policy.job.dispatch_ok
        - var: summary_json
      - call:
        - var: policy.job.written_path_contains
        - var: summary_json
        - ".artifacts/docs-operability-summary.md"
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
- id: DCCONF-JOB-REP-015
  title: objective scorecard json report
  purpose: Ensures report contract jobs dispatch and write the expected artifact output path.
  clauses:
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
      - ops.job.dispatch:
        - main
      - call:
        - var: policy.job.dispatch_ok
        - var: summary_json
      - call:
        - var: policy.job.written_path_contains
        - var: summary_json
        - ".artifacts/objective-scorecard.json"
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
- id: DCCONF-JOB-REP-016
  title: objective scorecard markdown report
  purpose: Ensures report contract jobs dispatch and write the expected artifact output path.
  clauses:
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
      - ops.job.dispatch:
        - main
      - call:
        - var: policy.job.dispatch_ok
        - var: summary_json
      - call:
        - var: policy.job.written_path_contains
        - var: summary_json
        - ".artifacts/objective-scorecard-summary.md"
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
- id: DCCONF-JOB-REP-017
  title: spec lang stdlib json report
  purpose: Ensures report contract jobs dispatch and write the expected artifact output path.
  clauses:
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
      - ops.job.dispatch:
        - main
      - call:
        - var: policy.job.dispatch_ok
        - var: summary_json
      - call:
        - var: policy.job.written_path_contains
        - var: summary_json
        - ".artifacts/spec-lang-stdlib.json"
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
- id: DCCONF-JOB-REP-018
  title: spec lang stdlib markdown report
  purpose: Ensures report contract jobs dispatch and write the expected artifact output path.
  clauses:
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
      - ops.job.dispatch:
        - main
      - call:
        - var: policy.job.dispatch_ok
        - var: summary_json
      - call:
        - var: policy.job.written_path_contains
        - var: summary_json
        - ".artifacts/spec-lang-stdlib-summary.md"
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
```


































