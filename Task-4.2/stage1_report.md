# Stage 1 — First API Call, Secrets Done Right

## Objective

The goal of Stage 1 was to understand how to connect a Python application with an LLM API, securely manage API keys, send messages to the model, inspect the response object, and understand how temperature affects model generation.

---

# Project Setup

## Tools Used

- Python
- OpenRouter API
- Model: `inclusionai/ling-3.0-flash:free`
- OpenAI Python SDK (OpenRouter compatible)
- python-dotenv

---

# Project Structure

```
Task-4.2/
│
├── .env
├── .gitignore
├── requirements.txt
│
├── config.py
├── llm_client.py
│
├── stage1_api.py
└── temperature_test.py
```

---

# 1. Environment Variables and API Security

## Why use `.env`?

The API key is a secret credential. It should not be written directly inside Python files because exposing it publicly can allow others to use the account.

Instead, the API key is stored in:

```
.env
```

Example:

```env
OPENROUTER_API_KEY=your_api_key_here
```

The `.env` file is added to `.gitignore` so it is not uploaded to GitHub.

---

# 2. Loading API Key

## `config.py`

The purpose of `config.py` is to load environment variables and make the API key available to the rest of the application.

Flow:

```
.env file
    |
    | load_dotenv()
    ↓
Environment Variables
    |
    | os.getenv()
    ↓
Python Variable
```

### Important Functions

### `load_dotenv()`

Reads the `.env` file and loads the variables into the environment.

### `os.getenv()`

Retrieves a specific variable from the environment.

It does not directly read the `.env` file.

---

# 3. Creating the API Client

## `llm_client.py`

The client is responsible for communicating with OpenRouter.

The client handles:

- Authentication using the API key
- Sending HTTP requests
- Receiving responses
- Formatting requests correctly

Flow:

```
Python Code

     ↓

OpenAI Client

     ↓

OpenRouter API

     ↓

LLM Model
```

The OpenAI SDK is used because OpenRouter provides an OpenAI-compatible API format.

---

# 4. First API Request

## Messages Format

The model receives messages as a list.

Example:

```python
messages=[
    {
        "role": "system",
        "content": "You are a concise AI assistant."
    },
    {
        "role": "user",
        "content": "What is Artificial Intelligence?"
    }
]
```

---

# System Message vs User Message

## System Message

The system message defines the behavior and personality of the model.

Example:

```
You are a concise AI assistant.
```

It works like a permanent instruction.

---

## User Message

The user message contains the actual request.

Example:

```
What is Artificial Intelligence?
```

---

# 5. Understanding the Response Object

The API does not return a simple string.

It returns a response object containing:

- Request ID
- Model information
- Generated choices
- Token usage
- Assistant message

Example:

```
response

├── id
├── model
├── choices
├── usage
└── provider
```

---

# Extracting the Assistant Response

The generated text is accessed using:

```python
response.choices[0].message.content
```

Explanation:

```
response
   |
   └── choices
          |
          └── [0]
                |
                └── message
                       |
                       └── content
```

Meaning:

- `response` → complete API response
- `choices` → list of generated responses
- `[0]` → first generated response
- `message` → assistant message object
- `content` → actual generated text

---

# 6. Temperature Experiment

## Purpose

Temperature controls how much randomness is used during generation.

---

# Temperature = 0

Low temperature produces more deterministic outputs.

Characteristics:

- More predictable
- More consistent
- Good for tasks like:
  - Classification
  - Extraction
  - Structured output

Example behavior:

```
Run 1:
Same style

Run 2:
Same style

Run 3:
Similar style
```

---

# Temperature = 1

Higher temperature allows more variation.

Characteristics:

- More creative
- More diverse responses
- Useful for:
  - Brainstorming
  - Creative writing
  - Idea generation

---

# Experiment Prompt

```
Create a unique metaphor to explain artificial intelligence.
```

---

# Results

## Temperature 0

Observations:

- The model repeatedly preferred similar metaphors.
- The "loom/tapestry" concept appeared multiple times.
- Responses were more consistent.

Example:

```
Artificial Intelligence: The Infinite Tapestry Weaver
```

---

## Temperature 1

Observations:

- The model produced different creative directions.
- Different metaphors appeared.

Examples:

```
The Weaver in the Dark Room
```

```
The Master Carpenter Who Has Never Touched Wood
```

```
AI as a Coral Reef
```

---

# Comparison

| Temperature | Behavior |
|---|---|
| 0 | More deterministic and predictable |
| 1 | More diverse and creative |

---

# Key Learnings

## 1. API Architecture

```
Python Application

        ↓

OpenRouter Client

        ↓

OpenRouter API

        ↓

LLM Model

        ↓

Response Object
```

---

## 2. Secure API Handling

Secrets should be stored separately:

```
.env
```

and loaded using:

```python
load_dotenv()
```

---

## 3. Client Responsibility

The client object:

- Sends requests
- Adds authentication
- Communicates with the API server

---

## 4. Response Understanding

LLM responses are structured objects, not plain text.

The generated answer is only one part:

```python
response.choices[0].message.content
```

---

## 5. Temperature Behavior

Temperature changes sampling behavior:

- Lower temperature → focused and consistent
- Higher temperature → varied and creative

---

# Stage 1 Status

✅ API connection completed  
✅ API key secured using `.env`  
✅ OpenRouter client created  
✅ System and user messages used  
✅ Response object inspected  
✅ Text extraction implemented  
✅ Temperature experiment completed  

**Stage 1 Completed Successfully**