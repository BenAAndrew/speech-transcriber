import os
from subprocess import check_output
from pydub import AudioSegment
from pydub.silence import split_on_silence

TARGET_BITRATE = "128"


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


def split_silence(file_path: str, output_folder: str):
    sound_file = AudioSegment.from_wav(file_path)
    audio_chunks = split_on_silence(sound_file, 
	    min_silence_len=800,
	    silence_thresh=-32
	)

    files = []
    for i, chunk in enumerate(audio_chunks):
        path = os.path.join(output_folder, f"chunk-{i}.wav")
        chunk.export(path, format="wav")
        files.append(path)
    
    return files
