import sys

import pygame
from PySide6.QtWidgets import QApplication

from src.config import IMAGES_PATH, LOAD_IMAGE_TIMER_IN_MS, SOUNDS_DIR
from src.view.viewer import Viewer

pygame.mixer.init()  # initialise the pygame


app = QApplication(sys.argv)

viewer = Viewer(
    images_dir=IMAGES_PATH,
    sounds_dir=SOUNDS_DIR,
    image_load_timer_in_ms=LOAD_IMAGE_TIMER_IN_MS,
    # training_notes={
    #    NoteType.E,
    #    NoteType.G,
    #    NoteType.A,
    #    NoteType.H,
    #    NoteType.c,
    #    NoteType.d,
    #    NoteType.e,
    #    NoteType.g,
    #    NoteType.a,
    #    NoteType.h,
    #    NoteType.c_,
    #    NoteType.e_,
    #    NoteType.f_,
    # },
)

viewer.show()

app.exec()
