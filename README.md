# Whisper Transcription API

A FastAPI-based audio transcription service using OpenAI's Whisper medium model. Supports multiple languages including English, Italian, French, Spanish, and Dutch.

## Features

- 🎵 **Audio Transcription**: Upload MP3/WAV files and get text transcription
- 🌍 **Multi-language Support**: Auto-detects language or specify manually
- 🔒 **API Key Authentication**: Secure access with custom API key
- 🚀 **High Quality**: Uses Whisper medium model for excellent accuracy
- ☁️ **Railway Ready**: Optimized for Railway deployment

## Supported Audio Formats

- MP3
- WAV
- M4A
- WebM

**File Size Limit**: 100MB per file

## Quick Start

### 1. Local Development

```bash
# Clone the repository
git clone <your-repo-url>
cd whisper-transcription-api

# Build and run with Docker
docker build -t whisper-api .
docker run -p 8000:8000 -e API_KEY=your_secret_key whisper-api
```

### 2. Test the API

**Health Check:**

```bash
curl http://localhost:8000/
```

**Transcribe Audio:**

```bash
curl -X POST "http://localhost:8000/transcribe" \
  -H "X-API-Key: your_secret_key" \
  -F "audio_file=@your_audio.mp3"
```

**Example Response:**

```json
{
  "success": true,
  "text": "Hello, this is a sample transcription.",
  "language": "en"
}
```

## Environment Variables

Create a `.env` file or set these in your deployment:

```bash
API_KEY=your_secret_api_key_here
WHISPER_MODEL=medium
PORT=8000
```

## API Endpoints

### `GET /`

Health check endpoint

### `POST /transcribe`

Transcribe audio file to text

**Headers:**

- `X-API-Key`: Your API key (required)

**Body:**

- `audio_file`: Audio file (multipart/form-data)

**Response:**

```json
{
  "success": boolean,
  "text": "transcribed text",
  "language": "detected_language_code"
}
```

## Deploy to Railway

1. Push this repo to GitHub
2. Connect GitHub repo to Railway
3. Add environment variable: `API_KEY=your_secret_key`
4. Deploy!

Railway will automatically:

- Build using the Dockerfile
- Download the Whisper medium model
- Start the API server

## Technical Details

- **Framework**: FastAPI
- **Model**: OpenAI Whisper Medium (~3GB)
- **Languages**: Auto-detection for 99+ languages
- **Processing**: ~10-15 seconds for 1-minute audio
- **Memory Usage**: ~5GB RAM recommended

## Error Codes

- `400`: Invalid file type
- `401`: Invalid or missing API key
- `413`: File too large (>100MB)
- `500`: Transcription error

## License

MIT License
