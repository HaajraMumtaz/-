from .vosk_recognizer import recognize_with_vosk
from .google_recognizer import recognize_with_google

def recognize_speech(audio_file, engine="vosk"):
    if engine == "vosk":
        return recognize_with_vosk(audio_file)
    elif engine == "google":
        return recognize_with_google(audio_file)
    else:
        raise ValueError("Unknown engine: " + engine)
