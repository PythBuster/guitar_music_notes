import sys

from PySide6.QtWidgets import QApplication

from config import IMAGES_PATH, LOAD_IMAGE_TIMER_IN_MS
from src.view.viewer import Viewer

app = QApplication(sys.argv)

viewer = Viewer(
    images_dir=IMAGES_PATH,
    image_load_timer_in_ms=LOAD_IMAGE_TIMER_IN_MS,
)

viewer.show()

app.exec()
