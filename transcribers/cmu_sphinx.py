import speech_recognition as sr

from transcribers.transcriber import Transcriber


class CMUSphinx(Transcriber):
    """
    Credit: https://cmusphinx.github.io/wiki/
    """

    def __init__(self):
        self.r = sr.Recognizer()

    def transcribe(self, path: str) -> str:
        try:
            audio_file = sr.AudioFile(path)
        except Exception:
            raise Exception(f"Cannot load audio file {path}")

        with audio_file as source:
            audio = self.r.record(source)
        return self.r.recognize_sphinx(audio)
