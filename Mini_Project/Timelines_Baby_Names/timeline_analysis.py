import pandas as pd
import matplotlib.pyplot as plt

""" Task 1
Calculate for each name in yob2000.txt its percentage of total births. Store this percentage as an additional column.
"""


def task1():
    df = pd.read_csv("Mini_Project/names/yob2000.txt", header=None)
    total_babies = df[2].sum()
    df["percentage"] = (df[2] / total_babies) * 100
    print(df.head(10))


""" 
Task 2
Read all files yob1880.txt, yob1881.txt ... yob2021.txt. Add an extra column for the year. Concatenate them into a single data structure.
"""


def task2():
    for year in range(1880, 2022):
        df = pd.read_csv(f"Mini_Project/names/yob{year}.txt", header=None)
        df["year"] = year
        if year == 1880:
            df_all = df
        else:
            df_all = pd.concat([df_all, df])
    print(df_all.head(10))
    return df_all

    # df_all.to_csv("Mini_Project/Timelines_Baby_Names/timeline.csv", index=False)


""" Task 3
Calculate the total number of births for each year. Visualize the timeline as a line plot. 
"""


def task3(df_all):
    total_births = df_all.groupby("year")[2].transform("sum")
    df_total_births = pd.DataFrame(
        {"year": df_all["year"], "total_births": total_births}
    )
    df_total_births = df_total_births.drop_duplicates()
    plt.plot(df_total_births["year"], df_total_births["total_births"])
    plt.xlabel("Year")
    plt.ylabel("Total births")
    plt.show()
    return df_total_births


""" Task 4
Now, create a timeline for your own name. First check if your name occurs at all. If yes, create a table with the columns year and number.

You may want to sum up the binary genders or choose one. With few exceptions, the influence on the result is tiny.

If your name is not very frequent, there might be missing data for some years. Insert missing data with a 0.

Draw a line plot and label the axes.
"""


def task4(df_all):
    name = "Richard"
    df_name = df_all[(df_all[0] == name) & (df_all[1] == "M")]
    df_name = df_name.drop(columns=[0, 1])
    df_name = df_name.rename(columns={2: "number"})
    df_name = df_name.set_index("year")
    df_name = df_name.reindex(range(1880, 2022), fill_value=0)
    plt.plot(df_name.index, df_name["number"])
    plt.xlabel("Year")
    plt.ylabel("Number of births")
    plt.show()


""" Task 5
Investigate the popularity of the names of some US celebrities over the last 130 years. Plot a time line with 2-4 names.
Inspect the following celebrities or choose your own:

name	comment
Madonna	wrote "Like a Prayer"
Lance	went to the moon
Barack	president
Katrina	hurricane in New Orleans
Luke	Jedi
Leia	princess from Star Wars
Frida	painter, biography went on a Broadway show
Arielle	mermaid
Harley	it's a chopper
Tyrion	character in 'Game of Thrones'
Khaleesi	job title in 'Game of Thrones' """

pop_persons = [
    {"name": "Madonna", "sex": "F"},
    {"name": "Lance", "sex": "M"},
    {"name": "Barack", "sex": "M"},
    {"name": "Simone", "sex": "F"},
    {"name": "Luke", "sex": "M"},
    {"name": "Leia", "sex": "F"},
    {"name": "Ashton", "sex": "F"},
    {"name": "Arielle", "sex": "F"},
    {"name": "Harley", "sex": "F"},
    {"name": "Tyrion", "sex": "M"},
]


def task5(df_all, pop_persons):
    for pop_person in pop_persons:
        df_pop_name = df_all[
            ((df_all[0] == pop_person["name"]) & (df_all[1] == pop_person["sex"]))
        ]
        df_pop_name = df_pop_name.drop(columns=[0, 1])
        df_pop_name = df_pop_name.rename(columns={2: "number"})
        df_pop_name = df_pop_name.set_index("year")
        df_pop_name = df_pop_name.reindex(range(1880, 2022), fill_value=0)
        plt.plot(df_pop_name.index, df_pop_name["number"], label=pop_person["name"])
        plt.xlabel("Year")
        plt.ylabel("Number of births")
        plt.legend()
        plt.show()


""" Task 6
Finally, we will normalize the data. Repeat Task 5, but divide the count of a given name by the total number of births of that year.
"""


def task6(df_all, df_total_births, pop_persons):
    for pop_person in pop_persons:
        df_normalized = df_all[
            ((df_all[0] == pop_person["name"]) & (df_all[1] == pop_person["sex"]))
        ]
        df_normalized = df_normalized.drop(columns=[0, 1])
        df_normalized = df_normalized.rename(columns={2: "number"})
        df_normalized = df_normalized.set_index("year")
        df_normalized = df_normalized.reindex(range(1880, 2022), fill_value=0)
        df_normalized["number"] = df_normalized["number"].div(
            df_total_births["total_births"].values
        )
        plt.plot(df_normalized.index, df_normalized["number"], label=pop_person["name"])
        plt.xlabel("Year")
        plt.ylabel("Number of births/ total births")
        plt.legend()
        plt.show()


# How does the result change and why is this important?
# The result changes because the number of births is not the same for each year. The number of births is normalized by the total number of births of that year. This is important because it shows the popularity of a name in relation to the total number of births of that year.

task1()
df_all = task2()
df_total_births = task3(df_all)
task4(df_all)
task5(df_all, pop_persons)
task6(df_all, df_total_births, pop_persons)
