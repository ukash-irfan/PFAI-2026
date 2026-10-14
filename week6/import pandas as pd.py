import pandas as pd

df = pd.read_csv("file.csv", na_values=["", "missing", "N/A"])
selected = df.loc[(df["score"] >= 50) & (df["attendance"] >= 75)]
df["score"] = pd.to_numeric(df["score"], errors="coerce")
