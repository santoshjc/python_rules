"""
polymorphism can also be achieved using interfaces, but in python we call
it as abstract base class or ABC

NOte:-
1)in simple way , an abstract class is completely an empty class, so even
if we define method in abstract class it will be completely empty.
2)If a method is defined within a class but doesn't have an
implementation (i.e., it's just a declaration), Python considers
it to be abstract, this concept is known as duck typing. so we do not
have to write abstract keyword like we write in java.


example :-
class Animal:
    def make_sound(self):
        pass  # Abstract method because no implementaion is written.

**The Dog and Cat classes must override this method to provide their
own implementations.
"""

from abc import ABC, abstractmethod

#define an abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

#derived class1
class Car(Vehicle):
    def start_engine(self):
        return "car engine started"

#derived class 2
class Motorcycle(Vehicle):
    def start_engine(self):
        return "motorcycle engine start"

#create objects of car and motorcycle
car = Car()
motorcycle = Motorcycle()

#printing just car
print(car.start_engine())
