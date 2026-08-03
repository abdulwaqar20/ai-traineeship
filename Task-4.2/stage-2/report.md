# Stage 2 — Prompt Iteration Study

## Objective

The goal of Stage 2 was to understand how prompt engineering affects the performance of Large Language Models (LLMs).

Instead of changing the model, we kept the same model and dataset, then improved only the prompts step by step.

The experiment followed this flow:

```
Naive Prompt
      |
      ↓
Clear Instructions
      |
      ↓
Few-Shot Examples
      |
      ↓
Role/System Prompt
      |
      ↓
Reasoning Instructions
```

The performance of each prompt was measured on the same 10 customer support emails.

---

# Task Description

The selected task was:

**Customer Support Ticket Classification**

Given a customer email, the model should extract:

- Category
- Priority
- Summary

Example:

Input:

```
My card was charged twice for my subscription.
Please refund the extra payment.
```

Expected output:

```
Category: Billing
Priority: High
Summary: Customer was charged twice for a subscription.
```

---

# Dataset

The evaluation dataset contains 10 customer support emails.

Each test case contains:

- Customer email
- Expected category
- Expected priority
- Expected summary

Dataset file:

```
test_cases.json
```

Example structure:

```json
{
    "email": "My password stopped working.",
    "expected": {
        "category": "Account",
        "priority": "Medium",
        "summary": "Customer cannot access account."
    }
}
```

---

# Prompt Versions

## 1. Naive Prompt

Prompt:

```
Extract information from this email.
```

Problem:

The model does not know:

- Which information to extract.
- Required format.
- Categories or priorities.

This creates ambiguity.

---

## 2. Clear Instructions Prompt

The prompt was improved by explicitly defining the required output:

```
Extract:
- Category
- Priority
- Summary

Return the answer in this format.
```

Improvement:

The model receives a clear target structure.

---

## 3. Few-Shot Prompt

Examples were added inside the prompt.

Example:

```
Email:
I forgot my password.

Output:
Category: Account
Priority: Medium
```

The model learns the expected pattern from examples.

This technique is called:

**In-context learning**

The model is not trained. Examples are only provided during inference.

---

## 4. Role/System Prompt

A system instruction was added:

```
You are an expert customer support analyst.
```

The purpose was to give the model a specific role and behavior.

---

## 5. Reasoning Instruction Prompt

The model was instructed to analyze the problem carefully before answering.

Example:

```
Identify the problem.
Determine category.
Determine priority.
Return only the final answer.
```

The goal was to improve decision making on difficult cases.

---

# Evaluation Method

The same 10 test cases were used for every prompt version.

For each prompt:

```
10 Emails
    |
    ↓
LLM Prediction
    |
    ↓
Compare with Expected Output
    |
    ↓
Calculate Accuracy
```

Accuracy formula:

```
Accuracy = (Correct Predictions / Total Predictions) × 100
```

---

# Model Used

Model:

```
inclusionai/ling-3.0-flash:free
```

Provider:

```
OpenRouter API
```

Temperature:

```
0
```

Reason:

The evaluation should be consistent and deterministic.

---

# Results

| Prompt Version | Correct Results | Accuracy |
|---|---:|---:|
| Naive | 0/10 | 0% |
| Clear Instructions | 4/10 | 40% |
| Few Shot | 6/10 | 60% |
| Role Prompt | 5/10 | 50% |
| Reasoning | 5/10 | 50% |

---

# Analysis

## Naive Prompt

Result:

```
0%
```

The model failed because the instruction was too broad.

The model did not know the required fields or output format.

---

## Clear Instructions

Result:

```
40%
```

Adding explicit instructions improved the performance.

The model understood what information needed to be extracted.

---

## Few-Shot Examples

Result:

```
60%
```

This was the best-performing prompt.

Providing examples helped the model understand the expected pattern and output style.

---

## Role Prompt

Result:

```
50%
```

The role instruction improved consistency but was less effective than examples.

A role alone does not always provide enough guidance.

---

## Reasoning Prompt

Result:

```
50%
```

Reasoning instructions helped some cases but did not significantly improve performance.

The effectiveness depends on the model and task complexity.

---

# Key Learnings

## 1. Prompt quality directly affects model performance

A vague prompt produces unreliable results.

Clear instructions improve accuracy.

---

## 2. Examples are powerful

Few-shot prompting allows the model to learn the expected behavior from examples without any training.

---

## 3. More instructions do not always mean better results

Adding a role or reasoning instructions may not improve every task.

The prompt should match the problem.

---

## 4. Evaluation is important

Prompt improvements should be measured using the same test cases.

Without evaluation, prompt changes are only guesses.

---

# Stage 2 Status

✅ Created evaluation dataset  
✅ Designed multiple prompt versions  
✅ Tested prompts on the same inputs  
✅ Compared accuracy results  
✅ Analyzed prompt improvements  

**Stage 2 Completed Successfully**