import polars as pl

df = pl.read_parquet("silicon_sample.parquet")
cells = (
    df.group_by("model_requested", "prompt")
    .agg(
        (pl.col("vote") == "Democratic").sum().alias("dem"),
        (pl.col("vote").is_in(["Democratic", "Republican", "Other"])).sum().alias("voters"),
        (pl.col("vote") == "Would not vote").mean().alias("share_not_voting"),
        pl.col("confidence").mean().alias("conf_mean"),
        pl.col("confidence").std().alias("conf_sd"),
    )
    .with_columns((pl.col("dem") / pl.col("voters")).alias("dem_share"))
    .sort("model_requested", "prompt")
)
print(cells)
