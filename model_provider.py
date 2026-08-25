from google import genai

# Initialize the Gemini client (uses GEMINI_API_KEY from environment)
client = genai.Client()

# Model ID for text generation
MODEL_ID = "gemini-3.6-flash"


# Send a prompt to Gemini and return the generated text
def generate(prompt: str) -> str:
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt,
    )
    return response.text