# Stage 3 – Structured Output with Pydantic Validation

## Objective

The goal of Stage 3 is to generate structured data from an LLM instead of plain text. Rather than asking the model to return natural language, we define a schema and validate the response before using it in our application.

---

## Technologies Used

* Python
* Ollama
* Phi-3
* Pydantic
* JSON

---

## Project Structure

```text
stage-3/
│── structured_output.py
│── test_cases.json
│── stage3.md
```

---

## How It Works

The program follows these steps:

1. Load the customer support emails from `test_cases.json`.
2. Send each email to the Phi-3 model running locally through Ollama.
3. Instruct the model to return only JSON.
4. Parse the JSON response.
5. Validate the response using a Pydantic schema.
6. Compare the predicted category and priority with the expected values.
7. Calculate the overall accuracy.

---

## Pydantic Schema

The model returns the following fields:

* **category**

  * Billing
  * Technical
  * Account
  * Security
  * General

* **priority**

  * Low
  * Medium
  * High
  * Critical

* **summary**

  * A short description of the issue.

* **sentiment**

  * Positive
  * Neutral
  * Negative

Pydantic ensures that every response follows this schema. If the model returns an invalid value, validation fails and the program handles the error gracefully instead of crashing.

---

## Prompt Design

A system prompt was used to guide the model. It contains:

* Classification rules for each category.
* Priority assignment rules.
* Sentiment rules.
* Instructions to return only valid JSON.
* The required JSON structure.

Using a system prompt improved consistency compared to placing all instructions inside the user prompt.

---

## Error Handling

The application handles multiple types of failures:

* Invalid JSON returned by the model.
* Pydantic validation errors.
* Runtime exceptions while communicating with the model.

If an error occurs, the program reports the issue and continues processing the remaining test cases.

---

## Dataset

A dataset of **20 customer support emails** was created containing different categories of issues such as:

* Billing
* Technical
* Account
* Security
* General

Each test case includes the expected category and priority, allowing the model's predictions to be evaluated.

---

## Evaluation

For each email:

1. The email is sent to the model.
2. The JSON response is validated.
3. The predicted category and priority are compared with the expected values.
4. The prediction is marked as **Correct** or **Wrong**.

Finally, the overall accuracy is calculated.

Example output:

```text
================
Case: 1

category='Billing'
priority='High'
summary='Customer reports duplicate billing and requests a refund.'
sentiment='Negative'

Correct
```

---

## Results

Current implementation:

* Valid JSON generation: ✅
* Pydantic validation: ✅
* Error handling: ✅
* Processed test cases: 20
* Model used: Phi-3 (Ollama)
* Accuracy achieved: **60%**

Most prediction errors were related to **priority classification**, while category prediction was generally accurate.

---

## What I Learned

During this stage, I learned:

* Why structured output is preferred over plain text in production applications.
* How Pydantic validates LLM responses.
* How to convert JSON into Python objects safely.
* How to handle invalid outputs without crashing the application.
* The importance of prompt engineering in improving structured responses.
* How to evaluate an LLM using a labeled dataset.

---

## Conclusion

Stage 3 successfully demonstrates how to build a structured-output pipeline using a local LLM. The application generates JSON responses, validates them with Pydantic, handles errors gracefully, and evaluates predictions against a labeled dataset. This approach is much more reliable than parsing free-form text and forms the foundation for building production-ready AI applications.
