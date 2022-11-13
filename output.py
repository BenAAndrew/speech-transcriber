import json
from typing import List
from audio import Clip


def to_text_file(clips: List[Clip], path: str):
    with open(path, "w") as f:
        for clip in clips:
            f.write(clip.text + "\n")


def to_json_file(clips: List[Clip], path: str):
    data = [clip.to_dict() for clip in clips]
    with open(path, "w") as f:
        json.dump(data, f)
