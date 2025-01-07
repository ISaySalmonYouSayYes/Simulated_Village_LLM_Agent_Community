from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Access environment variables
OPENAI_API_KEY = os.getenv("openAI_Key")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")

# Validate required variables
if not OPENAI_API_KEY:
    raise ValueError("Environment variable 'openAI_Key' is missing or empty.")
if not LANGSMITH_API_KEY:
    raise ValueError("Environment variable 'LANGSMITH_API_KEY' is missing or empty.")