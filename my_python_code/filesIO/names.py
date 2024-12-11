""" programs are not permanent in nature , I mean when we turn off the
computer all the content is removed , so I am introducing file I/O concept
by which we can save things in file permanantly in local , cloud env."""

names = []

for _ in range(3):
    names.append(input("what is your name ? "))

for name in sorted(names):
    print(f"hello, {name}")

"""here after running we are prompted to wrire names 3 times and it wil printed
but , if we run the program again , the names we typed get removed , so we need
another wayy to save them permanantly , lets see how in names2.py"""
