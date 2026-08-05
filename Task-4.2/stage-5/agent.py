import ollama
from tool_schema import TOOLS
from tools import calculator, get_current_time
from database import save_message, load_messages, create_table

MODEL = "qwen3:8b"

# System Prompt
SYSTEM_PROMPT = """
You are a helpful AI assistant.

You have access to external tools.

IMPORTANT RULES:

- If the user asks for the current time, ALWAYS call get_current_time.
- If the user asks for any mathematical calculation, ALWAYS call calculator.
- Never estimate, guess, or calculate these answers yourself.
- Wait for the tool result before answering.
- Use the tool result exactly as returned.
- Do not change or reinterpret the tool output.
- For greetings, small talk, explanations, opinions, and general knowledge, answer directly without tools.
- After receiving a tool result, write a natural sentence for the user.

Examples:

User: Hi
Assistant: Hello! How can I help you today?

User: What is 45 * 12?
→ Call calculator

User: What time is it in Karachi?
→ Call get_current_time

User: Who wrote Hamlet?
Assistant: William Shakespeare wrote Hamlet.
"""
# -------------------------
# Initialize Database
# -------------------------
create_table()

# Load previous conversation (persists across runs)
messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]
messages.extend(load_messages())

# -------------------------
# Tool Executor
# -------------------------
def execute_tool(tool_name, arguments):
    if tool_name == "calculator":
        return calculator(arguments["expression"])
    elif tool_name == "get_current_time":
        return get_current_time(arguments["timezone"])
    else:
        return "Tool not found"

# -------------------------
# Agent Function
# -------------------------
def run_agent(user_input):
    # Add user message to memory
    user_message = {
        "role": "user",
        "content": user_input
    }
    messages.append(user_message)
    save_message("user", user_input)

    # First LLM call — model decides if a tool is needed
    response = ollama.chat(
        model=MODEL,
        messages=messages,
        tools=TOOLS,
        options={
            "temperature": 0,
            "reasoning": False
        }
    )

    print("\nFirst Response:")
    print(response["message"])
    assistant_message = response["message"]

    # Check tool call(s)
    if assistant_message.get("tool_calls"):
        # Add the assistant's tool-call request to history ONCE
        # (not the raw tool_call var — the full assistant_message)
        messages.append(assistant_message)

        # Loop over ALL tool calls, not just the first
        for tool_call in assistant_message["tool_calls"]:
            tool_name = tool_call["function"]["name"]
            arguments = tool_call["function"]["arguments"]

            print("\nTool Selected:")
            print(tool_name)
            print("\nArguments:")
            print(arguments)

            # Execute Python function
            tool_result = execute_tool(tool_name, arguments)

            print("\nTool Result:")
            print(tool_result)

            # Tool result content MUST be a string
            messages.append(
                {
                    "role": "tool",
                    "content": str(tool_result)
                }
            )

        # Second LLM call — model turns tool result(s) into a final answer
        # No `tools=TOOLS` here, so it can't call another tool and must respond in text
        final_response = ollama.chat(
            model=MODEL,
            messages=messages,
            options={
                "temperature": 0,
                "reasoning": False
            }
        )

        print("\nFinal Response:")
        print(final_response["message"])

        answer = final_response["message"]["content"]
    else:
        # No tool needed — use the direct answer
        answer = assistant_message["content"]

    # Save final assistant response to memory + db
    # (we do NOT save the intermediate tool_calls/tool messages to db,
    # only the clean user/assistant exchange, matching load_messages() shape)
    messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
    save_message("assistant", answer)
    return answer

# -------------------------
# Chat Loop
# -------------------------
while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    answer = run_agent(user_input)
    print("\nAssistant:")
    print(answer)