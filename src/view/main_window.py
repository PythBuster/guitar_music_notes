from typing import Any

from PySide6.QtCore import QSettings, QByteArray
from PySide6.QtWidgets import QCheckBox, QMainWindow, QMessageBox

from src.config import IMAGES_PATH, SOUNDS_DIR
from src.custom_types import NoteType
from src.view.ui.ui_main_window import Ui_MainWindow
from src.view.viewer import Viewer


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app_data: dict[str, Any]):
        self.app_data = app_data

        super().__init__()
        self.setupUi(self)

        self.setWindowTitle(f"{app_data['name']} v{app_data['version']}")

        self.viewer = None
        self.setFixedSize(self.sizeHint())

        # connections
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

    def about_app(self):
        about = QMessageBox(self)
        about.setWindowTitle("About")
        about.setText("Guitar Music Notes")
        about.exec()

    def start_training(self):
        kwargs = {
            "images_dir": IMAGES_PATH,
            "sounds_dir": SOUNDS_DIR,
        }

        if self.radioButton_timer.isChecked():
            kwargs["image_load_timer_in_ms"] = (
                int(self.lineEdit_timer_seconds.text()) * 1000
            )

        training_notes = self.collect_selected_notes()

        if training_notes:
            kwargs["training_notes"] = training_notes

        self.viewer = Viewer(**kwargs)
        self.viewer.show()

    def collect_selected_notes(self) -> set[NoteType]:
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
        settings = QSettings(self.app_data['name'])

        settings.beginGroup("MainWindow")

        settings.setValue("geometry", self.saveGeometry())

        radioButton_timer_is_checked = self.radioButton_timer.isChecked()
        settings.setValue("radioButton_timer", radioButton_timer_is_checked)
        settings.setValue("lineEdit_timer_seconds", self.lineEdit_timer_seconds.text())

        selected_note_types = self.collect_selected_notes()
        settings.setValue("selected_note_types", selected_note_types)

        settings.endGroup()

    def read_settings(self) -> None:
        settings = QSettings(self.app_data['name'])

        settings.beginGroup("MainWindow")

        geometry = settings.value("geometry", QByteArray())

        if not geometry.isEmpty():
            self.restoreGeometry(geometry)

        radioButton_timer_is_checked = settings.value("radioButton_timer", False, type=bool)
        self.radioButton_timer.setChecked(radioButton_timer_is_checked)
        self.radioButton_manually.setChecked(not radioButton_timer_is_checked)
        self.groupBox_timer_settings.setVisible(radioButton_timer_is_checked)

        lineEdit_timer_seconds = settings.value("lineEdit_timer_seconds", "4")
        self.lineEdit_timer_seconds.setText(lineEdit_timer_seconds)

        selected_note_types = settings.value("selected_note_types", set())
        self.select_notes(selected_note_types=selected_note_types)

        settings.endGroup()

    def select_notes(self, selected_note_types: set[NoteType]) -> None:
        checkboxes = [
            child
            for child in self.groupBox_select_notes.children()
            if isinstance(child, QCheckBox)
        ]

        for checkbox in checkboxes:
            checkbox.setChecked(NoteType(checkbox.objectName().replace("note_", "").replace("_", "'")) in selected_note_types)

    def closeEvent(self, event):
        self.write_settings()
        self.viewer.close()
        event.accept()