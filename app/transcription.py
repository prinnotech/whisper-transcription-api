import whisper
import os


class TranscriptionService:
    def __init__(self):
        self.model = None
        self.model_name = "medium"

    def load_model(self):
        """Load the Whisper model"""
        if self.model is None:
            print(f"Loading Whisper {self.model_name} model...")
            self.model = whisper.load_model(self.model_name)
            print("Model loaded successfully!")

    def transcribe(self, file_path: str):
        """Transcribe audio file"""
        # Load model if not already loaded
        self.load_model()

        # Transcribe the audio
        result = self.model.transcribe(file_path)

        return {"text": result["text"].strip(), "language": result["language"]}

    def is_model_loaded(self):
        """Check if model is loaded"""
        return self.model is not None
