import pandas as pd
df = pd.read_csv("data.csv")
print(df.head())
print(df.tail())
print(df)
print(df.to_string())
print(df.info())