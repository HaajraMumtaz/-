# src/speech_to_text.py

import queue
import sounddevice as sd
import vosk
import json
import os

# Path to Vosk model (adjust if folder name is different)
MODEL_PATH = os.path.join("models", "vosk-model-small-en-us-0.15")

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("Vosk model not found! Put it inside models/ folder.")

# Load model
model = vosk.Model(MODEL_PATH)

# Setup audio queue
q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

# Speech recognition function
def listen_and_transcribe():
    rec = vosk.KaldiRecognizer(model, 16000)
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype="int16",
                           channels=1, callback=callback):
        print("🎤 Listening... Press Ctrl+C to stop.")
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "").strip()
                if text:
                    print("➡️", text)
            else:
                # partial recognition
                pass
