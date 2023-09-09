import threading
from pathlib import Path

import pygame
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from src.custom_types import NoteType


def map_note_type(image_path: Path) -> NoteType:
    image_name = image_path.name.split(".")[0]

    if image_name.startswith("'"):  # ''f
        image_name = image_name[::-2].upper()

    return NoteType(image_name)


class Note(QWidget):
    def __init__(self, image_path: Path, sound_path: Path):
        self.sound_path = sound_path

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

    def play_sound(self):
        sound_path = self.sound_path / f"{self.orig_filename}.mp3"

        def play():
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play(loops=0)

        try:
            threading.Thread(target=play, daemon=True).start()
        except Exception as ex:
            print("Sound not found:", sound_path, flush=True)
        else:
            print("Play Sound:", sound_path, flush=True)

    @property
    def name(self) -> str:
        return str(self.note_type)
