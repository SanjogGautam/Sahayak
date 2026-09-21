from google import genai
from dotenv import load_dotenv
import os
load_dotenv()
def ask(question: str, system = None,schema=None) -> str:

    kwargs={}
    if schema is not None:
        kwargs["response_format"]={

            "type": "text",
            "mime_type": "application/json",
            "schema": schema.model_json_schema()

        }
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
        stream=True,
        **kwargs
    )
    text = ""
    for event in stream:
        if event.event_type == "step.delta":
            if event.delta.type == "text":
                 text += event.delta.text
    return text
