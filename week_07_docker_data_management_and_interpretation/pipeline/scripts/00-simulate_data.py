#### Preamble ####
# Purpose: Simulate a poststratification frame for one ward and a set of respondents, and save both
# Author: Rohan Alexander
# Date: 21 October 2026
# Contact: rohan.alexander@utoronto.ca
# License: MIT
# Pre-requisites: uv sync

#### Workspace setup ####
from pathlib import Path

import numpy as np
import polars as pl

rng = np.random.default_rng(seed=853)
OUT = Path("data/00-simulated_data")
OUT.mkdir(parents=True, exist_ok=True)

#### Frame ####
# One row per cell of age by education by housing, with the number of adults in the ward in that cell.
# The shares are rough. A real frame comes from the census ward profile.
age = ["18-34", "35-54", "55+"]
education = ["no degree", "degree"]
housing = ["renter", "owner"]
cells = [(a, e, t) for a in age for e in education for t in housing]
p_age = {"18-34": 0.30, "35-54": 0.35, "55+": 0.35}
p_edu = {"no degree": 0.55, "degree": 0.45}
p_housing = {"renter": 0.47, "owner": 0.53}
ward_adults = 48_000
frame = pl.DataFrame({
    "age": [a for a, _, _ in cells],
    "education": [e for _, e, _ in cells],
    "housing": [t for _, _, t in cells],
    "n": [round(ward_adults * p_age[a] * p_edu[e] * p_housing[t]) for a, e, t in cells],
})
frame.write_parquet(OUT / "frame.parquet")

#### Respondents ####
# 600 respondents whose mix does not match the frame: too many degree holders and too many renters,
# which is what a convenience or online sample looks like. Vote choice depends on all three variables.
n = 600
r_age = rng.choice(age, n, p=[0.25, 0.35, 0.40])
r_edu = rng.choice(education, n, p=[0.35, 0.65])
r_housing = rng.choice(housing, n, p=[0.65, 0.35])
lp = (-0.2 + 0.7 * (r_housing == "renter") + 0.4 * (r_edu == "degree")
      + 0.3 * (r_age == "18-34") - 0.4 * (r_age == "55+"))
chow = rng.binomial(1, 1 / (1 + np.exp(-lp)))
respondents = pl.DataFrame({"age": r_age, "education": r_edu, "housing": r_housing, "chow": chow})
respondents.write_parquet(OUT / "respondents.parquet")

print(frame)
print(f"{n} respondents, {chow.mean():.3f} for Chow in the raw sample")
