import sys

#check the error
if len(sys.argv) < 2:
    print("too few arguments")
elif len(sys.argv) > 2:
    print("too many arguments")
else:
    print("hello , my name is ", sys.argv[1])
