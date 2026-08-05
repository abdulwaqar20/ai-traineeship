import ollama
import json
from tools import calculator, get_current_time

# -------------------------
# Tool Schema
# -------------------------
tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description":
            "Calculate mathematical expressions",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description":
                        "Mathematical expression"
                    }
                },
                "required": [
                    "expression"
                ]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description":
            """
            Get current time for a timezone.
            Use IANA timezone format.
            Examples:
            Asia/Tokyo
            Asia/Karachi
            America/New_York
            """,
            "parameters": {
                "type": "object",
                "properties": {
                    "timezone": {
                        "type": "string"
                    }
                },
                "required": [
                    "timezone"
                ]
            }
        }
    }
]

# -------------------------
# Available Python Tools
# -------------------------
available_tools = {
    "calculator": calculator,
    "get_current_time": get_current_time
}

# -------------------------
# Chat Function
# -------------------------
def run_agent(user_question):
    messages = [
        {
            "role":"system",
            "content":
            """
            You are a helpful assistant.

            Rules:
            1. Use calculator only for mathematical calculations.
            2. Use get_current_time only for time questions.
            3. If no tool is needed, answer directly.
            4. Never create fake tool calls.
            """
        },
        {
            "role":"user",
            "content":user_question
        }
    ]

    # First LLM call
    response = ollama.chat(
        model="llama3.1",
        messages=messages,
        tools=tools
    )
    message = response["message"]

    # Check if model wants a tool
    if message.get("tool_calls"):
        tool_call = message["tool_calls"][0]
        function_name = (
            tool_call["function"]["name"]
        )
        arguments = (
            tool_call["function"]["arguments"]
        )
        print("\nTool Selected:")
        print(function_name)
        print("Arguments:")
        print(arguments)
        # Execute Python function
        function = available_tools[function_name]
        result = function(**arguments)

        print("\nTool Result:")
        print(result)
        # -------------------------
        # Send tool result back
        # -------------------------
        messages.append(
            {
                "role":"assistant",
                "tool_calls":[tool_call]
            }
        )
        messages.append(
            {
                "role":"tool",
                "content":result
            }
        )
        # Second LLM call
        final_response = ollama.chat(
            model="llama3.1",
            messages=messages
        )
        return final_response["message"]["content"]
    else:
        return message["content"]

# -------------------------
# Testing
# -------------------------
questions = [
    "What is 4892 * 17?",
    "What time is it in Tokyo?",
    "Who wrote Hamlet?"
]

for q in questions:
    print("\n====================")
    print("Question:")
    print(q)
    answer = run_agent(q)
    print("\nAnswer:")
    print(answer)