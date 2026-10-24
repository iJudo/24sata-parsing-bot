from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

async def generate_description(title):
    prompt = (
        f"Napiši iznimno privlačan i kratak opis (max 150 znakova) za vijest: '{title}'. "
        f"Cilj je da korisnik klikne na poveznicu. Odgovori isključivo tekstom opisa na hrvatskom."
    )

    safety_settings = [
        types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                            threshold=types.HarmBlockThreshold.BLOCK_NONE),
        types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_HARASSMENT,
                            threshold=types.HarmBlockThreshold.BLOCK_NONE),
        types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
                            threshold=types.HarmBlockThreshold.BLOCK_NONE),
        types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                            threshold=types.HarmBlockThreshold.BLOCK_NONE),
        types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_CIVIC_INTEGRITY,
                            threshold=types.HarmBlockThreshold.BLOCK_NONE),
    ]

    try:
        response = await client.aio.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt,
            config=types.GenerateContentConfig(
                safety_settings=safety_settings,
                temperature=0.7
            )
        )
        return response.text.strip() if response.text else "Saznajte više detalja klikom na članak..."
    except Exception as e:
        print(f"Error: {e}")
        return "Error"