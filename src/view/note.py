from pathlib import Path

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from src.custom_types import NoteType


def map_note_type(image_path: Path) -> NoteType:
    image_name = image_path.name.split(".")[0]

    if image_name.startswith("'"):  # ''f
        image_name = image_name[::-2].upper()

    print("Note:", image_name, flush=True)
    return NoteType(image_name)


class Note(QWidget):
    def __init__(self, image_path: Path):
        super().__init__()
        self.image_label = QLabel()

        self.orig_filename = image_path.name.replace(".png", "")
        self.note_type = map_note_type(image_path=image_path)
        self.image_path = image_path

        self.qpixmap = QPixmap(image_path)
        self.image_label.setPixmap(self.qpixmap)

        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)
        self.setLayout(vbox)

    @property
    def name(self) -> str:
        return str(self.note_type)
