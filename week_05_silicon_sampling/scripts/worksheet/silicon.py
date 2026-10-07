#### Preamble ####
# Purpose: Client, models, schema, and one cached structured call, shared by the worksheet scripts
# Author: Your names
# Date: 7 October 2026
# Pre-requisites: uv add openai python-dotenv polars numpy; OPENROUTER_API_KEY in .env

import hashlib
import json
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
    timeout=60,
    max_retries=2,
)

MODELS = ["deepseek/deepseek-v4-flash-0731", "z-ai/glm-5.3-flash", "meta/muse-glimmer-30b"]
OPTIONS = ["Democratic", "Republican", "Other", "Would not vote"]
SCHEMA = {
    "type": "object",
    "properties": {
        "vote": {"type": "string", "enum": OPTIONS},
        "confidence": {"type": "integer", "minimum": 0, "maximum": 100},
    },
    "required": ["vote", "confidence"],
    "additionalProperties": False,
}
BUDGET_USD = 2.00
CACHE = Path("cache")
CACHE.mkdir(exist_ok=True)
spent = 0.0


def total_spent():
    """Dollars spent so far in this run. Call this rather than reading `spent`, which `import *` copies once."""
    return spent


def ask(model, persona, question, temperature=1.0, draw=0):
    """One structured answer. Cached on everything that determines it, so a rerun costs nothing.
    `draw` lets you ask the same persona the same question more than once."""
    global spent
    raw = f"{model}|{temperature}|{draw}|{persona}|{question}"
    path = CACHE / (hashlib.sha256(raw.encode()).hexdigest() + ".json")
    if path.exists():
        return json.loads(path.read_text())
    if spent >= BUDGET_USD:
        raise RuntimeError(f"Budget of ${BUDGET_USD} reached")
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": persona}, {"role": "user", "content": question}],
        temperature=temperature,
        response_format={"type": "json_schema", "json_schema": {"name": "vote", "strict": True, "schema": SCHEMA}},
    )
    spent += response.usage.cost
    try:
        answer = json.loads(response.choices[0].message.content)
        answer = {"vote": answer["vote"], "confidence": answer["confidence"]}
    except (TypeError, ValueError, KeyError):
        answer = {"vote": None, "confidence": None}  # no answer, or not the shape we asked for
    record = {
        "model_requested": model,
        "model_answered": response.model,
        "temperature": temperature,
        "draw": draw,
        "persona": persona,
        "question": question,
        "cost": response.usage.cost,
        **answer,
    }
    path.write_text(json.dumps(record))
    return record
