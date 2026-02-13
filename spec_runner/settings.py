DEFAULT_CASE_FILE_PATTERN = "*.spec.md"


def resolve_case_file_pattern(file_pattern: str | None) -> str:
    raw = str(file_pattern or "").strip()
    return raw or DEFAULT_CASE_FILE_PATTERN


def case_file_name(stem: str, *, file_pattern: str | None = None) -> str:
    pattern = resolve_case_file_pattern(file_pattern)
    if pattern.startswith("*.") and "*" not in pattern[1:] and "?" not in pattern and "[" not in pattern:
        return f"{stem}{pattern[1:]}"
    raise ValueError(f"cannot derive case filename stem from glob pattern: {pattern}")
