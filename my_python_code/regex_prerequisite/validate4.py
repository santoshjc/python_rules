"""
. -----> any character except a newline
* -----> 0 or more repetitions
+ -----> 1 or more repetitions
? -----> 0 or 1 repetitions
{m} ---> m repetitions
{m,n} -> m-n repetitions
^ -----> matched the start of the string
$ -----> matched the end of the string or just before the newline at the
         end of the string.
"""
import re

email = input("what is your email? ").strip()

if re.search(".+@.+", email):
    print("valid")
else:
    print("invalid")

"""here even if we type santsoh@. it will print valid, so wrong approach"""

