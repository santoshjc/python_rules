def main():
    student = get_name()
    if student["name"] == "padma":
        student["house"] == "ravenclaw"
    print(f"{student['name']} from {student['house']}")

def get_name():
    name = input("Name: ")
    house = input("house: ")
    return {"name": name, "house": house}

if __name__=="__main__":
    main()
# here we have used dictionary instead of using indexes
"""
now lets see OOPS in oop1.py

"""
