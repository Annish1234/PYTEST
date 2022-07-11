import pytest

def test4():
    word ="selenium"
    assert word.upper() =="SELENIUM"  #"if this appears pull works!!!"
    
@pytest.mark.home
def  test5():
    assert 10==10

def test6():
    assert "ANNISH"=="ANNISH"

@pytest.mark.home
def test_login():
    assert "ADMIN"=="ADMIN"
