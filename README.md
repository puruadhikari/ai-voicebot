# ai-voicebot
# AI-Powered Dental Assistant

## Overview
This project is an AI-powered real-time voice assistant for a dental clinic. It integrates AssemblyAI, ElevenLabs, and OpenAI to provide a conversational assistant that transcribes incoming speech, generates intelligent responses, and returns a human-like audio response.

### Key Features
- **Real-time Transcription**: Uses AssemblyAI to transcribe speech in real time.
- **AI Response Generation**: Uses OpenAI's GPT-3.5-turbo model to generate context-aware responses.
- **Text-to-Speech**: Uses ElevenLabs to convert generated responses into human-like speech.

### Folder Structure
- **src/**: Contains the main application code.
  - **ai_assistant/**: Contains modules for different functionalities (transcription, response generation, audio generation).
  - **utils/**: Utility functions, logging, and configuration management.
  - **api/**: Placeholder for REST API logic.
  - **app.py**: Entry point of the application.
- **config/**: Configuration files.
- **logs/**: Log files.
- **tests/**: Unit and integration tests.

### Installation
1. Clone the repository.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Create a `.env` file with the following variables:
   ```
   ASSEMBLYAI_API_KEY=your_assemblyai_api_key
   OPENAI_API_KEY=your_openai_api_key
   ELEVENLABS_API_KEY=your_elevenlabs_api_key
   ```

### Usage
To start the assistant:
```sh
python src/app.py
```

### Requirements
- Python 3.9 or higher
- Dependencies listed in `requirements.txt`

### Docker
To run the application in a Docker container:
1. Build the image:
   ```sh
   docker build -t ai_dental_assistant .
   ```
2. Run the container:
   ```sh
   docker run -p 8000:8000 ai_dental_assistant
   ```

### Logging
Logs are stored in `logs/app.log` to monitor the application's activity and errors.

### License
MIT License.