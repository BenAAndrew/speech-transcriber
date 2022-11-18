import os
import uuid
from flask import Flask, render_template, request, send_file
from main import transcribe_file
from output import to_json_file, to_srt_file, to_text_file

app = Flask(__name__, template_folder="static")

CHUNKS_FOLDER = "chunks"
AUDIO_FOLDER = "audio"
OUTPUT_FOLDER = "output"


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def transcribe():
    id = uuid.uuid4()
    path = os.path.join(AUDIO_FOLDER, f"{id}.wav")
    request.files["file"].save(path)
    max_clip_length = int(request.values["maxClipLength"]) * 1000
    clips = transcribe_file(path, request.values["transcriber"], punctuator=None, max_clip_length=max_clip_length)

    if request.values["format"] == "text":
        file_path = os.path.join(OUTPUT_FOLDER, f"{id}.txt")
        to_text_file(clips, file_path)
    elif request.values["format"] == "json":
        file_path = os.path.join(OUTPUT_FOLDER, f"{id}.json")
        to_json_file(clips, file_path)
    elif request.values["format"] == "srt":
        file_path = os.path.join(OUTPUT_FOLDER, f"{id}.srt")
        to_srt_file(clips, file_path)
    else:
        raise Exception(f"Unsupported export format '{request.values['format']}'")

    return send_file(file_path, as_attachment=True)


if __name__ == "__main__":
    os.makedirs(CHUNKS_FOLDER, exist_ok=True)
    os.makedirs(AUDIO_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    app.run(debug=True)
