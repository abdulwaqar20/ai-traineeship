# prompt_versions.py


# Version 1: Naive Prompt
NAIVE_PROMPT = """
Extract information from this email.
"""


# Version 2: Clear Instructions
CLEAR_PROMPT = """
You are analyzing customer support emails.

Extract these three fields:

1. Category
2. Priority
3. Summary

Use the following format:

Category:
Priority:
Summary:

Email:
{email}
"""


# Version 3: Few-Shot Examples
FEW_SHOT_PROMPT = """
You are a customer support ticket classifier.

Extract:
- Category
- Priority
- Summary

Example 1:

Email:
"I forgot my password and cannot login."

Output:
Category: Account
Priority: Medium
Summary: Customer cannot access account because they forgot password.


Example 2:

Email:
"My card was stolen and someone made unauthorized purchases."

Output:
Category: Security
Priority: Critical
Summary: Customer reports unauthorized transactions.


Now analyze this email:

{email}

Return only:

Category:
Priority:
Summary:
"""


# Version 4: Role/System Framing
ROLE_SYSTEM = """
You are an expert customer support analyst.

You classify customer problems accurately.
You understand customer intent and assign the correct priority level.

Your task is to analyze support emails and extract:

- Category
- Priority
- Summary

Be precise and consistent.
"""


ROLE_PROMPT = """
Analyze this customer support email.

Return:

Category:
Priority:
Summary:

Email:
{email}
"""


# Version 5: Step-by-step Reasoning Instruction
REASONING_PROMPT = """
You are an expert support ticket classifier.

Analyze the email carefully before answering.

Follow these steps internally:

1. Identify the customer's main problem.
2. Decide the correct category.
3. Determine urgency and priority.
4. Write a short summary.

Do not include your reasoning.
Only return:

Category:
Priority:
Summary:

Email:
{email}
"""