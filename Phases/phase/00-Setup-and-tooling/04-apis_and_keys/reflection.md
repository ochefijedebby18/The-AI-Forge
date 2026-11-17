# Phase 00 — Lesson 04: APIs & Keys

This lesson helped me understand how applications communicate with external services through APIs.

Before this lesson, I understood that applications could use AI models, but I did not fully understand how an application sends information to an external AI service and receives a response.

I learned that an API request involves four important components: an endpoint, an API key, a request body, and a response body. Each component has a specific purpose in the communication process.

One of the most important things I learned was how to handle API keys securely. I now understand why hardcoding API keys inside source code is dangerous. If I accidentally upload a project containing a real API key to GitHub, someone else could access and misuse that credential.

I also learned how environment variables and `.env` files help separate sensitive configuration from application code. I understand that `.env` files must be excluded from Git and that example configuration files should contain placeholders rather than real secrets.

Another important part of this lesson was understanding the difference between SDK-based requests and raw HTTP requests. An SDK provides ready-made tools that simplify API communication, while raw HTTP allows developers to construct requests and inspect their components more directly.

I also learned that API errors are useful information rather than simply signs that a program has failed. For example, HTTP 401 indicates an authentication problem, HTTP 404 indicates that a resource may not exist, and HTTP 429 indicates that a rate limit has been reached.

### What I Found Important

The most important lesson for me was that building AI applications is not only about understanding machine learning models. It also involves understanding how software communicates with AI services, how to manage credentials, and how to handle errors.

Security is especially important because an exposed API key can create financial and security risks.

### What I Still Need to Practise

I still need practical experience with:
- Configuring an API key securely on my computer.
- Making my first successful API request using the Anthropic Python SDK.
- Sending the same request using raw HTTP.
- Comparing the two approaches.
- Understanding API error messages through practical testing.

These practical exercises will help me move from understanding API concepts to using APIs independently in Python applications.

### Final Reflection

This lesson introduced me to an important part of AI engineering: connecting software applications to external AI services.

I now understand the basic structure of an API request, why API keys must be protected, and how SDKs and raw HTTP requests are used to communicate with APIs.

My next goal is to complete the practical exercises and build confidence in making secure API requests from Python.

I want to be able to use these skills when developing real AI applications, including applications that communicate with language models and other AI services.