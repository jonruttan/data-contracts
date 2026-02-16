from __future__ import annotations

import subprocess
from pathlib import Path


def run_process_op(
    *,
    command: list[str],
    cwd: str | Path | None = None,
    env: dict[str, str] | None = None,
    check: bool = False,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [str(x) for x in command],
        cwd=None if cwd is None else str(cwd),
        env=env,
        check=check,
        capture_output=True,
        text=True,
    )
