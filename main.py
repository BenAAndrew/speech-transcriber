from audio import convert_audio
from transcribers.cmu_sphinx import CMUSphinx
from transcribers.silero import Silero

c = CMUSphinx()
convert_audio("audio.mp3", "audio.wav")

print(c.transcribe("audio.wav"))

s = Silero()
print(s.transcribe("audio.wav"))
