
from audio import convert_audio
from transcribers.cmu_sphinx import CMUSphinx

c = CMUSphinx()
convert_audio("audio.mp3", "audio.wav")
print(c.transcribe("audio.wav"))
