""" re.search(pattern, string, flags=0)
pattern is argument that I want to search for in string that same from user
string argument here is the actual string that we gonna search for the pattern"""

import re

email = input("what is your email ? "). strip()

if re.search("@", email):
    print("valid") #this means re.search contains @ in the email then print valid
else:
    print("invalid")

"""here in this program also we are using re library but in console if we
only type @ then also it will print valid, lets do this using regex rules

. -----> any character except a newline
* -----> 0 or more repetitions
+ -----> 1 or more repetitions
? -----> 0 or 1 repetitions
{m} ---> m repetitions
{m,n} -> m-n repetitions


lets see this in validate4.py
"""
