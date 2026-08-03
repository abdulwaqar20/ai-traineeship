# llm_client.py

# from openai import OpenAI
# from config import OPENROUTER_API_KEY
# # from mistralai import Mistral
# # from config import MISTRAL_API_KEY

# client = OpenAI(
#     api_key= OPENROUTER_API_KEY,
#     base_url="https://openrouter.ai/api/v1"
# )


import os
from cerebras.cloud.sdk import Cerebras

client = Cerebras(
    api_key=os.environ.get("CEREBRAS_API_KEY")
)