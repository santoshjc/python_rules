"""
as we have str,int,float,bool like that we have list
list is lists of all values in one place
for loop can iterate over list of items
"""
for i in [0,1,2]:
    print("meawkela\n")
    #in this i is autometically initialised to 0 then meaw will be printed
    #then python will autometically update i = 1 then meaw will be printed
    #then python will autometically update i = 2 then meaw will be printed
    #and that is it for the values in list it will stop autometically
"""
above program is poorly designed , so not the best way to solve problem
because we cannot put so many no. manually in the list eg:- 1 thousand
so instead of putting value manually ,we will use inbuild function "range()"
"""
for i in range(5):
    print("laura\n")
    #here I am defining i variable but i am not using it, so instead of i
    #we can use _(underscore)

"""
we can also use this shortcut technique
"""
print("meaw_na_kela\n" * 3, end ="")

"""
now lets ask user how many time cat should meaw
when we want to get user input that matched a certain expectation we have
like the input number should be only positive or only negative numbers
then we need do it like this below -
"""
# while True is always true so the loop runs forever.
while True:
    n = int(input("what is n ? "))
    if n>0:
        break # this break statement has the ability to break the recent while loop
for _ in range(n):
    print("meaw_again")

"""now lets do it using a function that we will create"""

def main ():
    number = get_number()
    meaw(number)

def get_number():
    while True:
        n = int(input("what is n ? "))
        if n > 0:
            break
    return n
def meaw(n):
    for _ in range(n):
        print("meaw_na_laura")
main()
