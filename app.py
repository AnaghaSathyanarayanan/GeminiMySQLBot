import streamlit as st
from database import fetch_student_course_data
from gemini_helper import get_gemini_response
from ui import display_ui  # Import the display_ui function from ui.py

from dotenv import load_dotenv
import os

load_dotenv()  # This loads variables from your .env file into the environment

api_key = os.getenv("GEMINI_API_KEY")

# Streamlit App
user_prompt = display_ui()  # Call the UI function to handle the input and buttons

if user_prompt:
    try:
        # Fetch data from the database
        results = fetch_student_course_data()

        # Build context string from DB data
        context_data = "\n".join([ 
            f"ID: {row[0]}, Name: {row[1]} {row[2]}, Email: {row[3]}, Course: {row[4]}" 
            for row in results
        ])
        
        full_prompt = f"""You are a helpful assistant for a university database.
Here is the list of students and their courses:

{context_data}

Now answer this question:
{user_prompt}
"""

        # Get Gemini response
        with st.spinner("Thinking..."):
            gemini_reply = get_gemini_response(full_prompt)
            st.markdown(f"**Gemini says:** {gemini_reply}")

    except Exception as e:
        st.error(f"❌ Failed to connect to database: {e}")
