.PHONY: help setup docs-doctor check ci-gate test
.DEFAULT_GOAL := help

help: ## Display this help section
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "\033[32m%-38s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

setup: ## Create .venv and install editable package with dev deps
	@python3 -m venv .venv
	@.venv/bin/python -m pip install -U pip
	@.venv/bin/python -m pip install -e '.[dev]'

docs-doctor: ## Run fast docs quality checks
	@./scripts/docs_doctor.sh

check: ## Alias for ci-gate
	@$(MAKE) ci-gate

ci-gate: ## Run full CI gate locally
	@./scripts/ci_gate.sh

test: ## Run pytest
	@.venv/bin/python -m pytest
