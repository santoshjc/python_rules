x = int(input("what is x ? "))
if x % 2 == 0:
    print("Even")
else:
    print("Odd")

    """
    or by using fucntion
    """
def main():
		x2 = int(input("what is x2 ? "))
		# just assume that the function named is_even already exist ! even if its not avilable yet , we can create later
		if is_even(x2):
			print("Even")
		else:
			print("Odd")

	#now here we will invent our own function named is_even,and We want this function to take one argument (n) generic.
def is_even(n): #here the value of x2 variable with assigned in n variable.
		if n % 2 == 0:
			return True
		else:
			return False
main()
# Now I am using the function that I invented on line no. 13 .

