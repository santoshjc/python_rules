"""
<----Remove the duplicates--->
"""

students = [
    {"name":"Hermione","house":"Gryffindor"},
    {"name":"Harry","house":"Gryffindor"},
    {"name":"Ron","house":"Gryffindor"},
    {"name":"Draco","house":"Slytherin"},
    {"name":"Padma","house":"Ravenclaw"},
]

#empty list here i will store each house uniquely.
houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

# for ech houses name that I have stored in empty list houses
for house in sorted(houses):
    print(house)

