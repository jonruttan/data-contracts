DEFAULT_CASE_FILE_PATTERN = "*.spec.md"
ENV_ASSERT_HEALTH = "SPEC_RUNNER_ASSERT_HEALTH"
ENV_ENTRYPOINT = "SPEC_RUNNER_ENTRYPOINT"
ENV_SAFE_MODE = "SPEC_RUNNER_SAFE_MODE"
ENV_ENV_ALLOWLIST = "SPEC_RUNNER_ENV_ALLOWLIST"
DEFAULT_ASSERT_HEALTH_MODE = "ignore"


def governed_config_literals() -> dict[str, str]:
    return {
        DEFAULT_CASE_FILE_PATTERN: "DEFAULT_CASE_FILE_PATTERN",
        ENV_ASSERT_HEALTH: "ENV_ASSERT_HEALTH",
        ENV_ENTRYPOINT: "ENV_ENTRYPOINT",
        ENV_SAFE_MODE: "ENV_SAFE_MODE",
        ENV_ENV_ALLOWLIST: "ENV_ENV_ALLOWLIST",
    }


def resolve_case_file_pattern(file_pattern: str | None) -> str:
    raw = str(file_pattern or "").strip()
    return raw or DEFAULT_CASE_FILE_PATTERN


def case_file_name(stem: str, *, file_pattern: str | None = None) -> str:
    pattern = resolve_case_file_pattern(file_pattern)
    if pattern.startswith("*.") and "*" not in pattern[1:] and "?" not in pattern and "[" not in pattern:
        return f"{stem}{pattern[1:]}"
    raise ValueError(f"cannot derive case filename stem from glob pattern: {pattern}")
