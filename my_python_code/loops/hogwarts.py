students = ["hermione", "harry", "ron"]
for i in students:
    print(i)
    #instead of i we can use any variable
""" we cannot use range() function with strings, its only for integers"""
""" in string we can use len() function for string"""


"""
id we want to do operations on strings like out of 10 strings in an list
print the first 5 strings or print the strings from index 2 to 4 etc
then we can use nesting of len() function inside range() function. eg:-"""

students1 = ["ayush", "binoy", "santosh"]

for i in range(len(students1)):
    print(i + 1, students1[i])






