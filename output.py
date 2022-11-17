import json
from typing import List
from audio import Clip
from datetime import datetime, timedelta


def to_text_file(clips: List[Clip], path: str):
    with open(path, "w") as f:
        for clip in clips:
            f.write(clip.text + "\n")


def to_json_file(clips: List[Clip], path: str):
    data = [clip.to_dict() for clip in clips]
    with open(path, "w") as f:
        json.dump(data, f)


def to_srt_file(clips: List[Clip], path: str):
    def get_timestamp(milliseconds: int):
        start = datetime(1970, 1, 1) + timedelta(milliseconds=milliseconds)
        return start.strftime("%H:%M:%S,%f")[:-3]

    with open(path, "w") as f:
        for i, clip in enumerate(clips):
            start_timestamp = get_timestamp(clip.start)
            end_timestamp = get_timestamp(clip.end)
            f.write(f"{i+1}\n")
            f.write(f"{start_timestamp} --> {end_timestamp}\n")
            f.write(f"{clip.text}\n")
            if i != len(clips) - 1:
                f.write("\n")
