import re

email = input("what is your email? ").strip()

if re.search(r".+@.+\.edu", email): #if we want the email to end with .edu, but . has different meaning in regex. so we will use \n
    print("valid")
else:
    print("invalid")

"""it better then previous code , but still there is a fault
here , if we type santosh.harvard.edu, it will still considered
as valid."""
