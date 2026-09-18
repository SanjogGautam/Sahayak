from google import genai
from dotenv import load_dotenv
import os
load_dotenv()
def ask(question: str, system = None) -> str:
    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY"),
    )
    interaction = client.interactions.create(
        model="gemini-3.1-flash-lite",
        input=question,
        system_instruction=system,
        generation_config={
            "temperature": 0.0,
            "thinking_level": "high"
        },
    )
    return interaction.output_text
