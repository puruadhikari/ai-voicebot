from dotenv import load_dotenv

from src.ai_assistant.assistant import AiAssistant
from src.utils.logging import setup_logging

# Load environment variables from .env file
load_dotenv()


greeting = "Thank you for calling American Express. My name is Sandy, how may I assist you?"
print("AI Agent", greeting)
ai_assistant = AiAssistant()
#ai_assistant.audio_generator.generate_audio(greeting)
ai_assistant.start_transcription()
