from google import genai
from dotenv import load_dotenv
import os
from schemas import Recipe
load_dotenv()
def ask(question: str, system = None) -> str:
    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY"),
    )
    stream = client.interactions.create(
        model="gemini-3.1-flash-lite",
        input=question,
        system_instruction=system,
        generation_config={
            "temperature": 0.0,
            "thinking_level": "high"
        },
        response_format={
            "type":"text",
            "mime_type":"application/json",
            "schema": Recipe.model_json_schema()
        },
        stream=True,
    )
    for event in stream:
        if event.event_type=="step.delta":
            if event.delta_type=="text":
                return event.delta_text
