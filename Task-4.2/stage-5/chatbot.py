import ollama
from memory import messages

MODEL = "llama3.1"

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    if not user_input.strip():
        continue
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = ollama.chat(
        model=MODEL,
        messages=messages
    )
    answer = response["message"]["content"]
    print("\nAssistant:", answer)

    messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )