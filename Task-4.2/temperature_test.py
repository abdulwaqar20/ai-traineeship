from llm_client import client

prompt = "Create a unique metaphor to explain artificial intelligence."

temperatures = [0, 1]


for temp in temperatures:

    print("\n====================")
    print(f"Temperature: {temp}")
    print("====================")

    for i in range(3):

        response = client.chat.completions.create(
            model="inclusionai/ling-3.0-flash:free",
            temperature=temp,
            messages=[
                {
                    "role": "system",
                    "content": "You are a concise AI assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        answer = response.choices[0].message.content

        print(f"\nRun {i+1}:")
        print(answer)