"""The main module and startpoint of the guitar music notes app"""

import sys
from typing import Any

import pygame
import toml
from PySide6.QtWidgets import QApplication

from src.config import PYPROJECT_PATH
from src.view.main_window import MainWindow


def read_poetry_data_from_pyproject_toml() -> dict[str, Any]:
    """Read the poetry app data from pyproject.toml
    and return the data from that file.

    :return: The poetry data from pyproject.toml as dict.
    :rtype:  dict[str, Any]
    """

    return toml.load(PYPROJECT_PATH.open())["tool"]["poetry"]


if __name__ == "__main__":
    pygame.mixer.init()  # initialise the pygame

    app = QApplication(sys.argv)

    app_data = read_poetry_data_from_pyproject_toml()
    main_window = MainWindow(app_data=app_data)
    main_window.show()

    app.exec()
