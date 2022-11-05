import os

from audio import convert_audio
from transcribers.cmu_sphinx import CMUSphinx
from transcribers.silero import Silero
from transcribers.vosk import Vosk
from transcribers.wav2vec2 import Wav2Vec2
from transcribers.whisper import Whisper

c = CMUSphinx()
convert_audio("audio.mp3", "audio.wav")

print(c.transcribe("audio.wav"))

s = Silero()
print(s.transcribe("audio.wav"))

whisper = Whisper()
print(whisper.transcribe("audio.wav"))

wav2vec2 = Wav2Vec2()
print(wav2vec2.transcribe("audio.wav"))

vosk = Vosk()
print(vosk.transcribe("audio.wav"))

os.remove("audio.wav")