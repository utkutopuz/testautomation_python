import pytest

@pytest.fixture(scope = "class")   #only once the declaration for the "first" and "last" expressions
#to make the fixture method open to all the test files which need
def setup():
    print("it will be executed first")
    yield   #all the written steps after first executed part, will be before the yield 
    print("it will be the last")


@pytest.fixture()  #define as a fixture
def dataLoad():
    print("user profile data is being createsd")
    return ["Utku", 1998, "ITU"]


@pytest.fixture(params=[("chrome",2008, "Google" ), ("firefox",2004, "Mozilla"), ("bing", 2009 , "Microsoft"), ("Yandex",1997)])
def crossBrowser(request):
    return request.param  #datadriven and parameterization with return
    