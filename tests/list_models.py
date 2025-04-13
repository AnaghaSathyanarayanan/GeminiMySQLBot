import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load the .env file containing your API key
load_dotenv()

# Get the API key
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# List available models
try:
    print("🔍 Listing available Gemini models...\n")
    models = genai.list_models()
    for model in models:
        print(f"📌 {model.name} -> {model.supported_generation_methods}")
except Exception as e:
    print("❌ Error listing models:", e)
