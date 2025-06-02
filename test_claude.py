import anthropic
import os

# Replace with your Claude API key
os.environ["ANTHROPIC_API_KEY"] = "sk-..."

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-3-opus-20240229",  # You can also try claude-3-sonnet or haiku
    max_tokens=256,
    messages=[
        {"role": "user", "content": "Explain quantum physics in one sentence."}
    ]
)

print(response.content[0].text)
