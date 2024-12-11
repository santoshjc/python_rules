with open("names4.txt", "r") as file: # r mean read
    lines = file.readlines() # reading all line and returning me the list

for line in lines:
    print("hello,",line.rstrip())

"""now lets do the same thing in shortcut in a sorted
way in names6.py"""
