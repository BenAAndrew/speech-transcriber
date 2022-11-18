import argparse
import uuid
import os
from punctuator import Punctuator

from audio import convert_audio, generate_clips
from select_transcriber import select_transcriber, Transcriber

CHUNKS_FOLDER = "chunks"
AUDIO_FOLDER = "audio"


def transcribe_file(file_path: str, transcriber_name: str, punctuator: Punctuator = None, max_clip_length: int = 30000):
    assert os.path.isfile(file_path), f"{file_path} file does not exist"
    converted_path = os.path.join(AUDIO_FOLDER, f"{uuid.uuid4()}.wav")
    convert_audio(file_path, converted_path)
    transcriber = select_transcriber(transcriber_name)
    clips = generate_clips(converted_path, CHUNKS_FOLDER, max_clip_length)
    for clip in clips:
        transcription = transcriber.transcribe(clip.path)
        if punctuator:
            transcription = punctuator.punctuate(transcription)
        clip.set_text(transcription)
    os.remove(converted_path)
    return clips


def main():
    os.makedirs(CHUNKS_FOLDER, exist_ok=True)
    os.makedirs(AUDIO_FOLDER, exist_ok=True)
    parser = argparse.ArgumentParser(description="Transcribe a given audio file")
    parser.add_argument("-f", "--file", type=str, help="Audio file path", required=True)
    parser.add_argument(
        "-t",
        "--transcriber",
        type=str,
        help="Transcriber to use",
        choices=[t.value for t in Transcriber],
        required=True,
    )
    parser.add_argument("-p", "--punctuator", type=str, help="Punctuation model to use", required=False)
    parser.add_argument("-m", "--max-clip-length", type=int, help="Max clip length when to split (seconds)", required=False)
    args = parser.parse_args()
    punctuator = Punctuator(args.punctuator) if args.punctuator else None
    max_clip_length = args.max_clip_length * 1000 if args.max_clip_length else 30000
    clips = transcribe_file(args.file, args.transcriber, punctuator, max_clip_length)
    for clip in clips:
        print(clip.text)


if __name__ == "__main__":
    main()
