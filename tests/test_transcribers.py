import os
from transcribers.cmu_sphinx import CMUSphinx
from transcribers.silero import Silero
from transcribers.vosk import Vosk
from transcribers.wav2vec2 import Wav2Vec2
from transcribers.whisper import Whisper

AUDIO = os.path.join("tests", "audio.wav")


def test_cmu_sphinx():
    cmu = CMUSphinx()
    assert cmu.transcribe(AUDIO) == "this recording is from the british council"


def test_silero():
    silero = Silero()
    assert silero.transcribe(AUDIO) == "this recording is from the british countsil"


def test_whisper():
    whisper = Whisper()
    assert whisper.transcribe(AUDIO).strip() == "This recording is from the British Council."


def test_wav_2_vec_2():
    wav2vec2 = Wav2Vec2()
    assert wav2vec2.transcribe(AUDIO).strip().lower() == "this recording is from the british council"


def test_vosk():
    vosk = Vosk()
    assert vosk.transcribe(AUDIO) == "this recording is from the british council"
