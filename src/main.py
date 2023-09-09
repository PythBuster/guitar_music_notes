import sys

import pygame
from PySide6.QtWidgets import QApplication

from src.config import IMAGES_PATH, LOAD_IMAGE_TIMER_IN_MS, SOUNDS_DIR
from src.custom_types import NoteType
from src.view.viewer import Viewer

pygame.mixer.init()  # initialise the pygame


app = QApplication(sys.argv)

viewer = Viewer(
    images_dir=IMAGES_PATH,
    sounds_dir=SOUNDS_DIR,
    # image_load_timer_in_ms=LOAD_IMAGE_TIMER_IN_MS,
    training_notes={
        NoteType.NOTE_E,
        NoteType.NOTE_G,
        NoteType.NOTE_A,
        NoteType.NOTE_H,
        NoteType.NOTE_c,
        NoteType.NOTE_d,
        NoteType.NOTE_e,
        NoteType.NOTE_g,
        NoteType.NOTE_a,
        NoteType.NOTE_h,
        NoteType.NOTE_c_,
        NoteType.NOTE_e_,
        NoteType.NOTE_f_,
    },
)

viewer.show()

app.exec()
