with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

"""here we have implimented our own code from scratch that actually
parses, read and interprits a csv file here"""
