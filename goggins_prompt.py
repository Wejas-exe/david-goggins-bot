import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Check if API key exists
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")  # Use 1.5 if 2.0 doesn't respond

def get_goggins_response(user_input):
    if not user_input or not isinstance(user_input, str):
        return "I need something to respond to, stay hard!"
        
    prompt = f"""
You are David Goggins, the motivational beast.
Speak like Goggins — raw, real, intense, and no-nonsense.
Encourage the user in your typical style.

User: {user_input}
David Goggins:
"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Error generating response: {str(e)}")
        return "Goggins is taking a mental break. Stay hard and try again!"