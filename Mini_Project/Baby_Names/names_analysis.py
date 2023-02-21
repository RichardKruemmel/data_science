import pandas as pd

""" Task 1
Inspect the file yob2021.txt in a text editor. What do you observe about the structure of the file?

Usually these questions are the most relevant:

How many columns are there?
31537
How are columns separated?
,
Is there a header on top of the files?
No
"""

""" Task 2
Read the file 'yob2021.txt' into pandas.

"""

baby_names = pd.read_csv("Mini_Project/names/yob2021.txt", header=None)

""" Task 3
Print the first 10 rows. """
print(baby_names.head(10))

""" Task 4
Display the number of rows and columns.
 """

print("columns: ", baby_names.shape[0], "rows: ", baby_names.shape[1])

""" Task 5
Calculate the total number of babies born in 2021, i.e. the sum of the third column. """
total_babies = baby_names[2].sum()
print(total_babies)

""" Task 6
Like Task 5, but calculate the sum for boys and girls separately.
    """
total_girls = baby_names[baby_names[1] == "F"][2].sum()
total_boys = baby_names[baby_names[1] == "M"][2].sum()
print("Boys: ", total_boys)
print("Girls: ", total_girls)

""" Task 7
Check if your name occurs in the data.
    """
print("My name is in the data: ", "Richard" in baby_names[0].values)

""" Task 8
Calculate the percentage of girls and boys among the total births.
"""
print("Girls Percentage:", total_girls / total_babies * 100)
print("Boys Percentage:", total_boys / total_babies * 100)

"""Task 9
Create a table that contains the top 5 girls names and top 5 boys names."""

top_five_girls = (
    baby_names[baby_names[1] == "F"].sort_values(by=2, ascending=False).head(5)
)
top_five_boys = (
    baby_names[baby_names[1] == "M"].sort_values(by=2, ascending=False).head(5)
)

top_five_babies = pd.concat([top_five_girls, top_five_boys])
print(top_five_babies)

"""Task 10
Write the data from task 9 to an Excel spreadsheet.
"""
top_five_babies.to_excel("Mini_Project/Baby_Names/top_five_babies.xlsx")
