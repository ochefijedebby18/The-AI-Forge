import os
import anthropic
from dotenv import load_dotenv

# Load credentials and configuration
load_dotenv()

# Read environment variables
api_key = os.getenv("ANTHROPIC_API_KEY")
model = os.getenv("LLM_MODEL")

# Check configuration
if not api_key:
    raise ValueError("ANTHROPIC_API_KEY is missing.")

if not model:
    raise ValueError("LLM_MODEL is missing.")

# Create an Anthropic client
client = anthropic.Anthropic(api_key=api_key)

# Send a message to Claude
response = client.messages.create(
    model=model,
    max_tokens=150,
    messages=[
        {
            "role": "user",
            "content": "Explain what an API is in simple terms."
        }
    ]
)

# Display Claude's response
print("Claude's response:")
print(response.content[0].text)

# Display token usage
print("\nToken usage:")
print("Input tokens:", response.usage.input_tokens)
print("Output tokens:", response.usage.output_tokens)
