#### Preamble ####
# Purpose: Ask many personas the same question across several models, with caching and a budget
# Author: Rohan Alexander
# Date: 7 October 2026
# Pre-requisites: uv add openai python-dotenv polars numpy

import hashlib
import json
import os
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np
import polars as pl
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.environ["OPENROUTER_API_KEY"], timeout=60, max_retries=2)

MODELS = ["deepseek/deepseek-v4-flash-0731", "z-ai/glm-5.3-flash", "meta/muse-glimmer-30b"]
TEMPERATURE = 1.0
BUDGET_USD = 2.00
CACHE = Path("cache")
CACHE.mkdir(exist_ok=True)

#### Personas ####
# Twelve Toronto voters from a few marginals, drawn independently, with a fixed seed
rng = np.random.default_rng(seed=853)
N = 12
age = rng.choice(["in your twenties", "in your thirties", "in your forties", "in your fifties", "in your sixties", "over seventy"], size=N)
gender = rng.choice(["a woman", "a man"], size=N)
tenure = rng.choice(["rent", "own your home"], size=N, p=[0.47, 0.53])
area = rng.choice(["downtown", "Scarborough", "North York", "Etobicoke", "East York"], size=N)
personas = [
    f"You are {g} {a} who lives in {ar}, Toronto, and you {t}."
    for g, a, ar, t in zip(gender, age, area, tenure)
]
personas = list(dict.fromkeys(personas))  # drop any duplicates

#### Question ####
question = (
    "The Toronto mayoral election is on Monday 26 October 2026. "
    "If it were held today, which candidate would you vote for: Olivia Chow, Brad Bradford, "
    "Chris Alexander, someone else, or would you not vote? "
    "How confident are you, from 0 to 100?"
)
schema = {
    "type": "object",
    "properties": {
        "vote": {"type": "string", "enum": ["Chow", "Bradford", "Alexander", "Other", "Would not vote"]},
        "confidence": {"type": "integer", "minimum": 0, "maximum": 100},
    },
    "required": ["vote", "confidence"],
    "additionalProperties": False,
}

#### Calls ####
spent = 0.0


def key(model, persona):
    raw = f"{model}|{TEMPERATURE}|{persona}|{question}"
    return hashlib.sha256(raw.encode()).hexdigest()


def ask(model, persona):
    global spent
    path = CACHE / f"{key(model, persona)}.json"
    if path.exists():
        return json.loads(path.read_text())
    if spent >= BUDGET_USD:
        raise RuntimeError(f"Budget of ${BUDGET_USD} reached")
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": persona}, {"role": "user", "content": question}],
        temperature=TEMPERATURE,
        response_format={"type": "json_schema", "json_schema": {"name": "vote_choice", "strict": True, "schema": schema}},
    )
    spent += response.usage.cost
    record = {
        "model_requested": model,
        "model_answered": response.model,
        "persona": persona,
        "raw": response.choices[0].message.content,
        "cost": response.usage.cost,
    }
    path.write_text(json.dumps(record))
    return record


jobs = [(m, p) for m in MODELS for p in personas]
with ThreadPoolExecutor(max_workers=8) as pool:
    records = list(pool.map(lambda mp: ask(*mp), jobs))

#### Results ####
for r in records:
    try:
        answer = json.loads(r["raw"])
        r["vote"], r["confidence"] = answer["vote"], answer["confidence"]
    except (TypeError, ValueError, KeyError):
        r["vote"], r["confidence"] = None, None  # no answer, or not the shape we asked for

df = pl.DataFrame(records)
df.write_parquet("silicon_sample.parquet")
print(df.group_by("model_requested", "vote").len().sort("model_requested", "vote"))
print("Unusable answers:", df["vote"].null_count())
print(f"Spent ${spent:.4f} this run")
