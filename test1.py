import pytest 

@pytest.mark.login
def test1():
    a =3
    b =4
    assert a+1 ==b 
    assert a==b

def test2():
    name = "selenium"
    assert name.upper() == "SELENIUM"

def test3():
    assert True 

@pytest.mark.login
def test_login():
    assert "admin"=="admin"


def test4():
    assert False

def  test5():
    assert 100==100
    
@pytest.mark.login
def test6():
    assert "annish"=="ANNISH"

   