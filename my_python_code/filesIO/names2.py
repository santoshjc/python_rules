name = input("what is your name? ")

#`open` function is used to open a file programatically , to read and write
file = open("names2.txt", "w") #create the file names.txt and w mean write to it
file.write(name)
file.close() # close and saves the file

"""this program has one fault , it will not write to the file when new name
is types , instead it will recreate the file with new content , because
i have used `w`. lets see how to solve it in names3.py"""
