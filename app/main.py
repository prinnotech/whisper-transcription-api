from fastapi import FastAPI, File, UploadFile, HTTPException, Header
import os
import tempfile
from .transcription import TranscriptionService
from .models import TranscriptionResponse

app = FastAPI(title="Whisper Transcription API")

# Initialize transcription service
transcription_service = TranscriptionService()


@app.get("/")
async def health_check():
    """Health check"""
    return {"message": "Whisper API is running!", "status": "ok"}


@app.post("/transcribe")
async def transcribe_audio(
    audio_file: UploadFile = File(...), x_api_key: str = Header(..., alias="X-API-Key")
):
    """Upload MP3 and get transcription (requires API key)"""

    # Check API key
    required_api_key = os.getenv("API_KEY")
    if not required_api_key:
        raise HTTPException(status_code=500, detail="API key not configured on server")

    if x_api_key != required_api_key:
        raise HTTPException(status_code=401, detail="Invalid API key")

    # Check file size (100MB max)
    content = await audio_file.read()
    if len(content) > 100 * 1024 * 1024:  # 100MB
        raise HTTPException(status_code=413, detail="File too large. Max 100MB")

    # Save to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
        temp_file.write(content)
        temp_path = temp_file.name

    try:
        # Transcribe
        result = transcription_service.transcribe(temp_path)

        # Clean up
        os.unlink(temp_path)

        return {"success": True, "text": result["text"], "language": result["language"]}

    except Exception as e:
        # Clean up on error
        if os.path.exists(temp_path):
            os.unlink(temp_path)
        raise HTTPException(status_code=500, detail=f"Transcription failed: {str(e)}")
