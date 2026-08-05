import time
import ollama
from langchain_classic.memory import ConversationBufferWindowMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Configuration
MODEL_NAME = "qwen3:8b"
ROLE_MAP = {"human": "user", "ai": "assistant", "system": "system"}
# Memory
memory = ConversationBufferWindowMemory(
    k=5,
    return_messages=True
)

# Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a helpful AI assistant.

Answer naturally and accurately.

If you don't know something, say so instead of making it up.
"""
        ),
        MessagesPlaceholder(variable_name="history"),
        ("user", "{input}")
    ]
)

# Chat Function
def chat(user_input):
    history = memory.load_memory_variables({})["history"]
    messages = prompt.format_messages(
        history=history,
        input=user_input
    )

    ollama_messages = [
        {
            "role": ROLE_MAP[message.type],
            "content": message.content
        }
        for message in messages
    ]

    start = time.time()
    response = ollama.chat(
        model=MODEL_NAME,
        messages=ollama_messages,
        think=False,
        options={
            "temperature": 0,
            "num_ctx": 4096
        },
        keep_alive="30m"
    )
    elapsed = time.time() - start
    assistant_reply = response["message"]["content"]
    memory.save_context(
        {"input": user_input},
        {"output": assistant_reply}
    )
    print(f"\nResponse Time: {elapsed:.2f} seconds")
    return assistant_reply

# Chat Loop
print("AI Chatbot")

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        print("\nGoodbye!")
        break

    reply = chat(user_input)
    print("\nAssistant:")
    print(reply)