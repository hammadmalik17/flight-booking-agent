import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load your .env environment variables
load_dotenv()

# Configure the Gemini client
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use the correct model
model = genai.GenerativeModel("models/gemini-2.0-flash")

# Generate content
response = model.generate_content("Explain how AI works in a few words")

# Print the result
print("🤖 Gemini responds:\n", response.text)
