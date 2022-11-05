import speech_recognition as sr
from transcribers.transcriber import Transcriber

class CMUSphinx(Transcriber):
    def __init__(self):
        self.r = sr.Recognizer()

    def transcribe(self, path: str) -> str:
        audio_file = sr.AudioFile(path)
        with audio_file as source:
            audio = self.r.record(source)
        return self.r.recognize_sphinx(audio)
