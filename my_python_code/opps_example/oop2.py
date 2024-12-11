class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Mising name")
        if house not in ["ayush_house", "santosh_house", "binoy_house", "nandu_house"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house


    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__=="__main__":
    main()

"""
NOte- When we define any function within a class , necessarily we have to
pass one 'self' argument so that we have access to the current object
"""
