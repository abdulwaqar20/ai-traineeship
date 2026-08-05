from memory import messages

messages.append(
    {
        "role": "user",
        "content": "Hi"
    }
)

messages.append(
    {
        "role": "assistant",
        "content": "Hello!"
    }
)

messages.append(
    {
        "role": "user",
        "content": "My name is Waqar."
    }
)

for message in messages:
    print(message)