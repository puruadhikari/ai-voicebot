from elevenlabs import generate, stream
import os


class AudioGenerator:
    def __init__(self):
        # Store the ElevenLabs API key
        self.elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")

    def generate_audio(self, text):
        # Generate audio from text using ElevenLabs
        try:
            audio_stream = generate(
                api_key=self.elevenlabs_api_key,
                text=text,
                voice="Matilda",
                stream=True
            )
            if audio_stream:
                stream(audio_stream)
            else:
                raise ValueError("Audio stream generation failed.")
        except Exception as e:
            print("Error generating audio: %s" % str(e))
