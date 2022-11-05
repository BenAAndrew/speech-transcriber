from vosk import Model, KaldiRecognizer, SetLogLevel
import wave
import json

from transcribers.transcriber import Transcriber


class Vosk(Transcriber):
    """
    Credit: https://alphacephei.com/vosk/
    """

    def __init__(self):
       self.model = Model(lang="en-us")

    def transcribe(self, path: str) -> str:
        wf = wave.open(path, "rb")
        assert wf.getnchannels() == 1 and wf.getsampwidth() == 2 and wf.getcomptype() == "NONE", "Audio file must be WAV format mono PCM."

        rec = KaldiRecognizer(self.model, wf.getframerate())
        rec.SetWords(True)
        rec.SetPartialWords(True)

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                rec.Result()
            else:
                rec.PartialResult()

        return json.loads(rec.FinalResult())["text"]
