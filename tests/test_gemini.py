import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

try:
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content("List some popular data science topics")
    print("✅ Gemini Response:", response.text)
except Exception as e:
    print("❌ Gemini API Error:", e)
