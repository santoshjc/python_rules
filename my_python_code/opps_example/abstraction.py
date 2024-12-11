"""
abstraction is used to hide the irrelevant data/class in order to reduce the
complexity. it can be achieved by using abstract classes and interfaces.
A class that consists of one or more abstract method is called the abstract
class. Abstract methods do not contain their implementation. Abstract class
can be inherited by the subclass and abstract method gets its definition in
the subclass, so inheritance should must happen for abstraction.Python does
not have an explicit interface keyword like Java. However, it achieves a
similar concept using abstract classes and duck typing.Python provides the
abc module to use the abstraction in the Python program. example -->
"""

from abc import ABC, abstractmethod

#Abstract base class
class Vehicle(ABC):
    def drive(self): #concrete method
        print("the vehicle is used for driving")

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle): #concrete class
    def start_engine(self):
        print("Car engine started")

def operate_vehicle(vehicle):
    vehicle.start_engine()
    vehicle.drive()

car = Car()
operate_vehicle(car)
