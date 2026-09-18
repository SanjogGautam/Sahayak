from google import genai
from dotenv import load_dotenv
import os
load_dotenv()
client=genai.Client(
api_key=os.getenv("GEMINI_API_KEY"),
)
interaction=client.interactions.create(
model="gemini-3.1-flash-lite",
input="how tall is mount everest?",
generation_config={
"temperature":0.0,
"thinking_level":"high"
},
)
print(interaction.output_text)