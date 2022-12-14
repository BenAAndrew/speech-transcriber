# Speech Transcriber
A web-app/library for transcribing speech

## Installation
1. Install Python 3.9
2. Install ffmpeg
    - Windows: [Download zip](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip) & add `ffmpeg/bin` to environment path
    - Linux: `apt-get install ffmpeg`
3. `pip install -r requirements.txt`
4. (Optional) [Download punctuator model](https://drive.google.com/file/d/0B7BsN5f2F1fZZ2ZXd3R0dEh6NDA/view?usp=share_link&resourcekey=0-S3cjcY9TTBHI2poYfEXmWA) and save as `INTERSPEECH-T-BRNN.pcl` 

## Usages

### Web app
Run `pip install flask` before running the web app.

Then run `python app.py` to open the web app at http://localhost:5000/

### CLI
`python main.py --path filename --transcriber transcriber`
- Path: Path to the audio/video file to transcribe
- Transcriber: Transcription model to use, choose from:
    - cmu_sphinx
    - librispeech
    - silero
    - vosk
    - wav2vec2
    - wav2vec2_commonvoice
    - whisper

## Transcription models
When selecting transcription models, the following requirements were used:
1. Must be supported in Python 3.9
2. Must work locally (without the usage of an API)
3. Must have a straightforward installation process
    - Should not require building from source
    - Should not require additional OS libraries
    - Should not require manually downloading additional files 

Below is a comparison of transcription model performance produced using the [Librispeech test clean dataset](http://www.openslr.org/12) and [analysis script](analysis.py)

| Name | Dependencies | Model Size | Average processing time | Score
|-|-|-|-|-|
| [Wav2Vec2 CommonVoice](https://huggingface.co/speechbrain/asr-wav2vec2-commonvoice-en) | speechbrain | 1.18GB | 3.351s | 0.87
| [Librispeech](https://huggingface.co/facebook/s2t-small-librispeech-asr) | torch, transformers, torchaudio, librosa | 113MB | 0.558s | 0.85
| [Wav2Vec2](https://huggingface.co/facebook/wav2vec2-base-960h) | torch, transformers, torchaudio, librosa | 360MB | 1.325s | 0.8
| [Whisper](https://github.com/openai/whisper) | whisper | 138MB | 3.848s | 0.77
| [Vosk](https://alphacephei.com/vosk/) | vosk | 67.7MB | 1.206s | 0.76
| [Silero](https://github.com/snakers4/silero-models) | torch, transformers, torchaudio, librosa, omegaconf | 111MB | 0.261s | 0.68 |
| [CMU Sphinx](https://cmusphinx.github.io/wiki/) | SpeechRecognition, pocketsphinx | 33.9MB* | 1.123s | 0.55

*size of pocketsphinx package
