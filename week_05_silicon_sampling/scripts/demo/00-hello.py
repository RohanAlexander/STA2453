#### Preamble ####
# Purpose: First call to a model through OpenRouter; print the answer and the cost
# Author: Rohan Alexander
# Date: 7 October 2026
# Contact: rohan.alexander@utoronto.ca
# License: MIT
# Pre-requisites: uv add openai python-dotenv; OPENROUTER_API_KEY in .env

#### Workspace setup ####
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

#### Call ####
MODEL = "deepseek/deepseek-v4-flash-0731"

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "user", "content": "In one sentence, what is a silicon sample?"}
    ],
    temperature=0.7,
    max_tokens=2000,
)

print(response.choices[0].message.content)
print(response.usage)
