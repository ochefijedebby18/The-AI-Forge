# Phase 00 — Lesson 04: APIs & Keys

## 1. What Is an API?

API stands for **Application Programming Interface**.

An API allows two different software applications to communicate and exchange information.

For example, an AI application can send a request to an external AI service and receive a generated response. The application does not need to build and run the AI model itself; it can communicate with a model hosted by another provider.

### Simple example

Imagine asking an AI application:

"What is machine learning?"

The application sends the question to an AI service through an API. The service processes the request and sends a response back to the application.

The basic process is:

1. An application prepares a request.
2. It sends the request to an API endpoint.
3. The API receives and processes the request.
4. The service sends a response.
5. The application uses or displays the response.

## 2. The Four Main Parts of an API Request

### A. Endpoint

An endpoint is the URL or address where an API request is sent.

Example:

`https://api.anthropic.com/v1/messages`

It tells the application where to send its request.

### B. API Key

An API key is a credential used to identify an application or account and authorize API access.

It helps the service determine whether a request is permitted.

An API key must be kept private because someone who obtains it may be able to make requests using the associated account.

### C. Request Body

The request body contains the information being sent to the API.

For an AI API, it can include:
- The model to use.
- The maximum number of tokens to generate.
- The user's message.
- Other generation settings.

### D. Response Body

The response body contains the information returned by the API.

For an AI request, it usually contains the generated response and other information about the request.

## 3. What Is an API Key?

An API key is similar to a password or access credential for an API.

It is used to authenticate and authorize requests.

API keys should never be:
- Hardcoded directly into application source code.
- Uploaded to GitHub.
- Shared publicly.
- Included in screenshots or public documentation.
- Committed to a Git repository.

If an API key is exposed, it should be revoked or rotated immediately.

## 4. Environment Variables

An environment variable is a value stored outside the source code that a program can access while running.

Instead of writing an API key directly in Python, we can store it in an environment variable.

Example:

```python
import os

api_key = os.environ.get("ANTHROPIC_API_KEY")
```

This allows the program to retrieve the key without placing the secret directly in the source code.

## 5. The `.env` File

A `.env` file stores configuration values and secrets as environment-variable-style entries.

Example:

```env
ANTHROPIC_API_KEY=your_actual_key
LLM_MODEL=your_available_model_id
```

The `.env` file should be excluded from Git using `.gitignore`.

Example:

```gitignore
.env
.env.*
!.env.example
```

A safe `.env.example` file can be committed to Git because it contains placeholders rather than real credentials.

Example:

```env
ANTHROPIC_API_KEY=your_api_key_here
LLM_MODEL=your_model_id_here
```

Python does not automatically load `.env` files. A package such as `python-dotenv` can load the values into the environment.

Example:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ.get("ANTHROPIC_API_KEY")
```

## 6. SDK-Based API Requests

An SDK means Software Development Kit.

An SDK provides ready-made tools that make it easier for developers to communicate with an API.

For example, the Anthropic Python SDK allows Python applications to make requests without manually constructing every HTTP detail.

Installation:

```bash
python -m pip install anthropic
```

Example:

```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="YOUR_AVAILABLE_MODEL_ID",
    max_tokens=256,
    messages=[
        {
            "role": "user",
            "content": "What is a neural network in one sentence?"
        }
    ]
)

print(response.content[0].text)
```

The SDK reads `ANTHROPIC_API_KEY` from the environment by default.

The model ID must be one that is currently available to the account.

## 7. Raw HTTP API Requests

HTTP stands for Hypertext Transfer Protocol.

It is a communication protocol used to transfer information between clients and servers.

An application can communicate with an API directly through HTTP without using a provider's SDK.

For an Anthropic Messages API request, the endpoint is:

`https://api.anthropic.com/v1/messages`

The request includes:
- An HTTP method, such as POST.
- The API endpoint.
- Request headers.
- A JSON request body.

Important headers include:

```text
Content-Type: application/json
x-api-key: YOUR_API_KEY
anthropic-version: 2023-06-01
```

The API key header shown above is supported by Anthropic. The current authentication documentation also describes Bearer-token authentication.

A raw HTTP request gives the developer more direct control over the request and response. It is also useful for understanding and debugging API communication.

## 8. SDK vs Raw HTTP

| SDK | Raw HTTP |
|---|---|
| Uses a ready-made library. | Sends HTTP requests directly. |
| Less code is usually required. | More request details must be handled manually. |
| Easier for common application development. | Useful for understanding and debugging API communication. |
| Handles some request details automatically. | Gives more direct control over headers and request bodies. |

Both approaches communicate with the same API service.

## 9. Common API Errors

Understanding API errors helps developers identify what went wrong.

| HTTP Status Code | Meaning | Possible Solution |
|---|---|---|
| 400 | Bad Request | Check the request body and parameters. |
| 401 | Unauthorized | Check the API key and authentication. |
| 403 | Forbidden | Check account permissions and access. |
| 404 | Not Found | Check the endpoint or model ID. |
| 429 | Too Many Requests | Wait before retrying and respect rate limits. |
| 500 | Internal Server Error | The service may have a temporary problem. |

### Rate Limits

A rate limit controls how frequently an application can send requests to an API.

For example, a service may limit the number of requests an application can make within a certain period.

When the limit is exceeded, the API may return HTTP 429.

The application should respect the provider's retry instructions, including any `Retry-After` information when supplied.

## 10. Important API Terms

**API:** A way for software applications to communicate.

**API Key:** A credential used to authenticate and authorize API requests.

**Endpoint:** The address where an API request is sent.

**Request:** Information sent from a client to a server.

**Response:** Information returned by a server.

**SDK:** A collection of tools and libraries that simplifies development with a service.

**Token:** A unit of text processed by an AI model. Tokens are relevant to input, output, context limits, and API usage costs.

**Streaming:** A method of receiving a response in smaller pieces as it is generated instead of waiting for the entire response.

**Rate Limit:** A restriction on how frequently API requests can be made.

## 11. Security Principles

1. Never hardcode real API keys in source code.
2. Store secrets in environment variables or an appropriate secret manager.
3. Exclude `.env` files from Git.
4. Use placeholder values in example configuration files.
5. Never share API keys in public repositories, screenshots, or messages.
6. Revoke or rotate a key immediately if it becomes exposed.
7. Check API billing and usage limits before making real requests.

## 12. What I Learned

In this lesson, I learned that APIs allow applications to communicate with external services.

I learned the four important parts of an API request: endpoint, API key, request body, and response body.

I also learned how environment variables and `.env` files help protect sensitive information.

I understood the difference between making API requests through an SDK and sending raw HTTP requests.

Finally, I learned how common HTTP status codes help developers identify authentication problems, missing resources, rate limits, and server errors.

## 13. Practical Work Still to Complete

- [ ] Confirm `.env` is excluded from Git.
- [ ] Configure an API key locally without sharing it.
- [ ] Install and test the Anthropic Python SDK.
- [ ] Make a successful API request.
- [ ] Try the raw HTTP approach.
- [ ] Compare the SDK and raw HTTP responses.
- [ ] Test an authentication error safely.
- [ ] Complete the lesson quiz.