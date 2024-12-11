email = input("what is your email? ")

username, domain = email.split("@")

if (username) and domain.endswith(".edu"):
    print("valid")
else:
    print("invalid")

"""this is the way by which we can validate in python , but if we do in this
way , our code will become so much big because there will be so many if,
else , and conditional statements and our code will become big , so in python
we have "re" library to check , define and validate pattern . see validate3.py"""
