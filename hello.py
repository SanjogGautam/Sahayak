from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

client=genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
)
interaction= client.interactions.create(
    model= "gemini-3.8-flash",
    input="what is andromeda galaxy? ",
    generation_config={
        "thinking_level":"low"
    }

)
print(interaction.output_text)