import os
import random
from pathlib import Path

from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QPushButton, QSizePolicy,
                               QSpacerItem, QVBoxLayout, QWidget)
from src.view.note import Note


class Viewer(QWidget):
    def __init__(self, images_dir: Path, image_load_timer_in_ms: int | None = None):
        self.images_dir = images_dir
        self.image_load_timer_in_ms = image_load_timer_in_ms

        super().__init__()
        self.setWindowTitle("Training")

        self.root_layout = vbox = QVBoxLayout()
        #self.image_label = QLabel()
        #vbox.addWidget(self.image_label)
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
        self.image_names = [
            image_name
            for image_name in os.listdir(self.images_dir)
            if not image_name.startswith("_")
        ]

        self.load_image()

    def next_image(self) -> Path:
        image_file = random.choice(self.image_names)
        return self.images_dir / image_file

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

