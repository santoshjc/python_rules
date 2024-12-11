import sys

from saying import hello # from saying.py file

if len(sys.argv) == 2:
    hello(sys.argv[1]) # `sys.argv[1]` will hopefully be the person's name,which i expect the person to type in the prompt

""" unfortunately this program will print all the function
available in saying.py (hello, goodbye, etc) because it
will read line of code from top to bottom"""

"""so to avoid this problem which print all function
instead of which i wanted to print. I can use this
technique, the techniques is to , rename my main funct
from just `main()` to `if __name__=="__main__":`
__name__ is special variable whose variable is autometically
set by python to be "main" when we run a file from the
command line"""
