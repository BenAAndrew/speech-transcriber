import argparse
import uuid
import os

from audio import convert_audio
from select_transcriber import select_transcriber, Transcriber


def transcribe_file(path: str, transcriber_name: str):
    assert os.path.isfile(path), f"{path} file does not exist"
    converted_path = f"{uuid.uuid4()}.wav"
    convert_audio(path, converted_path)
    transcriber = select_transcriber(transcriber_name)
    print(transcriber.transcribe(converted_path))
    os.remove(converted_path)


def main():
    parser = argparse.ArgumentParser(description="Transcribe a given audio file")
    parser.add_argument("-p", "--path", type=str, help="Audio file path", required=True)
    parser.add_argument("-t", "--transcriber", type=str, help="Transcriber to use", choices=[t.value for t in Transcriber], required=True)
    args = parser.parse_args()
    transcribe_file(args.path, args.transcriber)


if __name__ == "__main__":
    main()
