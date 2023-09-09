from pathlib import Path

IMAGES_PATH = Path(__file__).absolute().resolve().parent.parent / "images"
SOUNDS_DIR = (
    Path(__file__).absolute().resolve().parent.parent / "sounds" / "classical_guitar"
)

LOAD_IMAGE_TIMER_IN_MS = 3000
