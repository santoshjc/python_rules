"""example of why inheritance is required, instead
of this way """

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    ...

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house


    ...


class Professor:
    def __init__(self, name, subject):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.subject = subject

"""
this program is will cause redundancy , We can use
inheritance to solve this problem in oop_inheritance2.py -->
"""