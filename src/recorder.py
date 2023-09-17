import array
import wave
import time
from pathlib import Path

import pyaudio
import sounddevice

from src.config import MIC_NAME
from src.node_detector import detect_note


class Recorder:
    # pyAudio settings
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    CHUNK = 1024

    SHORT_NORMALIZE = 1.0 / 32768.0

    THRESHOLD = 15
    TIMEOUT_LENGTH = 1

    FRAME_FORMAT = "h"
    NORMALIZE = 1 / 32768

    all_sound_devices = sounddevice.query_devices()
    input_devices = list(
        filter(lambda device: MIC_NAME in device["name"], all_sound_devices)
    )

    _MIC_DEVICE_INDEX = input_devices[0]["index"]

    def __init__(self):
        self._pyAudio = pyaudio.PyAudio()

        self._stream = self._pyAudio.open(
            format=Recorder.FORMAT,
            channels=Recorder.CHANNELS,
            rate=Recorder.RATE,
            input=True,
            output=True,
            frames_per_buffer=Recorder.CHUNK,
            input_device_index=Recorder._MIC_DEVICE_INDEX,
        )

    @staticmethod
    def rms(frame):
        shorts = array.array(Recorder.FRAME_FORMAT, frame)
        sum_squares = sum((sample * Recorder.NORMALIZE) ** 2 for sample in shorts)
        return (sum_squares / len(shorts)) ** 0.5 * 1000

    def record(self) -> str:
        print("Noise detected", flush=True)
        rec = []
        current = time.time()
        end = time.time() + Recorder.TIMEOUT_LENGTH

        while current <= end:
            data = self._stream.read(Recorder.CHUNK)
            if self.rms(data) >= Recorder.THRESHOLD:
                end = time.time() + Recorder.TIMEOUT_LENGTH

            current = time.time()
            rec.append(data)

        self._recorded_seconds = (current - end) * 100

        file_path = Path(__file__).absolute().resolve().parent / "output.wav"
        self._save(recording_data=b"".join(rec), file_path=file_path)
        detected_note = detect_note(file_path)

        print(f"Delete wav file: {file_path}", flush=True)
        file_path.unlink()

        return detected_note
        # self._play(b''.join(rec))

    def _save(self, recording_data: list, file_path: Path) -> None:
        with wave.open(str(file_path), "wb") as wf:
            wf.setnchannels(Recorder.CHANNELS)
            wf.setsampwidth(self._pyAudio.get_sample_size(Recorder.FORMAT))
            wf.setframerate(Recorder.RATE)

            print(f"Write wav file: {file_path}", flush=True)

            for _ in range(0, Recorder.RATE // Recorder.CHUNK * int(self._recorded_seconds)):
                wf.writeframes(recording_data)

    def _play(self, recording):
        print("Play listened", flush=True)
        self._stream.write(recording)

    def listen(self):
        print("Listening beginning", flush=True)

        try:
            while True:
                mic_input = self._stream.read(Recorder.CHUNK)
                rms_val = self.rms(mic_input)
                if rms_val > Recorder.THRESHOLD:
                    self.record()

        except Exception as ex:
            print(ex, flush=True)

    def close(self):
        self._stream.close()
