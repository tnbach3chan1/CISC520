import pandas as pd

df = pd.read_parquet("brfss_2025.parquet")
print(df.shape)
print(df.head())

