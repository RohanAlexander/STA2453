#### Preamble ####
# Purpose: Average marginal effects and predictions by group from the vote-choice model, saved as tables
# Author: Rohan Alexander
# Date: 21 October 2026
# Contact: rohan.alexander@utoronto.ca
# License: MIT
# Pre-requisites: uv sync; data/00-simulated_data/respondents.parquet from 00-simulate_data.py

#### Workspace setup ####
from pathlib import Path

import polars as pl
import statsmodels.formula.api as smf
from marginaleffects import avg_predictions, avg_slopes

IN = Path("data/00-simulated_data")
OUT = Path("outputs")
OUT.mkdir(exist_ok=True)

LEVELS = {"age": ["18-34", "35-54", "55+"], "education": ["no degree", "degree"], "housing": ["renter", "owner"]}
respondents = pl.read_parquet(IN / "respondents.parquet").with_columns(
    pl.col(c).cast(pl.Enum(v)) for c, v in LEVELS.items()
)
model = smf.logit("chow ~ age + education + housing", data=respondents.to_pandas()).fit(disp=0)

#### Marginal effects ####
# A logit coefficient is a change in log-odds, which nobody can picture. An average marginal effect is the
# average change in the probability of voting for Chow when one variable changes and the others stay as they are.
slopes = avg_slopes(model)
print(slopes)

# The predicted share for Chow by age group, averaging over the education and housing of the respondents.
by_age = avg_predictions(model, by="age")
print(by_age)

#### Save ####
pl.DataFrame(slopes).write_parquet(OUT / "marginal_effects.parquet")
pl.DataFrame(by_age).write_parquet(OUT / "predictions_by_age.parquet")
