import os
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")
print(f"API Key loaded: {api_key[:10]}..." if api_key else "No API key found")

# Test API connection
try:
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello, just testing!"}],
        max_tokens=10
    )
    print("✅ API key works!")
    print(f"Response: {response.choices[0].message.content}")
except Exception as e:
    print(f"❌ API Error: {e}")