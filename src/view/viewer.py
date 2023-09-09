import os
import random
from pathlib import Path

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QWidget

from src.custom_types import NoteType
from src.view.note import Note
from src.view.ui.ui_viewer import Ui_Viewer


class Viewer(QWidget, Ui_Viewer):
    def __init__(
        self,
        images_dir: Path,
        sounds_dir: Path,
        training_notes: set[NoteType] | None = None,
        image_load_timer_in_ms: int | None = None,
    ):
        super().__init__()
        self.setupUi(self)

        self.images_dir = images_dir
        self.sounds_dir = sounds_dir
        self.training_notes = training_notes
        self.image_load_timer_in_ms = image_load_timer_in_ms

        if self.image_load_timer_in_ms is not None:
            self.pushButton_next.setVisible(False)

            self.timer = QTimer()
            self.timer.timeout.connect(self.load_image)
            self.timer.start(image_load_timer_in_ms)
        else:
            self.pushButton_next.setVisible(True)
            self.pushButton_next.clicked.connect(self.load_image)

        self.current_note = None

        images_paths = [
            self.images_dir / image_name
            for image_name in os.listdir(self.images_dir)
            if not image_name.startswith("_")
        ]
        images = {NoteType(image_path.stem): image_path for image_path in images_paths}
        self.image_paths = [
            value
            for key, value in images.items()
            if self.training_notes is None or key in self.training_notes
        ]

        self._reorder_image_paths()

        self.load_image()
        self.setFixedSize(self.sizeHint())

    def _reorder_image_paths(self):
        self._next_image_iteration = 0
        random.shuffle(self.image_paths)
        self.next_image_iter = iter(self.image_paths)

    def next_image(self) -> Path:
        self._next_image_iteration += 1

        if self._next_image_iteration >= len(self.image_paths):
            self._reorder_image_paths()

        return next(self.next_image_iter)

    def load_image(self):
        next_note = Note(
            image_path=self.next_image(),
            sound_path=self.sounds_dir,
            image_label=self.label_image,
        )

        # if self.current_note is None:
        #    self.current_note = next_note
        #    self.root_layout.addWidget(self.current_note)
        # else:
        #    self.root_layout.removeWidget(self.current_note)
        #    self.current_note = next_note
        #    self.root_layout.addWidget(self.current_note)

        self.update()
        next_note.play_sound()

    def closeEvent(self, event):
        event.accept()
