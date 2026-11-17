import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve configuration
api_key = os.getenv("ANTHROPIC_API_KEY")
model = os.getenv("LLM_MODEL")

# Check configuration without revealing the secret
if api_key:
    print("Anthropic API key: Configured")
else:
    print("Anthropic API key: Missing")

if model:
    print("LLM model:", model)
else:
    print("LLM model: Not configured")