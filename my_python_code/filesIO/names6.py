names = []

#no need to write "r" implicitly , because r is defaulted
with open("names4.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello,{name}")

"""this concept is called file handling"""
