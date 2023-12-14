
import pytest
from math import sqrt


@pytest.mark.smoke   #tagging by using -m in the CLI
@pytest.mark.skip()   #to skip the method
def test_greeting():
    msg = "Hello"
    assert msg == "Hi", "Test failed because of the string matching"
    

def test_squarenumber():
    a = 49
    b = 1024
    c = 5006

    assert sqrt(a).is_integer(), f"{a} is not a square number"
    assert sqrt(b).is_integer(), f"{b} is not a square number"
    assert not sqrt(c).is_integer(), f"{c} is not a square number"


@pytest.mark.xfail   #running but not reporting(xpassed)
def test_goodbyeword():   #use -k to test multiple method by a specific word
    word = "bye"
    assert word =="bye", "goodbye has not done properly"


