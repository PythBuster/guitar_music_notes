import concurrent
import os
import random
import threading
from collections import defaultdict
from pathlib import Path

from PySide6.QtCore import QTimer, QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QSoundEffect
from PySide6.QtWidgets import (QHBoxLayout, QPushButton, QSizePolicy,
                               QSpacerItem, QVBoxLayout, QWidget)
from playsound import playsound

from src.custom_types import NoteType
from src.view.note import Note, map_note_type


class Viewer(QWidget):
    def __init__(
        self,
        images_dir: Path,
        sounds_dir: Path,
        training_notes: set[NoteType] | None = None,
        image_load_timer_in_ms: int | None = None,
    ):
        self.images_dir = images_dir
        self.sounds_dir = sounds_dir
        self.training_notes = training_notes
        self.image_load_timer_in_ms = image_load_timer_in_ms

        super().__init__()
        self.setWindowTitle("Training")

        self.root_layout = vbox = QVBoxLayout()
        self.setLayout(vbox)

        if self.image_load_timer_in_ms is not None:
            self.timer = QTimer()
            self.timer.timeout.connect(self.load_image)
            self.timer.start(image_load_timer_in_ms)
        else:
            self.next_button = QPushButton()
            self.next_button.setText("Next")
            self.next_button.clicked.connect(self.load_image)

            hbox = QHBoxLayout()
            spacer = QSpacerItem(0, 0)
            spacer.changeSize(5, 5, QSizePolicy.Expanding, QSizePolicy.Expanding)

            hbox.addItem(spacer)
            hbox.addWidget(self.next_button)
            vbox.addLayout(hbox)

        self.current_note = None

        images_paths = [
            Path(image_name)
            for image_name in os.listdir(self.images_dir)
            if not image_name.startswith("_")
        ]
        images = {map_note_type(image_path): image_path for image_path in images_paths}
        self.image_paths = [
            self.images_dir / value
            for key, value in images.items()
            if self.training_notes is None or key in self.training_notes
        ]

        self._reorder_image_paths()

        self.load_image()

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
        next_note = Note(self.next_image())

        if self.current_note is None:
            self.current_note = next_note
            self.root_layout.addWidget(self.current_note)
        else:
            self.root_layout.removeWidget(self.current_note)
            self.current_note = next_note
            self.root_layout.addWidget(self.current_note)

        self.update()
        self.play_sound(next_note.orig_filename)

    def play_sound(self, file_name: str):
        sound_path = self.sounds_dir / f"{file_name}.mp3"

        try:
            threading.Thread(target=playsound, args=(sound_path,), daemon=True).start()
        except Exception as ex:
            print("Sound not found:", sound_path, flush=True)
        else:
            print("Play Sound:", sound_path, flush=True)

    def closeEvent(self, event):
        event.accept()
