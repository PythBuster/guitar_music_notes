"""The main window module with all the logic and classes around the main window UI."""

from typing import Any

from PySide6.QtCore import QByteArray, QEvent, QSettings
from PySide6.QtWidgets import QCheckBox, QMainWindow, QMessageBox

from src.config import IMAGES_PATH, SOUNDS_PATH, MAX_TIMER_IN_SEC
from src.custom_types import NoteType
from src.view.ui.ui_main_window import Ui_MainWindow
from src.view.viewer import Viewer


class MainWindow(QMainWindow, Ui_MainWindow):
    """The UI class of the mai window."""

    def __init__(self, app_data: dict[str, Any]):
        self.app_data = app_data

        super().__init__()
        self.setupUi(self)

        self.setWindowTitle(f"{app_data['name']} v{app_data['version']}")

        self.viewer: Viewer | None = None
        self.setFixedSize(self.sizeHint())

        # connections
        self.lineEdit_timer_seconds.textChanged.connect(self._validate_timer_input)
        self.radioButton_timer.clicked.connect(
            lambda: self.groupBox_timer_settings.setVisible(True)
        )
        self.radioButton_manually.clicked.connect(
            lambda: self.groupBox_timer_settings.setVisible(False)
        )
        self.pushButton_start_training.clicked.connect(self.start_training)
        self.actionAbout_Qt.triggered.connect(
            lambda: QMessageBox.aboutQt(self, "About Qt")
        )
        self.actionAbout_Guitar_Music_Notes.triggered.connect(self.about_app)

        self.read_settings()

    def _validate_timer_input(self, input: str) -> None:
        digit_only_input = "".join([ch for ch in input if ch.isdigit()])

        def not_valid():
            self.lineEdit_timer_seconds.setText(digit_only_input)
            self.pushButton_start_training.setEnabled(False)

        if digit_only_input:
            int_input = int(digit_only_input)

            if not(0 < int_input <= MAX_TIMER_IN_SEC):
                not_valid()
                return

            self.lineEdit_timer_seconds.setText(str(int_input))
            self.pushButton_start_training.setEnabled(True)
        else:
            not_valid()

    def about_app(self):
        """Open a about app dialogue."""

        about = QMessageBox(self)
        about.setWindowTitle("About")
        about.setText("Guitar Music Notes")
        about.exec()

    def start_training(self) -> None:
        """Initialize the Viewer UI instance by reading some options from config.py
        and shows it."""

        kwargs: dict[str, Any] = {
            "images_dir": IMAGES_PATH,
            "sounds_dir": SOUNDS_PATH,
        }

        if self.radioButton_timer.isChecked():
            kwargs["image_load_timer_in_ms"] = (
                int(self.lineEdit_timer_seconds.text()) * 1000
            )

        training_notes = self._collect_selected_notes()

        if training_notes:
            kwargs["training_notes"] = training_notes

        kwargs["follow_with_solution"] = self.checkBox_follow_with_solution.isChecked()

        self.viewer = Viewer(**kwargs)
        self.viewer.show()

    def _collect_selected_notes(self) -> set[NoteType]:
        """Collect notes into a set of NoteTypes by checking the
        note checkboxes in the viewer UI.

        :return: Return the collected set of NoteTypes.
        :rtype: set[NoteType]
        """

        selected_checkboxes = [
            child
            for child in self.groupBox_select_notes.children()
            if isinstance(child, QCheckBox)
            if child.isChecked()
        ]

        selected_notes = {
            NoteType(checkbox.objectName().replace("note_", "").replace("_", "'"))
            for checkbox in selected_checkboxes
        }

        return selected_notes

    def write_settings(self) -> None:
        """Persist the current state in the ui (like selected notes, training modes,
        ui position etc.) in user settings."""

        settings = QSettings(self.app_data["name"])

        settings.beginGroup("MainWindow")

        settings.setValue("geometry", self.saveGeometry())

        radioButton_timer_is_checked = self.radioButton_timer.isChecked()
        settings.setValue("radioButton_timer", radioButton_timer_is_checked)
        settings.setValue("lineEdit_timer_seconds", self.lineEdit_timer_seconds.text())

        selected_note_types = self._collect_selected_notes()
        settings.setValue("selected_note_types", selected_note_types)
        settings.setValue(
            "checkBox_follow_with_solution",
            self.checkBox_follow_with_solution.isChecked(),
        )

        settings.endGroup()

    def read_settings(self) -> None:
        """Read saved user settings and load states in the ui (like selected notes,
        training modes, ui position etc.)."""

        settings = QSettings(self.app_data["name"])

        settings.beginGroup("MainWindow")

        geometry = settings.value("geometry", QByteArray())

        if not geometry.isEmpty():
            self.restoreGeometry(geometry)

        radioButton_timer_is_checked = settings.value(
            "radioButton_timer", False, type=bool
        )
        self.radioButton_timer.setChecked(radioButton_timer_is_checked)
        self.radioButton_manually.setChecked(not radioButton_timer_is_checked)
        self.groupBox_timer_settings.setVisible(radioButton_timer_is_checked)

        lineEdit_timer_seconds = settings.value("lineEdit_timer_seconds", "4")
        self.lineEdit_timer_seconds.setText(lineEdit_timer_seconds)

        selected_note_types = settings.value("selected_note_types", defaultValue=set())
        self._check_notes_in_viewer(selected_note_types=selected_note_types)

        is_checkBox_follow_with_solution_checked = settings.value(
            "checkBox_follow_with_solution", defaultValue=False, type=bool
        )
        self.checkBox_follow_with_solution.setChecked(
            is_checkBox_follow_with_solution_checked
        )

        settings.endGroup()

    def _check_notes_in_viewer(self, selected_note_types: set[NoteType]) -> None:
        checkboxes = [
            child
            for child in self.groupBox_select_notes.children()
            if isinstance(child, QCheckBox)
        ]

        for checkbox in checkboxes:
            checkbox.setChecked(
                NoteType(checkbox.objectName().replace("note_", "").replace("_", "'"))
                in selected_note_types
            )

    def closeEvent(self, event: QEvent) -> None:
        """The overwritten close event.

        Before closing the window, the active timer need to be stopped.

        :param event: The current event.
        :type event: QEvent
        """

        self.write_settings()

        if self.viewer is not None:
            self.viewer.close()

        event.accept()
