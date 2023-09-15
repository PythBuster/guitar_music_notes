"""The viewer module with all the logic and classes around the viewer UI."""

import os
import random
from pathlib import Path
from typing import Any, Generator, MutableSequence

from PySide6.QtCore import QEvent, QTimer
from PySide6.QtWidgets import QWidget

from src.custom_types import NoteType
from src.view.note import Note
from src.view.ui.ui_viewer import Ui_Viewer


def auto_reshuffled_list_generator(seq: MutableSequence) -> Any:
    """Acts as infinite generator which reshuffles the list after each complete pass.

    :param seq: The sequence (mutable) of elements to pass through.
    :type seq: MutableSequence

    :raises ValueError: if seq is empty.
    """

    if not seq:
        raise ValueError("Not allowed empty sequence.")

    while True:
        random.shuffle(seq)
        yield from seq


class Viewer(QWidget, Ui_Viewer):
    """The UI class of the note viewer."""

    def __init__(
        self,
        images_dir: Path,
        sounds_dir: Path,
        training_notes: set[NoteType] | None = None,
        image_load_timer_in_ms: int | None = None,
    ) -> None:
        super().__init__()
        self.setupUi(self)

        self.images_dir = images_dir
        self.sounds_dir = sounds_dir
        self.training_notes = training_notes
        self.image_load_timer_in_ms = image_load_timer_in_ms
        self.timer = QTimer()
        self.current_note: Note | None = None

        images_paths = [
            self.images_dir / image_name
            for image_name in os.listdir(self.images_dir)
            if not image_name.startswith("_")
        ]
        images = {NoteType(image_path.stem): image_path for image_path in images_paths}
        image_paths = [
            value
            for key, value in images.items()
            if self.training_notes is None or key in self.training_notes
        ]

        self.image_paths_generator = auto_reshuffled_list_generator(image_paths)

        self._load_next_note()

        self.setFixedSize(self.sizeHint())

        if self.image_load_timer_in_ms is not None:
            self.pushButton_next.setVisible(False)
            self.timer.start(self.image_load_timer_in_ms)
        else:
            self.pushButton_next.setVisible(True)
            self.pushButton_next.clicked.connect(self._load_next_note)

        # connections
        self.timer.timeout.connect(self._load_next_note)

    def _load_next_note(self) -> None:
        """Load/initialize the next note by loading the image and
        playing the sound of the note."""

        self.current_note = Note(
            image_path=next(self.image_paths_generator),
            sound_path=self.sounds_dir,
            image_label=self.label_image,
        )

        self.current_note.play_sound()

    def closeEvent(self, event: QEvent) -> None:
        """The overwritten close event.

        Before closing the window, the active timer need to be stopped.

        :param event: The current event.
        :type event: QEvent
        """

        if self.timer.isActive():
            self.timer.stop()

        event.accept()
