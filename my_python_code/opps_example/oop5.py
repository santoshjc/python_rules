"""
class variables exist within the class itself and there is
just one copy of that variable for all of the objects. they
all share this class variable.
because the variable is inside the hat , I can now use
this list variable in any of my function.
"""

class Hat:
    houses = ["gryffindor","hufflepuff","slytherin","ravenclaw"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses)) #here house is not a instance variable accessinble via self , instead houses is a class variable which is accessible using via class variable (cls)

# hat = Hat() # here I dont have to instantiate any hat object like i am doing in line 16. I can just use functionality that comes from this class.

Hat.sort("Harry") # I am directly accessing it using class variable


"""NoTe - class variable and class method is same as static variable and static method from java.
Both class variables and methods are shared across all instances of a class. the only difference is
In Python, you use @classmethod and cls to create class methods.
In Java, you use the static keyword to create static methods.
"""
