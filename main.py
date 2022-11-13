import argparse
import uuid
import os
from punctuator import Punctuator

from audio import convert_audio, generate_clips
from select_transcriber import select_transcriber, Transcriber

CHUNKS_FOLDER = "chunks"
AUDIO_FOLDER = "audio"


def transcribe_file(file_path: str, transcriber_name: str, punctuator: Punctuator = None):
    assert os.path.isfile(file_path), f"{file_path} file does not exist"
    converted_path = os.path.join(AUDIO_FOLDER, f"{uuid.uuid4()}.wav")
    convert_audio(file_path, converted_path)
    transcriber = select_transcriber(transcriber_name)
    chunks = generate_clips(converted_path, CHUNKS_FOLDER)
    text = []
    for chunk in chunks:
        transcription = transcriber.transcribe(chunk)
        if punctuator:
            transcription = punctuator.punctuate(transcription)
        text.append(transcription)
    os.remove(converted_path)
    return text


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
    args = parser.parse_args()
    punctuator = Punctuator(args.punctuator) if args.punctuator else None
    text = transcribe_file(args.file, args.transcriber, punctuator)
    for line in text:
        print(line)


if __name__ == "__main__":
    main()
