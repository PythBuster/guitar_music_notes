import sys
from typing import Any

import pygame
import toml
from PySide6.QtWidgets import QApplication

from src.config import PYPROJECT_PATH
from src.view.main_window import MainWindow

pygame.mixer.init()  # initialise the pygame


def read_pyproject_toml() -> dict[str, Any]:
    return toml.load(PYPROJECT_PATH.open())


pyproject_data = read_pyproject_toml()

app = QApplication(sys.argv)

main_window = MainWindow(app_data=pyproject_data["tool"]["poetry"])
main_window.show()

app.exec()
