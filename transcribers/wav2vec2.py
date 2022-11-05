from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import torch
import librosa
from transcribers.transcriber import Transcriber


class Wav2Vec2(Transcriber):
    """
    Credit: https://huggingface.co/facebook/wav2vec2-base-960h
    """

    def __init__(self):
       self.processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
       self.model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

    def transcribe(self, path: str) -> str:
        try:
            wav, _ = librosa.load(path)
        except Exception:
            raise Exception(f"Cannot load audio file {path}")

        data = torch.tensor([wav])
        input_values = self.processor(data[0], return_tensors="pt", padding="longest").input_values
        logits = self.model(input_values).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = self.processor.batch_decode(predicted_ids)
        return transcription[0]
