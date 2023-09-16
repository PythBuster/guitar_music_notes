"""The viewer module with all the logic and classes around the viewer UI."""

import os
import random
from pathlib import Path
from typing import Any, MutableSequence

from PySide6.QtCore import QEvent, QTimer
from PySide6.QtWidgets import QWidget

from src.config import SHOW_SOLUTION_TIMER_IN_MS
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
        follow_with_solution: bool = False,
    ) -> None:
        super().__init__()
        self.setupUi(self)

        self.solution_frame.setVisible(False)

        self.images_dir = images_dir
        self.sounds_dir = sounds_dir
        self.training_notes = training_notes
        self.image_load_timer_in_ms = image_load_timer_in_ms
        self.timer_mode = bool(image_load_timer_in_ms)
        self.timer = QTimer()
        self.solution_timer = QTimer()

        self.current_note: Note | None = None
        self.follow_with_solution = follow_with_solution

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

        # connections
        self.solution_timer.timeout.connect(self._load_next_note)

        if self.timer_mode:
            self.pushButton_next.setVisible(False)

            if self.follow_with_solution:
                self.timer.timeout.connect(self._show_solution)
            else:
                self.timer.timeout.connect(self._load_next_note)

            self.timer.start(self.image_load_timer_in_ms)
        else:
            self.pushButton_next.setVisible(True)

            if self.follow_with_solution:
                self.pushButton_next.clicked.connect(self._show_solution)
            else:
                self.pushButton_next.clicked.connect(self._load_next_note)

    def _load_next_note(self) -> None:
        """Load/initialize the next note by loading the image and
        playing the sound of the note."""

        self.solution_timer.stop()

        self.current_note = Note(
            image_path=next(self.image_paths_generator),
            sound_path=self.sounds_dir,
            image_label=self.label_image,
        )

        self.current_note.play_sound()

        self.label_image.setVisible(True)
        self.solution_frame.setVisible(False)

        if self.timer_mode:
            self.timer.start(self.image_load_timer_in_ms)
        else:
            self.pushButton_next.setVisible(True)

    def _show_solution(self) -> None:
        """Load/initialize the solution of last note view."""

        if self.timer_mode:
            self.timer.stop()

        if self.current_note is not None:
            self.label_note.setText(self.current_note.name)

        self.label_image.setVisible(False)
        self.solution_frame.setVisible(True)
        self.pushButton_next.setVisible(False)

        self.solution_timer.start(SHOW_SOLUTION_TIMER_IN_MS)

    def closeEvent(self, event: QEvent) -> None:
        """The overwritten close event.

        Before closing the window, all active timer need to be stopped.

        :param event: The current event.
        :type event: QEvent
        """

        if self.timer.isActive():
            self.timer.stop()

        if self.solution_timer.isActive():
            self.solution_timer.stop()

        event.accept()
