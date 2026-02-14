from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CaseSettings:
    default_file_pattern: str


@dataclass(frozen=True)
class EnvSettings:
    assert_health: str
    entrypoint: str
    safe_mode: str
    env_allowlist: str


@dataclass(frozen=True)
class AssertionHealthSettings:
    default_mode: str


@dataclass(frozen=True)
class SpecPortabilitySegmentRuleSettings:
    prefix: str
    segment: str


@dataclass(frozen=True)
class SpecPortabilityWeightsSettings:
    non_evaluate_leaf_share: float
    expect_impl_overlay: float
    runtime_specific_capability: float
    non_core_type: float


@dataclass(frozen=True)
class SpecPortabilityReportSettings:
    top_n: int


@dataclass(frozen=True)
class SpecPortabilitySettings:
    roots: tuple[str, ...]
    core_types: tuple[str, ...]
    segment_rules: tuple[SpecPortabilitySegmentRuleSettings, ...]
    runtime_capability_tokens: tuple[str, ...]
    runtime_capability_prefixes: tuple[str, ...]
    weights: SpecPortabilityWeightsSettings
    report: SpecPortabilityReportSettings
    recursive: bool
    min_overall_ratio: float | None
    min_segment_ratios: dict[str, float]
    enforce: bool


@dataclass(frozen=True)
class RunnerSettings:
    case: CaseSettings
    env: EnvSettings
    assertion_health: AssertionHealthSettings
    spec_portability: SpecPortabilitySettings


SETTINGS = RunnerSettings(
    case=CaseSettings(default_file_pattern="*.spec.md"),
    env=EnvSettings(
        assert_health="SPEC_RUNNER_ASSERT_HEALTH",
        entrypoint="SPEC_RUNNER_ENTRYPOINT",
        safe_mode="SPEC_RUNNER_SAFE_MODE",
        env_allowlist="SPEC_RUNNER_ENV_ALLOWLIST",
    ),
    assertion_health=AssertionHealthSettings(default_mode="ignore"),
    spec_portability=SpecPortabilitySettings(
        roots=(
            "docs/spec/conformance/cases",
            "docs/spec/governance/cases",
            "docs/spec/impl",
        ),
        core_types=("text.file", "cli.run"),
        segment_rules=(
            SpecPortabilitySegmentRuleSettings(
                prefix="docs/spec/conformance/cases",
                segment="conformance",
            ),
            SpecPortabilitySegmentRuleSettings(
                prefix="docs/spec/governance/cases",
                segment="governance",
            ),
            SpecPortabilitySegmentRuleSettings(
                prefix="docs/spec/impl",
                segment="impl",
            ),
        ),
        runtime_capability_tokens=("api.http", "governance.check"),
        runtime_capability_prefixes=("runtime.", "php.", "python."),
        weights=SpecPortabilityWeightsSettings(
            non_evaluate_leaf_share=0.45,
            expect_impl_overlay=0.25,
            runtime_specific_capability=0.15,
            non_core_type=0.15,
        ),
        report=SpecPortabilityReportSettings(top_n=10),
        recursive=True,
        min_overall_ratio=None,
        min_segment_ratios={},
        enforce=False,
    ),
)

# Backward-compatible aliases for existing call sites/tests.
DEFAULT_CASE_FILE_PATTERN = SETTINGS.case.default_file_pattern
ENV_ASSERT_HEALTH = SETTINGS.env.assert_health
ENV_ENTRYPOINT = SETTINGS.env.entrypoint
ENV_SAFE_MODE = SETTINGS.env.safe_mode
ENV_ENV_ALLOWLIST = SETTINGS.env.env_allowlist
DEFAULT_ASSERT_HEALTH_MODE = SETTINGS.assertion_health.default_mode


def governed_config_literals() -> dict[str, str]:
    return {
        SETTINGS.case.default_file_pattern: "SETTINGS.case.default_file_pattern",
        SETTINGS.env.assert_health: "SETTINGS.env.assert_health",
        SETTINGS.env.entrypoint: "SETTINGS.env.entrypoint",
        SETTINGS.env.safe_mode: "SETTINGS.env.safe_mode",
        SETTINGS.env.env_allowlist: "SETTINGS.env.env_allowlist",
    }


def resolve_case_file_pattern(file_pattern: str | None) -> str:
    raw = str(file_pattern or "").strip()
    return raw or SETTINGS.case.default_file_pattern


def case_file_name(stem: str, *, file_pattern: str | None = None) -> str:
    pattern = resolve_case_file_pattern(file_pattern)
    if pattern.startswith("*.") and "*" not in pattern[1:] and "?" not in pattern and "[" not in pattern:
        return f"{stem}{pattern[1:]}"
    raise ValueError(f"cannot derive case filename stem from glob pattern: {pattern}")
