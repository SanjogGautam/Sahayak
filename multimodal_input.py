from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY"),
)
uploaded_file=client.files.upload(file="a.jpg")
interaction = client.interactions.create(
        model="gemini-3.1-flash-lite",
        input=[
            {"type":"text","text":"Tell me about this image"},
            {
                "type":"image",
                "uri":uploaded_file.uri,
                "mime_type": uploaded_file.mime_type,
            }
        ],
        generation_config={
            "temperature": 0.0,
            "thinking_level": "high"
        },
    )
print(interaction.output_text)
