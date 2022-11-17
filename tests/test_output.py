import os
import json
from audio import Clip
from output import to_json_file, to_srt_file, to_text_file

TEST_TEXT_FILE = "test.txt"
TEST_JSON_FILE = "test.json"
TEST_SRT_FILE = "test.srt"


def test_to_text_file():
    if os.path.isfile(TEST_TEXT_FILE):
        os.remove(TEST_TEXT_FILE)

    clips = [Clip(path="a.wav", start=0, end=14000), Clip(path="b.wav", start=17500, end=23000)]
    clips[0].set_text("Clip A")
    clips[1].set_text("Clip B")

    to_text_file(clips, TEST_TEXT_FILE)

    assert os.path.isfile(TEST_TEXT_FILE)
    with open(TEST_TEXT_FILE) as f:
        content = f.read()

    assert content == "Clip A\nClip B\n"

    os.remove(TEST_TEXT_FILE)


def test_to_json_file():
    if os.path.isfile(TEST_JSON_FILE):
        os.remove(TEST_JSON_FILE)

    clips = [Clip(path="a.wav", start=0, end=14000), Clip(path="b.wav", start=17500, end=23000)]
    clips[0].set_text("Clip A")
    clips[1].set_text("Clip B")

    to_json_file(clips, TEST_JSON_FILE)

    assert os.path.isfile(TEST_JSON_FILE)
    with open(TEST_JSON_FILE) as f:
        content = json.loads(f.read())

    assert content == [{"text": "Clip A", "start": 0, "end": 14000}, {"text": "Clip B", "start": 17500, "end": 23000}]

    os.remove(TEST_JSON_FILE)


def test_to_srt_file():
    if os.path.isfile(TEST_SRT_FILE):
        os.remove(TEST_SRT_FILE)

    clips = [Clip(path="a.wav", start=0, end=14000), Clip(path="b.wav", start=17500, end=23000)]
    clips[0].set_text("Clip A")
    clips[1].set_text("Clip B")

    to_srt_file(clips, TEST_SRT_FILE)

    assert os.path.isfile(TEST_SRT_FILE)
    with open(TEST_SRT_FILE) as f:
        content = f.read().strip()

    lines = content.split("\n\n")
    assert lines[0].split("\n") == ["1", "00:00:00,000 --> 00:00:14,000", "Clip A"]
    assert lines[1].split("\n") == ["2", "00:00:17,500 --> 00:00:23,000", "Clip B"]

    os.remove(TEST_SRT_FILE)
