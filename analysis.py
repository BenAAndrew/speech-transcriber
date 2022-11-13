import os
from tqdm import tqdm
import time
import re
from audio import convert_audio

from transcribers.cmu_sphinx import CMUSphinx
from transcribers.librispeech import Librispeech
from transcribers.silero import Silero
from transcribers.vosk import Vosk
from transcribers.wav2vec2 import Wav2Vec2
from transcribers.wav2vec2_commonvoice import Wav2Vec2CommonVoice
from transcribers.whisper import Whisper

DATASET_PATH = "test-clean"
MODELS = {
    "cmu_spinx": CMUSphinx(),
    "librispeech": Librispeech(),
    "silero": Silero(),
    "vosk": Vosk(),
    "wav2vec2_commonvoice": Wav2Vec2CommonVoice(),
    "wav2vec2": Wav2Vec2(),
    "whisper": Whisper()
}

assert os.path.isdir(DATASET_PATH), "Missing test dataset. Download test-clean from http://www.openslr.org/12"

def extract_dataset():
    clips = {}

    for folder in os.listdir(DATASET_PATH):
        for subfolder in os.listdir(os.path.join(DATASET_PATH, folder)):
            path = os.path.join(DATASET_PATH, folder, subfolder)
            with open(os.path.join(path, f"{folder}-{subfolder}.trans.txt")) as f:
                text_file = [l for l in f.read().split('\n') if l]
                for line in text_file:
                    filename, text = line.split(' ', 1)
                    output_path = os.path.join(path, f"{filename}.wav")
                    if not os.path.isfile(output_path):
                        original_path = os.path.join(path, f"{filename}.flac")
                        convert_audio(original_path, output_path)
                    clips[output_path] = text.lower()

    return clips


def similarity(actual, predicted):
    actual_words = actual.split(" ")
    predicted_words = predicted.split(" ")
    score = sum([1 if word in actual_words else -1 for word in predicted_words])
    return score / len(actual_words)


print("Loading dataset...")
clips = extract_dataset()
scores = {name: [] for name in MODELS}
durations = {name: [] for name in MODELS}

for name, model in MODELS.items():
    print(name)
    scores = []
    durations = []
    for filepath, text in tqdm(clips.items()):
        start = time.time()
        prediciton = re.sub(r'[^a-zA-Z0-9 ]', '', model.transcribe(filepath).lower())
        duration = time.time() - start
        scores.append(similarity(text, prediciton))
        durations.append(duration)
    print(name, "Score:", sum(scores)/len(scores), "Avg duration (single):", sum(durations)/len(durations))
