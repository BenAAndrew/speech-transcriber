import os
from transcribers.cmu_sphinx import CMUSphinx

AUDIO = os.path.join("tests", "audio.wav")

def test_cmu_sphinx():
    cmu = CMUSphinx()
    assert cmu.transcribe(AUDIO) == "this recording is from the british council"
