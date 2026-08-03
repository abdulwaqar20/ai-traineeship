import json
import ollama
from pathlib import Path
from pydantic import BaseModel, ValidationError, Field
from typing import Literal
# ==================================
# Schema Definition
# ==================================
class SupportTicket(BaseModel):
    category: Literal[
        "Billing",
        "Technical",
        "Account",
        "Security",
        "General"
    ] = Field(
        description="Main category of customer issue"
    )

    priority: Literal[
        "Low",
        "Medium",
        "High",
        "Critical"
    ] = Field(
        description="Urgency level of the issue"
    )

    summary: str = Field(
        description="Short summary of the customer issue"
    )
    sentiment: Literal[
        "Positive",
        "Neutral",
        "Negative"
    ] = Field(
        description="Customer sentiment towards the issue"
    )

# ==================================
# System Prompt
# ==================================
SYSTEM_PROMPT = """
You are an expert customer support ticket classifier.
Classify customer emails using these rules.
CATEGORY RULES:
Billing:
- Payment failures
- Duplicate charges
- Incorrect invoices
- Subscription problems
- Refund requests

Technical:
- Application crashes
- Bugs
- Software errors
- Installation problems
- Performance issues

Account:
- Login problems
- Password reset
- Forgot username
- Account deletion
- Profile updates

Security:
- Hacked accounts
- Unauthorized access
- Suspicious login attempts
- Unknown transactions

General:
- General questions
- Feedback
- Compliments

PRIORITY RULES:
Critical:
- Hacked accounts
- Unauthorized transactions
- Security breaches

High:
- Payment failures
- Duplicate billing
- Service outage
- Serious technical problems

Medium:
- Login problems
- Password issues
- Normal errors

Low:
- Information requests
- Account updates
- General feedback

SENTIMENT RULES:
Positive:
- Customer is happy or thankful

Negative:
- Customer complains or reports a problem

Neutral:
- Customer asks a normal question

Return ONLY valid JSON.
Do not add markdown.
Do not add explanations.
Required JSON format:

{
    "category": "Billing | Technical | Account | Security | General",
    "priority": "Low | Medium | High | Critical",
    "summary": "short explanation",
    "sentiment": "Positive | Neutral | Negative"
}
"""
# ==================================
# LLM Function
# ==================================
def call_llm(email, retries=2):
    for attempt in range(retries):
        try:
            response = ollama.chat(
                model="phi3",
                messages=[
                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT
                    },
                    {
                        "role": "user",
                        "content": email
                    }
                ],
                format="json"
            )
            content = response["message"]["content"]
            data = json.loads(content)
            ticket = SupportTicket(**data)
            return ticket
        except ValidationError as e:
            print("\nSchema validation failed:")
            print(e)
        except json.JSONDecodeError:
            print("\nInvalid JSON received from model")
        except Exception as e:
            print("\nLLM Error:")
            print(e)
        print(f"Retrying... ({attempt+1}/{retries})")
    return None

# ==================================
# Load Test Cases
# ==================================
file_path = Path(__file__).parent / "test_cases.json"
with open(file_path, "r",encoding="utf-8") as file:
    test_cases = json.load(file)

# ==================================
# Evaluation
# ==================================
correct = 0
total = len(test_cases)

for case in test_cases:
    print("\n================")
    print(f"Case: {case['id']}")

    ticket = call_llm(case["email"])

    if ticket:
        print(ticket)
        expected = case["expected"]

        if (
            ticket.category == expected["category"]
            and
            ticket.priority == expected["priority"]
            and
            ticket.sentiment == expected["sentiment"]
        ):
            print("Correct")
            correct += 1
        else:
            print("Wrong")
    else:
        print("Failed")



# ==================================
# Final Result
# ==================================

accuracy = (correct / total) * 100
print("\n================")
print(f"Accuracy: {accuracy:.2f}%")
print("================")