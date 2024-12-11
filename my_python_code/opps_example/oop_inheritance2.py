class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    ...

class Student(Wizard):
    def __init__(self, name, house):

        # super() keyword can access the superclass(parent class) which is Wizard,
        ## and then call wizard's __init__ function to student , and I will
        ### pass to the Wizard's init method the name that the student init method is passed
        super().__init__(name)

        self.house = house


    ...


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)

        self.subject = subject

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus","Defence Afainst the Dark Arts")
