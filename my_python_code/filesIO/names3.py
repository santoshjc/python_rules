name = input("what is your name? ")

#`open` function is used to open a file programatically , to read and write
file = open("names3.txt", "a") #a mean append
file.write(f"{name}\n")
file.close()

"""instead of `open and close` function we can
also do it using `with` keyword , in names4.py"""
