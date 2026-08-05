import json
from pathlib import Path
import ollama


MODEL = "llama3.1"


# -------------------------
# Load Test Cases
# -------------------------

file_path = Path(__file__).parent / "test_cases.json"
with open(file_path,"r",encoding="utf-8") as file:
    test_cases = json.load(file)

# -------------------------
# Tool Definitions
# -------------------------

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description":
            """
            Use this tool for mathematical calculations.
            """,
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
            Get current time of a location.
            Use IANA timezone format.
            Example:
            Asia/Tokyo
            Asia/Karachi
            Europe/London
            """,
            "parameters": {
                "type": "object",
                "properties": {
                    "timezone": {
                        "type": "string",
                        "description":
                        "Timezone name"
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
# Detect Tool Selected
# -------------------------
def detect_tool(question):
    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content":
                """
                You are an intelligent assistant.
                Your first job is to decide whether a tool is required.

                STRICT RULES:
                1. Use calculator ONLY when the user asks for:
                - arithmetic
                - mathematical calculations
                - numerical operations

                2. Use get_current_time ONLY when the user asks:
                - current time
                - present time
                - time in a specific location

                3. NEVER use tools for:
                - history questions
                - science explanations
                - famous people
                - general knowledge
                - definitions
                If no tool is required, answer directly.
                Avoid unnecessary tool calls.
                """
            },
            {
                "role": "user",
                "content": question
            }
        ],
        tools=TOOLS
    )
    tool_calls = response.message.tool_calls

    if tool_calls:
        return tool_calls[0].function.name
    return "none"

# -------------------------
# Evaluation
# -------------------------
correct = 0
for case in test_cases:
    print("\n====================")
    print("Question:")
    print(case["question"])
    selected_tool = detect_tool(case["question"])
    print("\nSelected Tool:")
    print(selected_tool)
    expected = case["expected_tool"]
    if selected_tool == expected:
        print("Correct")
        correct += 1
    else:
        print("Wrong","| Expected:",expected)

accuracy = (correct /len(test_cases)) * 100

print("\n====================")
print(f"Tool Selection Accuracy: {accuracy:.2f}%")
print("====================")