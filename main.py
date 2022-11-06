import argparse
import uuid
import os
from punctuator import Punctuator

from audio import convert_audio
from select_transcriber import select_transcriber, Transcriber


def transcribe_file(file_path: str, transcriber_name: str, punctuator_path: str = None):
    assert os.path.isfile(file_path), f"{file_path} file does not exist"
    converted_path = f"{uuid.uuid4()}.wav"
    convert_audio(file_path, converted_path)
    transcriber = select_transcriber(transcriber_name)
    transcription = transcriber.transcribe(converted_path)
    if punctuator_path:
        punctuator = Punctuator(punctuator_path)
        transcription = punctuator.punctuate(transcription)
    print(transcription)
    os.remove(converted_path)


def main():
    parser = argparse.ArgumentParser(description="Transcribe a given audio file")
    parser.add_argument("-f", "--file", type=str, help="Audio file path", required=True)
    parser.add_argument("-t", "--transcriber", type=str, help="Transcriber to use", choices=[t.value for t in Transcriber], required=True)
    parser.add_argument("-p", "--punctuator", type=str, help="Punctuation model to use", required=False)
    args = parser.parse_args()
    transcribe_file(args.file, args.transcriber, args.punctuator)


if __name__ == "__main__":
    main()
