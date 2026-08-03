# import os
# from dotenv import load_dotenv

# # Load variables from .env
# load_dotenv()

# # Read the API key
# # MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
# OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# # Optional safety check
# if OPENROUTER_API_KEY is None:
#     raise ValueError("OPENROUTER_API_KEY not found in .env file")


import os
from dotenv import load_dotenv
from cerebras.cloud.sdk import Cerebras

# Load variables from .env
load_dotenv()

# Initialize the Cerebras client
client = Cerebras(
    api_key=os.environ.get("CEREBRAS_API_KEY")
)

# Optional safety check
if not client.api_key:
    raise ValueError("CEREBRAS_API_KEY not found in .env file or environment variables")