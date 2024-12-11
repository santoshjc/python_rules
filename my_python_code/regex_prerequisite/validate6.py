"""^ -----> matched the start of the string
$ -----> matched the end of the string or just before the newline at the
         end of the string.
[] ----> set of characters
[^] ---> complementing the set 
"""

import re

email = input("what is your email? ").strip()

if re.search(r"^.+@.+\.edu", email):
    print("valid")
else:
    print("invalid")
