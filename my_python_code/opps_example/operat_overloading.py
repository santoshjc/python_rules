class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

#I need to use those special method that come with the class
## and define myself how the vault to be printed as a string using __str__
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"


potter = Vault(10050, 504, 250)
print("harry have: ", potter)

weasley = Vault(100, 50, 25)
print("weasley have: ", weasley)

santosh = Vault(1, 4, 3)
print("santosh have: ", santosh)

"""operator overloading can be used using  __add__ methdod
we will explore it later by ourself
"""
