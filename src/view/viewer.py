"""The viewer module with all the logic and classes around the viewer UI."""

import os
import random
import typing
from pathlib import Path
from threading import Event, Thread
from typing import Any, MutableSequence

from PySide6.QtCore import QEvent, QTimer, QObject, Signal, Slot, QThread
from PySide6.QtWidgets import QWidget, QApplication

from src.config import SHOW_SOLUTION_TIMER_IN_MS
from src.custom_types import NoteType
from src.recorder import Recorder
from src.view.note import Note
from src.view.ui.ui_viewer import Ui_Viewer


def auto_reshuffled_list_generator(seq: MutableSequence) -> Any:
    """Acts as infinite generator which reshuffles the list after each complete pass.

    :param seq: The sequence (mutable) of elements to pass through.
    :type seq: MutableSequence

    :raises ValueError: if seq is empty.
    """

    if not seq:
        raise ValueError("Not allowed empty sequence.")

    while True:
        random.shuffle(seq)
        yield from seq


class RecorderThread(QObject, Recorder):
    note_detected_signal = Signal(str)
    stop_listening_thread = Event()

    def listen(self):
        print("Listening beginning", flush=True)

        while True:

            if RecorderThread.stop_listening_thread.is_set():
                break

            mic_input = self._stream.read(self.CHUNK)
            rms_val = self.rms(mic_input)
            if rms_val > self.THRESHOLD:
                detected_note = self.record()
                self.note_detected_signal.emit(detected_note)

        print("End listening", flush=True)


class Viewer(QWidget, Ui_Viewer):
    """The UI class of the note viewer."""

    def __init__(
        self,
        images_dir: Path,
        sounds_dir: Path,
        training_notes: set[NoteType] | None = None,
        image_load_timer_in_ms: int | None = None,
        follow_with_solution: bool = False,
        via_mic_detection: bool = False,
    ) -> None:
        super().__init__()
        self.setupUi(self)

        self.solution_frame.setVisible(False)

        self.images_dir = images_dir
        self.sounds_dir = sounds_dir
        self.training_notes = training_notes
        self.image_load_timer_in_ms = image_load_timer_in_ms
        self.timer_mode = bool(image_load_timer_in_ms)
        self.via_mic_detection = via_mic_detection

        self.timer = QTimer()
        self.solution_timer = QTimer()
        self.recorder = RecorderThread()

        self.current_note: Note | None = None
        self.follow_with_solution = follow_with_solution

        images_paths = [
            self.images_dir / image_name
            for image_name in os.listdir(self.images_dir)
            if not image_name.startswith("_")
        ]
        images = {NoteType(image_path.stem): image_path for image_path in images_paths}
        image_paths = [
            value
            for key, value in images.items()
            if self.training_notes is None or key in self.training_notes
        ]

        self.image_paths_generator = auto_reshuffled_list_generator(image_paths)

        self._load_next_note()

        self.setFixedSize(self.sizeHint())

        # connections
        self.solution_timer.timeout.connect(self._load_next_note)

        if self.timer_mode:
            self.pushButton_next.setVisible(False)

            if self.follow_with_solution:
                self.timer.timeout.connect(self._show_solution)
            else:
                self.timer.timeout.connect(self._load_next_note)

            self.timer.start(self.image_load_timer_in_ms)
        elif self.via_mic_detection:
            self.pushButton_next.setVisible(False)

            # start the new listen thread
            self.recorder.note_detected_signal.connect(self.on_note_detection)
            RecorderThread.stop_listening_thread.clear()
            listen_thread = Thread(daemon=True, target=self.recorder.listen)
            listen_thread.start()
        else:
            self.pushButton_next.setVisible(True)

            if self.follow_with_solution:
                self.pushButton_next.clicked.connect(self._show_solution)
            else:
                self.pushButton_next.clicked.connect(self._load_next_note)

    @Slot(str)
    def on_note_detection(self, note):
        print("Detected Note:", note, flush=True)
        note_type = self._map_keynote_to_note_type(note)
        print("Mapped Note:", note_type, flush=True)
        print("Current Note:", self.current_note.note_type, flush=True)

        # current note detection is not good enough,
        # just check if base note is matching
        current_base_note = self.current_note.note_type.value.replace("'", "")[0]
        detected_base_note = note_type.value.replace("'", "")[0]
        is_matching = current_base_note == detected_base_note

        if is_matching:
            self.setStyleSheet("QWidget{background-color: green;}")
        else:
            self.setStyleSheet("QWidget{background-color: red;}")

        self._ui_update_result()

        if self.follow_with_solution:
            self._show_solution()
        else:
            self._load_next_note()

    def _ui_update_result(self):
        self.update()
        QApplication.processEvents()
        QThread.sleep(2)

    def _map_keynote_to_note_type(self, keynote: str) -> NoteType:
        try:
            note, level = keynote[0], keynote[1]
            is_semitone = len(keynote) > 2

            level = int(level)

            clean_note_name = note = note.lower()

            if level < 3:
                note = f"'{note}"

            note = note.replace("b", "h")

            if is_semitone:
                if keynote[2] == "#":
                    note = note.replace(clean_note_name, f"{clean_note_name}is")
                else:
                    note = note.replace(clean_note_name, f"{clean_note_name}es")
                    note = note.replace("ee", "e")

            mapped_level = "'" * (level - 4)
            note_name = f"{note}{''.join(mapped_level)}"
            print(">>>>", note_name, flush=True)
            return NoteType(note_name)
        except:
            return NoteType.UNKNOWN


    def _load_next_note(self) -> None:
        """Load/initialize the next note by loading the image and
        playing the sound of the note."""

        self.setStyleSheet("QWidget{background-color: white;}")

        if self.solution_timer.isActive():
            self.solution_timer.stop()

        self.current_note = Note(
            image_path=next(self.image_paths_generator),
            sound_path=self.sounds_dir,
            image_label=self.label_image,
        )

        self.current_note.play_sound()

        self.label_image.setVisible(True)
        self.solution_frame.setVisible(False)

        if self.timer_mode:
            self.timer.start(self.image_load_timer_in_ms)
        elif self.via_mic_detection:
            self.pushButton_next.setVisible(False)
        else:
            self.pushButton_next.setVisible(True)

    def _show_solution(self) -> None:
        """Load/initialize the solution of last note view."""

        self.setStyleSheet("QWidget{background-color: white;}")

        if self.timer_mode and self.timer.isActive():
            self.timer.stop()

        if self.current_note is not None:
            self.label_note.setText(self.current_note.name)

        self.label_image.setVisible(False)
        self.solution_frame.setVisible(True)

        self.pushButton_next.setVisible(False)

        self.solution_timer.start(SHOW_SOLUTION_TIMER_IN_MS)

    def closeEvent(self, event: QEvent) -> None:
        """The overwritten close event.

        Before closing the window, all active timer need to be stopped.

        :param event: The current event.
        :type event: QEvent
        """

        if self.timer.isActive():
            self.timer.stop()

        if self.solution_timer.isActive():
            self.solution_timer.stop()

        self.recorder.stop_listening_thread.set()
        self.recorder.close()

        event.accept()
