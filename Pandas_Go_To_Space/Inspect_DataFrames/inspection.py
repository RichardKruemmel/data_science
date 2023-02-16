import pandas as pd

df = pd.read_csv(
    "Pandas_Go_To_Space/Inspect_DataFrames/ship_inspection.csv",
    index_col="station",
    sep=",",
    header=0,
)

# print(df.head(3))
# print(df.tail(3))
# print(df.shape)
# print(df.dtypes)
# print(df.info())
# print(df["security"].value_counts())
# print(df["status"].unique())

# How many life forms are there on the bridge?
print(df.loc["bridge", "life forms"].sum())

# How many stations does the ship have?
print(df.shape[0])

# How many different security levels are there?
print(df["security"].nunique())

# There is one life support value that is neither 0 or 100%. How much is it?
print(
    df.loc[
        (df["life support [%]"] != 0) & (df["life support [%]"] != 100),
        "life support [%]",
    ].sum()
)
