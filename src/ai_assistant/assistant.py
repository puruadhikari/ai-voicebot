import assemblyai as aai
from .audio_generator import AudioGenerator
from .response_generator import ResponseGenerator
from ..prompts import ai_response_prompt
from ..constants import voice_ai_contstnts
from openai import OpenAI
from ..utils.logging import setup_logging
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


class AiAssistant:
    def __init__(self):
        self.logger = setup_logging()
        aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")
        self.openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")
        self.transcriber = None
        self.full_transcript = [
            {"role": "system", "content": ai_response_prompt.SYSTEM_PROMPT},
        ]
        self.audio_generator = AudioGenerator()
        self.response_generator = ResponseGenerator()

    def start_transcription(self):
        # Initialize and start real-time transcription
        try:
            self.transcriber = aai.RealtimeTranscriber(
                sample_rate=voice_ai_contstnts.SAMPLE_RATE,
                on_data=self.on_data,
                on_error=self.on_error,
                on_open=self.on_open,
                on_close=self.on_close,
                end_utterance_silence_threshold=voice_ai_contstnts.UTTERANCE_SILENCE_THRESHOLD
            )
            self.transcriber.connect()
            microphone_stream = aai.extras.MicrophoneStream(sample_rate=voice_ai_contstnts.SAMPLE_RATE)
            self.transcriber.stream(microphone_stream)
        except Exception as e:
            self.logger.error("Failed to start transcription: %s", str(e))

    def stop_transcription(self):
        # Stop the transcription process
        if self.transcriber:
            self.transcriber.close()
            self.transcriber = None

    def on_open(self, session_opened: aai.RealtimeSessionOpened):
        # Callback when the transcription session is opened
        #self.logger.info("Session ID: %s", session_opened.session_id)
        return

    def on_data(self, transcript: aai.RealtimeTranscript):
        # Callback when transcription data is received
        if not transcript.text:
            return

        if isinstance(transcript, aai.RealtimeFinalTranscript):
            self.generate_ai_response(transcript)
        else:
            self.logger.info("Transcription (interim):%s", transcript.text)

    def on_error(self, error: aai.RealtimeError):
        # Callback when an error occurs during transcription
        return

    def on_close(self):
        # Callback when the transcription session is closed
        self.logger.info("Transcription session closed.\n")
        return

    def generate_ai_response(self, transcript):
        # Generate an AI response based on the user's input
        self.stop_transcription()
        self.full_transcript.append({"role": "user", "content": transcript.text})
        self.logger.info("\nCustomer: %s", transcript.text)

        try:
            ai_response = self.response_generator.generate_response(self.full_transcript)
            #self.audio_generator.generate_audio(ai_response)
            self.start_transcription()
            self.logger.info("Real-time transcription restarted.")
        except Exception as e:
            self.logger.error("Failed to generate AI response: %s", str(e))
