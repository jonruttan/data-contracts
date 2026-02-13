# SPEC-OPT-OUT: This policy guard validates repository test governance that cannot be represented as a runtime spec case.
from pathlib import Path


def test_unit_test_files_declare_opt_out_reason() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    unit_test_files = sorted((repo_root / "tests").glob("test_*_unit.py"))
    assert unit_test_files, "expected at least one unit test file"

    for path in unit_test_files:
        lines = path.read_text(encoding="utf-8").splitlines()
        header = lines[0].strip() if lines else ""
        assert header.startswith("# SPEC-OPT-OUT:"), f"missing SPEC-OPT-OUT header in {path}"
        reason = header.removeprefix("# SPEC-OPT-OUT:").strip()
        assert reason, f"empty SPEC-OPT-OUT reason in {path}"
