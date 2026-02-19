.PHONY: help setup hooks-install docs-doctor verify-docs docs-build docs-generate docs-generate-check docs-lint docs-check schema-registry-check schema-registry-build schema-docs-check schema-docs-build normalize-check normalize-fix core-check ci-smoke ci-cleanroom ci-gate check prepush prepush-fast perf-smoke test
.DEFAULT_GOAL := help

help: ## Display this help section
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "\033[32m%-38s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

# ---------------------------------------------------------------------------
# Bootstrap
# ---------------------------------------------------------------------------

setup: ## Create .venv and install editable package with dev deps
	@python3 -m venv .venv
	@.venv/bin/python -m pip install -U pip
	@.venv/bin/python -m pip install -e '.[dev]'

hooks-install: ## Install managed git hooks (enforces local pre-push parity gate)
	@./scripts/install_git_hooks.sh

# ---------------------------------------------------------------------------
# Docs
# ---------------------------------------------------------------------------

docs-doctor: ## Run fast docs quality checks
	@./scripts/docs_doctor.sh

verify-docs: ## Alias for docs-doctor
	@$(MAKE) docs-doctor

docs-build: ## Generate reference docs artifacts (index, coverage, graph)
	@./runners/public/runner_adapter.sh --impl rust docs-build

docs-generate: ## Generate all registry-backed docs surfaces
	@./runners/public/runner_adapter.sh --impl rust docs-generate

docs-generate-check: ## Verify all registry-backed docs surfaces are up-to-date
	@./runners/public/runner_adapter.sh --impl rust docs-generate-check

docs-lint: ## Run docs metadata/schema and quality lint checks
	@./runners/public/runner_adapter.sh --impl rust docs-lint

docs-check: ## Verify generated docs artifacts are up-to-date and lint passes
	@./runners/public/runner_adapter.sh --impl rust docs-build-check
	@./runners/public/runner_adapter.sh --impl rust docs-lint

# ---------------------------------------------------------------------------
# Schema + Normalization
# ---------------------------------------------------------------------------

normalize-check: ## Verify normalization across specs/contracts/tests
	@./runners/public/runner_adapter.sh --impl rust normalize-check

normalize-fix: ## Apply normalization rewrites across specs/contracts/tests
	@./runners/public/runner_adapter.sh --impl rust normalize-fix

schema-registry-check: ## Verify schema registry artifacts and docs are up-to-date
	@./runners/public/runner_adapter.sh --impl rust schema-registry-check
	@./runners/public/runner_adapter.sh --impl rust schema-docs-check

schema-registry-build: ## Build schema registry artifacts and generated schema docs
	@./runners/public/runner_adapter.sh --impl rust schema-registry-build
	@./runners/public/runner_adapter.sh --impl rust schema-docs-build

schema-docs-check: ## Verify generated schema docs snapshot is up-to-date
	@./runners/public/runner_adapter.sh --impl rust schema-docs-check

schema-docs-build: ## Regenerate schema docs snapshot from registry
	@./runners/public/runner_adapter.sh --impl rust schema-docs-build

# ---------------------------------------------------------------------------
# Gate Profiles
# ---------------------------------------------------------------------------

ci-smoke: ## Fast CI preflight (governance + docs + style)
	@./runners/public/runner_adapter.sh --impl rust governance
	@./runners/public/runner_adapter.sh --impl rust docs-generate-check
	@./runners/public/runner_adapter.sh --impl rust docs-lint
	@./runners/public/runner_adapter.sh --impl rust normalize-check
	@./runners/public/runner_adapter.sh --impl rust schema-registry-check
	@./runners/public/runner_adapter.sh --impl rust schema-docs-check
	@./runners/public/runner_adapter.sh --impl rust style-check

ci-cleanroom: ## Run full CI gate in a fresh git worktree (clean-checkout parity)
	@./runners/public/runner_adapter.sh --impl rust ci-cleanroom

core-check: ## Run lightweight core adoption checks
	@./scripts/core_gate.sh

ci-gate: ## Run full CI gate locally
	@./scripts/ci_gate.sh

check: ## Canonical alias for ci-gate
	@$(MAKE) ci-gate

# ---------------------------------------------------------------------------
# Pre-push
# ---------------------------------------------------------------------------

perf-smoke: ## Run governance/docs timing checks against perf baselines (warn mode)
	@./runners/public/runner_adapter.sh --impl rust perf-smoke --mode warn

prepush: ## Required local pre-push gate (default rust critical-gate path)
	@SPEC_PREPUSH_MODE=critical ./scripts/local_ci_parity.sh

prepush-fast: ## Rust-only critical pre-push mode
	@SPEC_PREPUSH_MODE=fast ./scripts/local_ci_parity.sh

# ---------------------------------------------------------------------------
# Local tests
# ---------------------------------------------------------------------------

test: ## Run rust-required full test lane
	@./runners/public/runner_adapter.sh --impl rust test-full
