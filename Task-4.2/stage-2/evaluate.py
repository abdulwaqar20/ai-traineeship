import json
from pathlib import Path
import sys
import time

sys.path.append(r"D:\SCS-Internship\ai-traineeship\Task-4.2")

from llm_client import client

from prompt_versions import (
    NAIVE_PROMPT,
    CLEAR_PROMPT,
    FEW_SHOT_PROMPT,
    ROLE_PROMPT,
    ROLE_SYSTEM,
    REASONING_PROMPT
)

MODEL = "inclusionai/ling-3.0-flash:free"
# Load test data
test_file = Path(__file__).parent / "test_cases.json"
with open(test_file, "r", encoding="utf-8") as file:
    test_cases = json.load(file)

PROMPTS = {
    "Naive": {
        "system": None,
        "prompt": NAIVE_PROMPT
    },
    "Clear Instructions": {
        "system": None,
        "prompt": CLEAR_PROMPT
    },
    "Few Shot": {
        "system": None,
        "prompt": FEW_SHOT_PROMPT
    },
    "Role Prompt": {
        "system": ROLE_SYSTEM,
        "prompt": ROLE_PROMPT
    },
    "Reasoning": {
        "system": None,
        "prompt": REASONING_PROMPT
    }
}

def call_llm(system_prompt, user_prompt):
    messages = []

    if system_prompt:
        messages.append(
            {
                "role": "system",
                "content": system_prompt
            }
        )

    messages.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    try:
        response = client.chat.completions.create(
            model=MODEL,
            temperature=0,
            messages=messages
        )

        return response.choices[0].message.content

    except Exception as e:
        print(f"API Error: {e}")
        return None

def check_accuracy(output, expected):
    output = output.lower()
    category_correct = (expected["category"].lower() in output)
    priority_correct = (expected["priority"].lower() in output)
    return (category_correct and priority_correct)

results = {}

for prompt_name, prompt_data in PROMPTS.items():
    correct = 0
    print("\n======================")
    print(prompt_name)
    print("======================")
    for case in test_cases:
        email = case["email"]
        prompt = prompt_data["prompt"].format(email=email)

        answer = call_llm(prompt_data["system"],prompt)

        time.sleep(10)  # To avoid hitting rate limits

        if answer is None:
            print(f"Case {case['id']}: Skipped (API Error)")
            continue

        is_correct = check_accuracy(answer, case["expected"])
        if is_correct:
            correct += 1
        print(f"Case {case['id']}:","Correct" if is_correct else "Wrong")
    accuracy = correct / len(test_cases) * 100
    results[prompt_name] = accuracy

print("\n\nFINAL RESULTS")
print("======================")
for name, score in results.items():
    print(f"{name}: {score:.0f}%")