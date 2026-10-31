import pandas as pd

df = pd.read_sas("LLCP2025.XPT", format="xport", encoding="latin-1")
# df.to_csv("brfss_2025.csv", index=False)
# or, for a much smaller and faster file:
df.to_parquet("brfss_2025.parquet")