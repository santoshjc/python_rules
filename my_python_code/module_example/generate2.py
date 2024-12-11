import random

number = random.randint(1, 10) # will generate number in 10% probability
print("random is: ",number)

cards = ["jack","queen","king"]
random.shuffle(cards)
for card in cards:
    print("shuffled card is: ", card)



