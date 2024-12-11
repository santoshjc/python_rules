email = input("what is your email? ").strip() #strip will remove whitespaces(both leading and trailing)

if "@" in email and "." in email:
    print("valid")
else:
    print("invalid")

"""faulty program because just typing @ and . can show us valid result"""

