"""
the generall purpose tool that allow us to create our own data types as well
and give it a name , it is known class, a class is a blueprint for pieces of
data(object).
"""
class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    student = Student() # here I am creating an object(instance) of Student class
    student.name = input("Name: ")#in oop2.py we we see more nice technique to do , instead of this 
    student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()
