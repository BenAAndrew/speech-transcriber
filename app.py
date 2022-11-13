import os
import uuid
from flask import Flask, render_template, request, send_file
from main import transcribe_file

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
    text = transcribe_file(path, request.values["transcriber"])
    text_file = os.path.join(OUTPUT_FOLDER, f"{id}.txt")
    with open(text_file, "w") as f:
        for line in text:
            f.write(line + "\n")
    return send_file(text_file, as_attachment=True)


if __name__ == "__main__":
    os.makedirs(CHUNKS_FOLDER, exist_ok=True)
    os.makedirs(AUDIO_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    app.run(debug=True)
