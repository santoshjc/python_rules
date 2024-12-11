"""
encapsulation is the way of wrapping data(variables) and methods(functions)
together as a single unit.This puts restrictions on accessing variables and
methods directly and can prevent the accidental modification of data. In java
we use access specifiers like (public, private,protected)etc but incase of
python we write "__" double underscore to denote private.,and "_" single underscore
to denote protected. we use getters and setters to achieve encapsulation.

*a private variable cannot be accessed outside the class
*a protected variable can be accessed using derived class only but not
outside class
"""

class Person:
    def __init__(self, name, age, gender):
        self.__name = name   #private variable
        self.__age = age     #private variable
        self.gender = gender #public variable

#it will be in '_Person__age', '_Person__name'format in directory cuz its private
person = Person("santosh", 27, "male")

#gender will be availabe in directory as its public
print(dir(person))

"""
as we are not able to access the private variables from outside the class,
can we access it from methods that are present inside the class ? yes,
using getters and setters. see encapsulation2.py .
"""
