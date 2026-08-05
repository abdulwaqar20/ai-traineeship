from system_prompt import SYSTEM_PROMPT
from database import load_messages, create_table

create_table()

# messages = [
#     {
#         "role": "system",
#         "content": SYSTEM_PROMPT
#     }
# ]

messages = load_messages()