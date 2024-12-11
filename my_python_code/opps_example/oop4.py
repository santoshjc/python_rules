import random #import random library

class Hat:

    #in my init funch i have defined a initializationof the object that stores in self.houses the list of four houses
    def __init__(self):
        self.houses = ["gryffindor","hufflepuff","slytherin","ravenclaw"]

    #in sort i am accessing the above list using random to choose one among 4 houses
    def sort(self, name):
        house = random.choice(self.houses)
        print(name, "is in", house)


hat = Hat() # here I am instantiate a hat object.
hat.sort("Harry")
