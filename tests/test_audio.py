import os
import shutil
from audio import combine_clips, generate_clips
from transcribers.librispeech import Librispeech

AUDIO = os.path.join("tests", "audio2.wav")
CHUNKS_FOLDER = "chunks"


def test_generate_clips():
    if os.path.isdir(CHUNKS_FOLDER):
        shutil.rmtree(CHUNKS_FOLDER)
    os.makedirs(CHUNKS_FOLDER)
    transcriber = Librispeech()
    chunks = generate_clips(AUDIO, CHUNKS_FOLDER, max_clip_length=500)
    assert chunks[0].path == os.path.join(CHUNKS_FOLDER, "chunk-audio2-0.wav")
    assert chunks[1].path == os.path.join(CHUNKS_FOLDER, "chunk-audio2-1.wav")

    transcription = [transcriber.transcribe(chunk.path) for chunk in chunks]
    assert len(transcription) == 2
    assert transcription[0] == "during long slushy country roads and speaking to damp audiences and draughty schoolrooms there after day for a fortnight"
    assert transcription[1] == "he'll have to put him in of herums at some place of worship on sunday morning and he can come to us immediately afterwards"
    shutil.rmtree(CHUNKS_FOLDER)


def test_combine_clips():
    clip_ranges = [[0, 100], [200, 300]]
    assert combine_clips(clip_ranges, 300) == [[0, 300]]
    assert combine_clips(clip_ranges, 200) == clip_ranges
