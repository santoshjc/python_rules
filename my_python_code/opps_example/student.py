def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")


def get_name():
    name = input("name: ")
    return name

def get_house():
    house = input("house: ")
    return house


if __name__ == "__main__":
    main()
#this is basically a tuple , typle is immutable , which mean cannot change
