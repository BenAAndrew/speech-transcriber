from speechbrain.pretrained import EncoderDecoderASR

from transcribers.transcriber import Transcriber


class Wav2Vec2CommonVoice(Transcriber):
    """
    Credit: https://huggingface.co/speechbrain/asr-wav2vec2-commonvoice-en
    """

    def __init__(self):
        self.model = EncoderDecoderASR.from_hparams(
            source="speechbrain/asr-wav2vec2-commonvoice-en", savedir="pretrained_models/asr-wav2vec2-commonvoice-en"
        )

    def transcribe(self, path: str) -> str:
        return self.model.transcribe_file(path)
