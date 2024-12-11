def main():
    student = get_student()
    if student[0] == "padma":
        student[1] == "ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("name: ")
    house = input("house: ")
    return [name, house] #as tuble is immutable , but we if we return it as list using [] , the it can be mutable

if __name__== "__main__":
    main()
