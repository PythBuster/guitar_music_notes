"""The note module with all the logic and classes around the note UI widget."""

import threading
from pathlib import Path

import pygame
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QWidget

from src.custom_types import NoteType


class Note(QWidget):
    """The UI widget of the note."""

    def __init__(self, image_path: Path, sound_path: Path, image_label: QLabel) -> None:
        self.sound_path = sound_path

        super().__init__()
        self.image_label = image_label
        self.image_path = image_path
        self.note_type = NoteType(self.image_path.stem)

        self.qpixmap = QPixmap(image_path)
        self.image_label.setPixmap(self.qpixmap)

    def play_sound(self) -> None:
        """Play the sound of the related note instance (self)."""

        sound_path = self.sound_path / f"{self.image_path.stem}.mp3"

        def play():
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play(loops=0)

        try:
            threading.Thread(target=play, daemon=True).start()
        except Exception:
            print("Sound not found:", sound_path, flush=True)
        else:
            print("Play Sound:", sound_path, flush=True)
