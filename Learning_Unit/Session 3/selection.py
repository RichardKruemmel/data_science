import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("penguins")
print(df.head(3))

# select one column
print(df["island"])

# select multiple columns (it needs double square brackets as it expects a list of columns)
print(df[["island", "bill_length_mm"]])

# slect rows using a slice
print(df[0:3])

# select rows using a boolean mask
print(df[df["island"] == "Biscoe"])

# select rows using a iloc (position based)
print(df.iloc[0])

# select rows using a loc (label based)
print(df.loc[0])

# mask = (True, False, True, True) * 100[: df.shape]
# print(mask)

# select row and column
print(df.loc[99, "species"])
print(df.iloc[99, 0])

# selection algebra
print(df.loc[(df["island"] == "Biscoe") & (df["bill_length_mm"] > 45)])

# or operator
print(df.loc[(df["body_mass_g"] > 4500) | (df["bill_length_mm"] > 60)])

# Note: logarithmic transformation

# Assumptions that the data is tidy
# Bar plot of heaviest penguins
# First inspect the data
heaviest_penguins = df.sort_values(by="body_mass_g", ascending=False).head(5)
heaviest_penguins["body_mass_g"].plot.bar()

# mean weight by species
mean_weight = df.groupby("species")["body_mass_g"].mean()
print(mean_weight)
mean_weight.plot.bar()

# line plot does not make sense with penguins
flight = sns.load_dataset("flights")
flight["passengers"].plot.line()
