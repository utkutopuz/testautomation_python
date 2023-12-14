
import pytest


@pytest.mark.smoke  
def test_greeting(setup):
    print("Hello")
    

def test_goodbye():
    print("stay well")
    

def test_crossBrowser(crossBrowser):
    print(crossBrowser)
    print(crossBrowser[1])
    

    

