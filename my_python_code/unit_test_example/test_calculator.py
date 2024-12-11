"""
from calculator import square

def main():
    test_square()

 # this is convention , if the program that i am testing is square() then-
 ## my function should be test_square()
def test_square():
    try:
        assert square(2)== 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3)== 9
    except AssertionError:
        print("3 squared was not 9")

if __name__=="__main__":
    main()

 this is so big unit test code , even bigger then the actual code
so we will not do it in such way instead , we will do it using pytest """


from calculator import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
#pip install pytest
##to execute run `pytest test_calculator.py`
