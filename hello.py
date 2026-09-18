from google import genai
from dotenv import load_dotenv
import os
load_dotenv()
client=genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
)
interaction=client.interactions.create(
    model="gemini-3.8-flash",
    system_instruction="Your name is Sanjog Gautam. You are a BSC.CSIT student at 6th semester",
    input="Hello there!"
)
print(interaction.output_text)