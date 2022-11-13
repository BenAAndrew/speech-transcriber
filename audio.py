import os
from subprocess import check_output
from pathlib import Path
from typing import List
from pydub import AudioSegment
from pydub.silence import detect_nonsilent

TARGET_BITRATE = "128"
MIN_SILENCE_LENGTH = 700
SILENCE_THRESHOLD = -32
SILENCE_TO_KEEP = 100


def convert_audio(input_path: str, output_path: str):
    check_output(
        [
            "ffmpeg",
            "-i",
            input_path,
            "-ac",
            "1",
            "-ab",
            TARGET_BITRATE,
            "-acodec",
            "pcm_s16le",
            output_path,
        ]
    )


class Clip:
    path: str
    start: int
    end: int
    text: str

    def __init__(self, path, start, end):
        self.path = path
        self.start = start
        self.end = end

    def set_text(self, text):
        self.text = text

    def to_dict(self):
        return {
            "text": self.text,
            "start": self.start,
            "end": self.end
        }


def generate_clips(file_path: str, output_folder: str, max_clip_length: int=30000):
    """
    Divides a given audio file into a set of clips (split on silence)

    Attributes
    ----------
    file_path : str
        Path to wav file
    output_folder : str
        Folder to export clips to
    max_clip_length : int
        Target max clip length (ms)

    Returns
    -------
    list
        List of Clips (containing path, start & end)
    """
    filename = Path(file_path).stem
    sound_file = AudioSegment.from_wav(file_path)

    if len(sound_file) <= max_clip_length:
        return [Clip(file_path, 0, len(sound_file))]

    clip_ranges = split_silence(sound_file)
    combined_clip_ranges = combine_clips(clip_ranges, max_clip_length)
    clips = []
    for i, (start, end) in enumerate(combined_clip_ranges):
        audio = sound_file[start:end]
        path = os.path.join(output_folder, f"chunk-{filename}-{i}.wav")
        audio.export(path, format="wav")
        clip = Clip(path, start, end)
        clips.append(clip)

    return clips


def combine_clips(clip_ranges: List[List[int]], max_clip_length: int):
    for i in range(1, len(clip_ranges)):
        start = clip_ranges[i-1][0]
        end = clip_ranges[i][1]
        duration = end - start
        if duration <= max_clip_length:
            clip_ranges[i-1] = [start, end]
            del clip_ranges[i]
            return combine_clips(clip_ranges, max_clip_length)

    return clip_ranges


def split_silence(sound_file: AudioSegment):
    return [
        [max(0, start - SILENCE_TO_KEEP), min(len(sound_file), end + SILENCE_TO_KEEP)]
        for (start, end) in detect_nonsilent(
            sound_file, min_silence_len=MIN_SILENCE_LENGTH, silence_thresh=SILENCE_THRESHOLD
        )
    ]
