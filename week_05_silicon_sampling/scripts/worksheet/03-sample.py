#### Preamble ####
# Purpose: Thirty personas, three models, two prompts; save the sample
# Author: Your names
# Date: 7 October 2026
# Pre-requisites: silicon.py and personas.parquet in this folder

from concurrent.futures import ThreadPoolExecutor

import polars as pl
from silicon import *

QUESTION = (
    "The election for the United States House of Representatives is on Tuesday 3 November 2026. "
    "If it were held today, would you vote for the Democratic candidate, the Republican candidate, "
    "someone else, or would you not vote? How confident are you, from 0 to 100?"
)
PROMPTS = {
    "neutral": QUESTION,
    "framed": "Prices for groceries and rent have risen a lot over the past year. " + QUESTION,
}
personas = pl.read_parquet("personas.parquet")

jobs = [(m, name, row["id"], row["persona"]) for m in MODELS for name in PROMPTS for row in personas.iter_rows(named=True)]


def run(job):
    model, name, pid, persona = job
    return {"prompt": name, "id": pid, **ask(model, persona, PROMPTS[name])}


with ThreadPoolExecutor(max_workers=8) as pool:
    records = list(pool.map(run, jobs))

df = pl.DataFrame(records).join(personas.drop("persona"), on="id")
df.write_parquet("silicon_sample.parquet")
print(df.group_by("model_requested", "prompt", "vote").len().sort("model_requested", "prompt", "vote"))
print(f"Spent ${total_spent():.4f}")
