"""
^ -------> matched the start of the string
$ -------> matched the end of the string or just before the newline at the
         end of the string.
[] ------> set of characters
[^] -----> complementing the set
\w ------> word character, as well as number and the underscores
\d ------> decimal digit
\D ------> not a decimal digit
\s ------> whitespace characters
\S ------> not a whitespace character
\W ------> not a word character
A|B -----> either A or B
(...) ---> a group
(?:...) -> non-capturing version
"""

import re

email = input("what is your email? ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.(com|gov|in|net|edu|org)$", email):
    print("valid")
else:
    print("invalid")

"""now this is the proper regular expression syntax that solves the problem ,
however this looks so cryptic,we have some buildin shortcut to solve the
same problem with the help of above commented symbols"""
