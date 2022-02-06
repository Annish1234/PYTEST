import pytest

def test4():
    word ="selenium"
    assert word.upper() =="SELENIUM"  #"if this appears pull works!!!"
    
@pytest.mark.home
def  test5():
    assert 100==100

def test6():
    assert "annish"=="ANNISH"

@pytest.mark.home
def test_login():
    assert "admin"=="admin"
