#### Preamble ####
# Purpose: Fit a logistic regression of vote choice, poststratify to the frame, and turn it into a win probability
# Author: Rohan Alexander
# Date: 21 October 2026
# Contact: rohan.alexander@utoronto.ca
# License: MIT
# Pre-requisites: uv sync; data/00-simulated_data/frame.parquet and respondents.parquet from 00-simulate_data.py

#### Workspace setup ####
import json
from datetime import date
from pathlib import Path

import numpy as np
import polars as pl
import statsmodels.formula.api as smf
from patsy import dmatrix

IN = Path("data/00-simulated_data")
OUT = Path("outputs")
OUT.mkdir(exist_ok=True)
rng = np.random.default_rng(seed=853)

frame = pl.read_parquet(IN / "frame.parquet")
respondents = pl.read_parquet(IN / "respondents.parquet")

#### Fit ####
LEVELS = {"age": ["18-34", "35-54", "55+"], "education": ["no degree", "degree"], "housing": ["renter", "owner"]}
cats = [pl.col(c).cast(pl.Enum(v)) for c, v in LEVELS.items()]
model = smf.logit("chow ~ age + education + housing", data=respondents.with_columns(cats).to_pandas()).fit(disp=0)
print(model.summary().tables[1])

#### Poststratify ####
# Predict the share for Chow in every cell of the frame, then weight by the number of adults in the cell.
frame_pd = frame.with_columns(cats).to_pandas()
cell_share = np.asarray(model.predict(frame_pd))
weights = frame["n"].to_numpy() / frame["n"].sum()
estimate = float(np.sum(cell_share * weights))

# Uncertainty from the model: draw coefficient vectors from their sampling distribution, recompute the
# poststratified share for each, and read off an interval and a win probability.
Xf = np.asarray(dmatrix("age + education + housing", frame_pd))  # the right-hand side of the formula
draws = rng.multivariate_normal(model.params.to_numpy(), model.cov_params().to_numpy(), size=2000)
shares = np.array([np.sum(1 / (1 + np.exp(-(Xf @ b))) * weights) for b in draws])
lo, hi = np.percentile(shares, [2.5, 97.5])
win = float(np.mean(shares > 0.5))

#### Save ####
forecast = {
    "race": "Ward 13 councillor (simulated)",
    "date": str(date.today()),
    "share_chow": round(estimate, 3),
    "interval_95": [round(float(lo), 3), round(float(hi), 3)],
    "win_probability": round(win, 2),
    "raw_sample_share": round(float(respondents["chow"].mean()), 3),
}
(OUT / "forecast.json").write_text(json.dumps(forecast, indent=2))
pl.DataFrame({"age": frame["age"], "education": frame["education"], "housing": frame["housing"],
              "n": frame["n"], "share_chow": np.round(cell_share, 3)}).write_parquet(OUT / "cells.parquet")
print(json.dumps(forecast, indent=2))
