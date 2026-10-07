#### Preamble ####
# Purpose: One persona answers a vote-choice question with a structured output
# Author: Rohan Alexander
# Date: 7 October 2026
# Pre-requisites: as for 00-hello.py

import json
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.environ["OPENROUTER_API_KEY"])

MODEL = "deepseek/deepseek-v4-flash-0731"

persona = (
    "You are a 34-year-old woman who rents an apartment in Toronto's Ward 13, "
    "works in retail, finished high school, and did not vote in the 2022 municipal election."
)

question = (
    "The Toronto mayoral election is on Monday 26 October 2026. "
    "If it were held today, which candidate would you vote for: Olivia Chow, Brad Bradford, "
    "Chris Alexander, someone else, or would you not vote? "
    "How confident are you, from 0 to 100?"
)

schema = {
    "type": "object",
    "properties": {
        "vote": {
            "type": "string",
            "enum": ["Chow", "Bradford", "Alexander", "Other", "Would not vote"],
        },
        "confidence": {"type": "integer", "minimum": 0, "maximum": 100},
    },
    "required": ["vote", "confidence"],
    "additionalProperties": False,
}

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": persona},
        {"role": "user", "content": question},
    ],
    temperature=1.0,
    response_format={
        "type": "json_schema",
        "json_schema": {"name": "vote_choice", "strict": True, "schema": schema},
    },
)

answer = json.loads(response.choices[0].message.content)
print(answer, response.usage.cost)
