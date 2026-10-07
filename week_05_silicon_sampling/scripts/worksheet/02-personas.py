#### Preamble ####
# Purpose: Make thirty personas from independent marginals and save them
# Author: Your names
# Date: 7 October 2026
# Pre-requisites: uv add polars numpy

import numpy as np
import polars as pl

rng = np.random.default_rng(seed=853)
N = 30

age = rng.choice(["in your twenties", "in your thirties", "in your forties", "in your fifties", "in your sixties", "over seventy"],
                 size=N, p=[0.17, 0.17, 0.16, 0.16, 0.17, 0.17])
gender = rng.choice(["a woman", "a man"], size=N, p=[0.51, 0.49])
education = rng.choice(["did not finish high school", "finished high school", "have some college", "have a bachelor's degree", "have a graduate degree"],
                       size=N, p=[0.09, 0.28, 0.28, 0.22, 0.13])
region = rng.choice(["the Northeast", "the Midwest", "the South", "the West"], size=N, p=[0.17, 0.21, 0.38, 0.24])

personas = pl.DataFrame({"age": age, "gender": gender, "education": education, "region": region}).with_row_index("id")
personas = personas.with_columns(
    (pl.lit("You are ") + pl.col("gender") + pl.lit(" ") + pl.col("age") + pl.lit(" who lives in ")
     + pl.col("region") + pl.lit(" of the United States and ") + pl.col("education") + pl.lit(".")).alias("persona")
)
personas.write_parquet("personas.parquet")
print(personas["persona"][0])
