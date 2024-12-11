class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


    def __str__(self):
        return f"{self.name} from {self.house}"

    #i can call this method without instantiating student menthod,(static variable)
    @classmethod
    def get(cls): # I want to access get method without creating student object. so the convention is to give this method atleast one argument cls which is the reference to the class
        name = input("Name: ")
        house = input("house: ")
        return cls(name, house)
"""
here everything related to the student is inside the student class
"""

def main():
    student = Student.get()
    print(student)


if __name__=="__main__":
    main()
