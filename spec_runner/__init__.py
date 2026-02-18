from __future__ import annotations

from pathlib import Path

# Keep the import namespace stable while the implementation package lives under
# runners/python/spec_runner.
_PKG_DIR = Path(__file__).resolve().parent
_IMPL_DIR = _PKG_DIR.parent / "runners" / "python" / "spec_runner"

if _IMPL_DIR.is_dir():
    __path__.append(str(_IMPL_DIR))
