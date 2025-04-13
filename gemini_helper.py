import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Gemini API Error: {e}"
