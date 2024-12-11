"""
The word "polymorphism" means "many forms", and in programming it refers
to methods/functions/operators with the same name that can be executed
on many objects or classes.

-----function polymorphism-----
1)An example of a Python function that can be used on different objects
is the len() function.
-For strings len() returns the number of characters
-For tuples len() returns the number of items in the tuple
-For dictionaries len() returns the number of key/value pairs in the dictionary

-----class polymorphism-----
we can have multiple classes(suppose 3 classes, Car, Boat, Plane) with
the same method name:- def move() , Because of polymorphism we can execute
the same method:- move() for all three classes.

-----method overloading-----
inheriting a method in a child class then modifying the logic of that inherited
method in the child class is called overriding, Example below ->
"""
#base class
class Animal:
    def speak(self):
        return "Sound of the animal"

#derived class
class Dog(Animal): #to achive method overriding we much inheritance.
    def speak(self):
        return "bhow bhow !!!"

#derived class
class Cat:
    def speak(self):
        return "meow meow !!!"

#calling Dog class and assigning it to dog variable then calling using dog.speak()
dog = Dog()
print(dog.speak())

#calling Cat class and assigning it to cat variable then calling using cat.speak()
cat = Cat()
print(cat.speak())
