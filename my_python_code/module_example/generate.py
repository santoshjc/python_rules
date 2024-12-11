import random # it will import everything from random
coin = random.choice(["head\n","tail\n"])
print(coin)

""" from is the keyword in python that we can use when importing functions
from module but it allows us to be more specific"""

from random import choice

coin = choice(["tera","mera"])
print(coin)



