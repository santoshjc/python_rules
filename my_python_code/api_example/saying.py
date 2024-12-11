def main():
    hello("world") # i will only call only 'hello' function from say.py file, but goodbye will also got called
    goodbye("world")


def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

if __name__=="__main__": # this is the technique, to understand read code from say.py
    main()
