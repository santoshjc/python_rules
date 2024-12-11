"""
decorator(@) in python is a way to decorate the functions
it is basically a functions to modify the behaviour
of other function, lets see example :-
"""
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Mising name")
        self.name = name
        self.house = house


    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter
    @property
    def house(self):
        return self._house

    # Setter
    @house.setter
    def house(self, house):
        if house not in ["ayush_house", "santosh_house", "binoy_house", "nandu_house"]:
            raise ValueError("Invalid house")
        self._house = house

def main():
    student = get_student()
    #student.house = "new house name overwritten here"
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__=="__main__":
    main()
"""
unfortunately if i have an instance variable called name
and house, then i cannot also have fucntions called house
they will collide so we to fix it :-
using ._ (in line 20, 27) underscore

NOte - after running this program it will show valueError
because in line 31 , I am maliciously trying to change house
to not be one of the four valid houses but something different
to check the outout , remove the # in line 31

"""
