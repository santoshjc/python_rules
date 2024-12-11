name = input("what is your name ? ")

with open("names4.txt", "a") as file:
    file.write(f"{name}\n")

"""till now we have seen to write files , now lets
see how to read the files in names5.py"""
