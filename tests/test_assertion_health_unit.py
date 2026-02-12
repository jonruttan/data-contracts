from spec_runner.assertion_health import (
    format_assertion_health_error,
    lint_assert_tree,
    resolve_assert_health_mode,
)


def test_resolve_mode_defaults_to_ignore():
    assert resolve_assert_health_mode({}, env={}) == "ignore"


def test_resolve_mode_uses_env_and_per_test_override():
    assert resolve_assert_health_mode({}, env={"SPEC_RUNNER_ASSERT_HEALTH": "warn"}) == "warn"
    assert (
        resolve_assert_health_mode(
            {"assert_health": {"mode": "error"}},
            env={"SPEC_RUNNER_ASSERT_HEALTH": "warn"},
        )
        == "error"
    )


def test_lint_detects_always_true_and_duplicates():
    diags = lint_assert_tree(
        [
            {"target": "stdout", "must": [{"contain": ["", "ok", "ok"]}]},
            {"target": "stderr", "cannot": [{"regex": [".*"]}]},
        ]
    )
    codes = {d.code for d in diags}
    assert {"AH001", "AH002", "AH003"} <= codes
    msg = format_assertion_health_error(diags)
    assert "assertion health check failed" in msg
