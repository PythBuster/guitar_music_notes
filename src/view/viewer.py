import os
import random
from pathlib import Path

from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QPushButton, QSizePolicy,
                               QSpacerItem, QVBoxLayout, QWidget)


class Viewer(QWidget):
    def __init__(self, images_dir: Path, image_load_timer_in_ms: int | None = None):
        self.images_dir = images_dir
        self.image_load_timer_in_ms = image_load_timer_in_ms

        super().__init__()

        vbox = QVBoxLayout()
        self.image_label = QLabel()
        vbox.addWidget(self.image_label)
        self.setLayout(vbox)

        if self.image_load_timer_in_ms is not None:
            self.load_image()

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
            self.load_image()

    def next_image(self) -> Path:
        image_file = random.choice(os.listdir(self.images_dir))

        return self.images_dir / image_file

    def load_image(self):
        self.image_label.setPixmap(QPixmap(self.next_image()))
