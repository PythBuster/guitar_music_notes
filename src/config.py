from pathlib import Path

PYPROJECT_PATH = Path(__file__).absolute().resolve().parent.parent / "pyproject.toml"
IMAGES_PATH = Path(__file__).absolute().resolve().parent.parent / "images"
SOUNDS_DIR = (
    Path(__file__).absolute().resolve().parent.parent / "sounds" / "classical_guitar"
)

LOAD_IMAGE_TIMER_IN_MS = 4000
