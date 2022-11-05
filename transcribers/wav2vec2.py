from huggingsound import SpeechRecognitionModel
from transcribers.transcriber import Transcriber


class Wav2Vec2(Transcriber):
    """
    Credit: https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-english
    """

    def __init__(self):
        self.model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-english")

    def transcribe(self, path: str) -> str:
        result = self.model.transcribe([path])
        return result[0]["transcription"]
