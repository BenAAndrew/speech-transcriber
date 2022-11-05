import os
from transcribers.cmu_sphinx import CMUSphinx
from transcribers.silero import Silero

AUDIO = os.path.join("tests", "audio.wav")


def test_cmu_sphinx():
    cmu = CMUSphinx()
    assert cmu.transcribe(AUDIO) == "this recording is from the british council"


def test_silero():
    silero = Silero()
    assert silero.transcribe(AUDIO) == "this recording is from the british countsil"
