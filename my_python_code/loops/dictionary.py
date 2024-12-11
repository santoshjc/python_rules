students = {
    "hermione": "Gryffindor",
    "harry":"Gryffindor",
    "ron":"Gryffindor",
    "draco":"slytherin"

}

print(students["hermione"])
print(students["harry"])
print(students["ron"])
print(students["draco"])

"""lets do same thing in more dynamic and simple way"""

#when we use for loop in python to iterate dictionary it iterate the keys only and not the value
for student in students:
    print(student)#here we will only see keys after printing
    print(student, students[student], sep=":- ")#now if i want to print key along with values then we can do this





