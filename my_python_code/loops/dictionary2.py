"""to compose a list of dictionary"""

students = [
    {"name":"hermione", "house":"gryffindor","patronus":"otter"},
    {"name":"harry", "house":"gryffindor","patronus":"otter"},
    {"name":"ron", "house":"gryffindor","patronus":"otter"},
    {"name":"draco", "house":"slytherin","patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=":- " )

"""
one of the features of python is that it make these dictionaries highly
performant for us even if the dictionary is very large, we can manipulate
those data quickly, there are inbuild function that we can use like sort etc
"""


