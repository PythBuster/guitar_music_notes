"""All global app data are located here."""

from pathlib import Path

PYPROJECT_PATH = Path(__file__).absolute().resolve().parent.parent / "pyproject.toml"
IMAGES_PATH = Path(__file__).absolute().resolve().parent.parent / "images"
SOUNDS_PATH = (
    Path(__file__).absolute().resolve().parent.parent / "sounds" / "classical_guitar"
)

LOAD_IMAGE_TIMER_IN_MS = 4000
SHOW_SOLUTION_TIMER_IN_MS = 2000
MAX_TIMER_IN_SEC = 10
MIC_NAME = "SC450USB"
