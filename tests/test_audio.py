import os
import shutil
from audio import split_silence
from transcribers.librispeech import Librispeech

AUDIO = os.path.join("tests", "audio2.wav")
CHUNKS_FOLDER = "chunks"


def test_split_silence():
    if os.path.isdir(CHUNKS_FOLDER):
        shutil.rmtree(CHUNKS_FOLDER)
    os.makedirs(CHUNKS_FOLDER)
    transcriber = Librispeech()
    chunks = split_silence(AUDIO, CHUNKS_FOLDER)
    transcription = [transcriber.transcribe(chunk) for chunk in chunks]
    assert transcription == [
        "during long slushy country roads and speaking to damp audiences and draughty schoolrooms there after day for a fortnight",
        "he'll have to put him in appearance at some place of worship on sunday morning and he can come to us immediately afterwards",
    ]
    shutil.rmtree(CHUNKS_FOLDER)
