import sys

"""sys.exit()"""

#check the error
if len(sys.argv) < 2:
    sys.exit("too few arguments")
elif len(sys.argv) > 2:
    sys.exit("too many arguments")
else:
    print("hello , my name is ", sys.argv[1])
