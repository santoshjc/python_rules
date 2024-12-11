""" a slice is the subset of a list"""

import sys

#check the error
if len(sys.argv) < 2:
    sys.exit("too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)

