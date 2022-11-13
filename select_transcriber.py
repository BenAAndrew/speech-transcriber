from enum import Enum

from transcribers.cmu_sphinx import CMUSphinx
from transcribers.librispeech import Librispeech
from transcribers.silero import Silero
from transcribers.vosk import Vosk
from transcribers.wav2vec2 import Wav2Vec2
from transcribers.wav2vec2_commonvoice import Wav2Vec2CommonVoice
from transcribers.whisper import Whisper


class Transcriber(Enum):
    CMU_SPHINX = "cmu_sphinx"
    LIBRISPEECH = "librispeech"
    SILERO = "silero"
    VOSK = "vosk"
    WAV2VEC2 = "wav2vec2"
    WAV2VEC2_COMMONVOICE = "wav2vec2_commonvoice"
    WHISPER = "whisper"


def select_transcriber(name: str):
    if name == Transcriber.CMU_SPHINX.value:
        return CMUSphinx()
    elif name == Transcriber.LIBRISPEECH.value:
        return Librispeech()
    elif name == Transcriber.SILERO.value:
        return Silero()
    elif name == Transcriber.VOSK.value:
        return Vosk()
    elif name == Transcriber.WAV2VEC2.value:
        return Wav2Vec2()
    elif name == Transcriber.WAV2VEC2_COMMONVOICE.value:
        return Wav2Vec2CommonVoice()
    elif name == Transcriber.WHISPER.value:
        return Whisper()
    else:
        raise Exception(f"Unsupported transcriber '{name}'")
