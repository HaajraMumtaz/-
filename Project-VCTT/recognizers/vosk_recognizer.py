import json
from vosk import Model, KaldiRecognizer
import wave

# Load model once (we'll pick the small model first)
model = Model("models/vosk-model-small-en-us-0.15")

def recognize_with_vosk(audio_file):
    wf = wave.open(audio_file, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())

    text = ""
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            text += " " + result.get("text", "")
    return text.strip()
