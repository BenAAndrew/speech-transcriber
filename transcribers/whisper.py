import whisper
from transcribers.transcriber import Transcriber


class Whisper(Transcriber):
    """
    Credit: https://github.com/openai/whisper
    """

    def __init__(self):
        self.model = whisper.load_model("base")

    def transcribe(self, path: str) -> str:
        result = self.model.transcribe(path)
        return result["text"]
