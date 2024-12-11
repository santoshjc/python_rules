"""
1)in this program , within Student class , I have defined all student related properties, which mean
i have bundled up all student related functionality inside my class.

2) but then in line 15 there is a function called get_student() that just exist else where in thus file,
this is not wrong , This will work but then this is not good design principle.
It will be great if we keep get_student() functionality within the class itself. because i will be looking
all student related functionality within the class itself instead of looking down else where in the code.

3) So the class methods allow us to address this bad design principle issue
4) Lets see in oop7.py -->
"""
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    print(student)

def get_student(): #bad design
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__=="__main__":
    main()
