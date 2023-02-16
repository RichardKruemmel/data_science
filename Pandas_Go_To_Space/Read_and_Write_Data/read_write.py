import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df_penguin = pd.read_csv(
    "Pandas_Go_To_Space/Read_and_Write_Data/penguin_sector.csv",
    index_col=0,
    sep=",",
    header=0,
)
df_panda = pd.read_csv(
    "Pandas_Go_To_Space/Read_and_Write_Data/panda_sector.csv",
    index_col=0,
    sep=",",
    header=0,
)
df_amoeba = pd.read_csv(
    "Pandas_Go_To_Space/Read_and_Write_Data/amoeba_sector.csv",
    index_col=0,
    sep=",",
    header=0,
)

df = pd.concat([df_panda, df_penguin, df_amoeba])
print(df)
sns.scatterplot(data=df, x="x", y="z", size="size", hue="class")
# plt.show()

# How many planets are there in all three star maps combined?
print("There are", len(df), "planets in all three star maps combined.")
print(df.shape[0])
