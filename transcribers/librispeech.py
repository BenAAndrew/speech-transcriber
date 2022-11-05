import torch
from transformers import Speech2TextProcessor, Speech2TextForConditionalGeneration
import librosa
from transcribers.transcriber import Transcriber


class Librispeech(Transcriber):
    """
    Credit: https://huggingface.co/facebook/s2t-small-librispeech-asr
    """

    def __init__(self):
        self.model = Speech2TextForConditionalGeneration.from_pretrained("facebook/s2t-small-librispeech-asr")
        self.processor = Speech2TextProcessor.from_pretrained("facebook/s2t-small-librispeech-asr")

    def transcribe(self, path: str) -> str:
        try:
            wav, _ = librosa.load(path)
        except Exception:
            raise Exception(f"Cannot load audio file {path}")

        data = torch.tensor([wav])
        input_features = self.processor(
            data[0],
            sampling_rate=16000,
            return_tensors="pt"
        ).input_features 
        generated_ids = self.model.generate(input_features)
        transcription = self.processor.batch_decode(generated_ids)
        return transcription[0]
