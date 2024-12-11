"""sys is a module called system"""

import sys

print("hello my name is", sys.argv[1])
print("too few arguments")

try:
    print("hello my name is", sys.argv[1])
except IndexError:
    print("too few arguments")
