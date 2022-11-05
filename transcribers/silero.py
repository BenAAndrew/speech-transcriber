import torch
import librosa

from transcribers.transcriber import Transcriber

SILERO_LANGUAGES = {"English": "en", "German": "de", "Spanish": "es"}


class Silero(Transcriber):
    """
    Credit: https://github.com/snakers4/silero-models
    """

    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model, self.decoder, _ = torch.hub.load(
            repo_or_dir="snakers4/silero-models",
            model="silero_stt",
            language="en",
            device=self.device,
        )

    def transcribe(self, path: str) -> str:
        try:
            wav, _ = librosa.load(path)
        except Exception:
            raise Exception(f"Cannot load audio file {path}")

        data = torch.tensor([wav])
        data = data.to(self.device)
        output = self.model(data)[0]
        return self.decoder(output.cpu())
