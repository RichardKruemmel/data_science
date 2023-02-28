import pandas as pd
import matplotlib.pyplot as plt

""" Analyze which last letters appear most frequently in first names.

Task 1
Read all files from the Baby Name Dataset into a single DataFrame. The DataFrame should have the columns name, gender, number and year.

"""


def task1():
    for year in range(1880, 2022):
        df = pd.read_csv(f"Mini_Project/names/yob{year}.txt", header=None)
        df["year"] = year
        if year == 1880:
            df_all = df
        else:
            df_all = pd.concat([df_all, df])
    df_all = df_all.rename(columns={0: "name", 1: "gender", 2: "number"})
    return df_all


"""
Task 2
Create an extra column with the last letter of each name.

Create string indexes for an entire column with the expression

df[col].str[i]
Alternatively, write a function that returns the last letter and use it to create a pd.Series:

df[col].apply(my_func)

"""


def task2(df_all):
    df_all["last_letter"] = df_all["name"].str[-1]
    return df_all


"""
Task 3
Create a bar plot showing the count of each last letter.
"""


def task3(df_all):
    df_all["last_letter"].value_counts().plot(kind="bar")
    plt.savefig(
        "Mini_Project/Last_letters/barplot.png",
        dpi=150,
    )
    plt.show()


"""
Task 4
Now, create a timeline for one last letter.

First, select that letter over all years. Second, group by the year and calculate the count for each year. The resulting table should look like this:

year  count
1880    300
1881    317
1882    342
...
Finally, create a line plot from this data.
"""


def task4(df_all):
    df = df_all[df_all["last_letter"] == "a"]
    df = df.groupby("year")["number"].sum()
    df.plot()
    plt.savefig(
        "Mini_Project/Last_letters/timeline_a.png",
        dpi=150,
    )
    plt.show()


"""
Task 5
Let's plot multiple timelines.

Count the names grouped by last letter and year. Use the expression:

df.groupby([col1, col2])[col3].count()
The resulting table should look something like this:

last  year
a     1880    31446
      1881    31581
      1882    36536
...
b     1880     5432
This DataFrame has a hierarchical index.

Convert the DataFrame to a crosstable that has the year in the row index and the letters in the column index. You can do this with the expression

df.unstack(0)
Draw a line plot showing the frequency of the letters d, n and y. Try other ones if you like.
"""


def task5(df_all):
    df = df_all.groupby(["last_letter", "year"])["number"].sum()
    df = df.unstack(0)
    df[["d", "n", "y"]].plot()
    plt.savefig(
        "Mini_Project/Last_letters/mult_timelines.png",
        dpi=150,
    )
    plt.show()


"""
Task 6
Finally, let's look for frequent first/last letter combinations.

Add an extra column containing the first letter.
Cross-tabulate by grouping by first and last letter and count the names (over all years).
Now you should have a table with first letters in columns and last letters in rows (or vice versa).

Plot a heatmap (check the Seaborn Example Gallery).

Hints:
To make the plot nicer convert the names to upper or lower case at the very beginning with:

df['name'].str.uppper()
You also might sort the table by rows:

df.sort_values(by=col, axis=0`)
For sorting by columns, set axis=0

"""


def task6(df_all):
    df_all["first_letter"] = df_all["name"].str[0]
    df = df_all.groupby(["first_letter", "last_letter"])["number"].sum()
    df = df.unstack(0)
    df = df.fillna(0)
    df = df.sort_values(by="A", axis=0)
    df = df.sort_values(by="a", axis=1)
    print(df.head(10))
    plt.figure(figsize=(10, 10))
    plt.xticks(range(26), df.columns)
    plt.yticks(range(26), df.index)
    plt.title("First and last letter combinations")
    plt.xlabel("First letter")
    plt.ylabel("Last letter")
    plt.imshow(df, cmap="hot")
    plt.savefig(
        "Mini_Project/Last_letters/heatmap.png",
        dpi=150,
    )
    plt.show()


"""

Task 7
Save your plots to .png files with 150 dpi.

Task 8
What visualization(s) would you use to compare the last letters of girls and boys?
bar plot with two bars for each gender
"""


def task8(df_all):
    # Create stacked bar for each gender and each letter sorted by total count
    df = df_all.groupby(["last_letter", "gender"])["number"].sum()
    df = df.unstack(1)
    df = df.fillna(0)
    df["total"] = df["F"] + df["M"]
    df = df.sort_values(by="total", axis=0, ascending=False)
    df = df.drop("total", axis=1)
    df.plot(kind="bar", stacked=True)
    plt.title("Last letter occurance based on gender")
    plt.xlabel("Last letter")
    plt.ylabel("Count")
    plt.xticks(range(26), df.index)
    plt.show()


df_all = task1()
df_all = task2(df_all)
task3(df_all)
task4(df_all)
task5(df_all)
task6(df_all)
# task7 is done inside the relevant tasks
task8(df_all)


"""
Hints:
Instead of the count, you can use the sum instead.
You might also try to log-transform the data with np.log before plotting.
It might be a good idea to normalize the data before plotting.
Of course, the entire analysis also can be done for first letters, but for the last letters a research paper exists that had quite an impact. """
