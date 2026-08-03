from llm_client import client

response = client.chat.completions.create(
    model="inclusionai/ling-3.0-flash:free",
    messages=[
        {
            "role": "system",
            "content": "You are a concise AI assistant."
        },
        {
            "role": "user",
            "content": "What is Artificial Intelligence?"
        }
    ]
)

print(response.choices[0].message.content)