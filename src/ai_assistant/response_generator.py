from dotenv import load_dotenv
from openai import OpenAI
import os
from src.constants import voice_ai_contstnts


class ResponseGenerator:
    def __init__(self):
        # Initialize the OpenAI client
        self.openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate_response(self, full_transcript):
        # Generate a response using OpenAI's GPT-3.5-turbo model

        response = self.openai_client.chat.completions.create(
            model=voice_ai_contstnts.OPEN_AI_MODEL_NAME,
            messages=full_transcript
        )
        response_text = response.choices[0].message.content
        print("\nAI Agent:", response_text)
        return response_text
